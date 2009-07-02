from __future__ import generators

import codecs
from pprint import pprint as pp

# How to interpret an empty alias.
IMPLIED_ALIAS = 'Latin-1'

# Special coding name for Python internal Unicode strings.
UNICODE_STRING = '<Ustring>'

# Special coding name for unapplied or removed surface.
TRIVIAL_SURFACE = '<Data>'

# Unicode zero width no-break space.
BYTE_ORDER_MARK = u'\uFEFF'

# Unicode replacement character.
REPLACEMENT_CHARACTER = u'\uFFFD'

# Unicode byte order mark swapped.
BYTE_ORDER_MARK_SWAPPED = u'\uFFFE'

# Not a Unicode character.
NOT_A_CHARACTER = u'\uFFFF'

# Defined errors.
class error(Exception): pass
class NotImplementedError(error): pass
class UnknownWordError(error): pass
class AmbiguousWordError(error): pass
class UnresolvedRecodecError(error): pass
class ComplexRecodecError(error): pass

## Miscellaneous routines.

def cleaned_alias(name):
    return registry.aliases.cleaned(name)

class Aliases:
    # Aliases is a dictionary-like object, for which any non-ambiguous
    # abbreviation of a key may be used to retrieve a value.  The key
    # itself, not abbreviated, may always be use to retrieve a value even
    # if that key happens to be the prefix of another one.  Once set, a
    # key value may not changed.  If two different keys a common prefix,
    # this prefix and abbreviations thereof are not ambiguous if both
    # keys yield the same value.
    def __init__(self):
        self.table = {}
        import string
        self.clean_table = string.maketrans(
            string.ascii_uppercase, string.ascii_lowercase)

    def __getitem__(self, key):
        key = self.cleaned(key)
        try:
            exact, value = self.table[key]
        except KeyError:
            raise UnknownWordError, repr(key)
        if value is None:
            raise AmbiguousWordError, repr(key)
        return value

    def __setitem__(self, key, value):
        key = self.cleaned(key)
        exact = True
        while key:
            try:
                exact0, value0 = self.table[key]
            except KeyError:
                self.table[key] = exact, value
            else:
                if exact:
                    if value != value0:
                        assert not exact0, (key, value0, value)
                    self.table[key] = True, value
                elif value != value0 and not exact0:
                    self.table[key] = False, None
            key = key[:-1]
            exact = False

    def keys(self):
        return list(self.iterkeys())

    def iterkeys(self):
        for key, (exact, value) in self.table.iteritems():
            if exact:
                yield key

    def values(self):
        return list(self.itervalues())

    def itervalues(self):
        for exact, value in self.table.itervalues():
            if exact:
                yield value

    def items(self):
        return list(self.iteritems())

    def iteritems(self):
        for key, (exact, value) in self.table.iteritems():
            if exact:
                yield key, value

    def cleaned(self, name):
        # Return an alias NAME, all cleaned.
        return name.translate(self.clean_table, '/<>-_.:()@')

# Return some descriptive text for a UNICODE point, or None.
def unicode_description(unicode, modules=[]):
    if not modules:
        import os
        if 'fr' in (os.environ.get('LANGUAGE', '')[:2],
                    os.environ.get('LANG', '')[:2]):
            import fr_charname
            modules.append(fr_charname)
        import charname
        modules.append(charname)
    for module in modules:
        compressed = module.charname.get(unicode)
        if compressed is not None:
            singles = module.number_of_singles
            fragments = []
            counter = 0
            while counter < len(compressed):
                index = ord(compressed[counter]) - 1
                counter += 1
                if index >= singles:
                    index = (singles + 255 * (index - singles)
                             + ord(compressed[counter]) - 1)
                    counter += 1
                fragments.append(module.word[index])
            return ' '.join(fragments)

# Coding registry.

class Registry:
    def __init__(self):
        try:
            import preset
        except ImportError:
            import sys
            sys.stderr.write(
                "Module `Recode.preset' has not been built yet.\n")
            self.aliases = Aliases()
            self.methods = {}
        else:
            # ALIASES yields a pair out of a cleaned out alias name,
            # first the official coding name, then the cleaned out name
            # of the implied surface name, or None if no surface is implied.
            aliases = self.aliases = Aliases()
            for key, value in preset.aliases.iteritems():
                aliases[key] = value
            # METHODS relates a (BEFORE, AFTER) pair to a recoding METHOD.
            # BEFORE and AFTER are canonical coding names.  METHOD might
            # merely cache the callable method at run-time.  Until then,
            # it is either a 2-tuple or a 3-tuple.  The first element is
            # always a string naming a module to import.  For a 2-tuple,
            # the second element is a string naming a recoding function
            # within that module.  For a 3-tuple, the second element is
            # a string naming a Step sub-class in the module; the third
            # element is True if BEFORE gets recoded into AFTER by any Step
            # instance ENCODE method, or False if by its DECODE method.
            self.methods = preset.methods
            # Finding recoding sequences requires a graph of possibilities,
            # merely described by a collection of arcs.  We compute that
            # graph here once and for all.
            self.methods_keys = preset.methods.keys()

# FIXME: The `resolve' routine is fairly slow, as shown by `recodec -lc'.
# Maybe I could just invent a kind of GenericStep able to do the same?
def resolve(given, word_list):
    # Desambiguate GIVEN, knowing it is part of a WORD_LIST.  Unless it
    # matches exactly, GIVEN should be the prefix of at most one word,
    # which is then returned whole.  Otherwise, an exception is raised.
    if given in word_list:
        return given
    candidates = [word for word in word_list if word.startswith(given)]
    if len(candidates) == 1:
        return candidates[0]
    if len(candidates) > 1:
        raise AmbiguousWordError, (given, candidates)
    raise UnknownWordError, given

# Base Step class, and Python built-in Codecs.

class Step(codecs.Codec):
    # The verbs `encode' and `decode' have a fuzzy meaning, they imply
    # some directionality between some internal or common representation
    # of a text and an external representation of the same.  With Python
    # provided codecs, the common internal representation is often Unicode,
    # so the meaning of `encode' and `decode' is usually clear within a
    # Codec instance.  In practice, we might not always use the same common
    # representation, or switch the coding of a text between two internal
    # representations, so `encode' and `decode' become rather meaningless.
    # A Step oject is essentially a Codec object in which the attributes
    # INTERNAL_CODING and EXTERNAL_CODING `encode' and `decode' really mean.
    # We `encode' the internal coding into the external coding, and we
    # `decode' the external coding into the internal coding.

    encode = None                       # masking out `codecs.Codec.encode'
    decode = None                       # masking out `codecs.Codec.decode'

class BuiltinStep(Step):
    # Python built-in Codecs are available through sub-classing this one.
    # PYTHON_ENCODING should be overridden in sub-classes with the name
    # of the Python encoding, this is a module name within the `encodings'
    # package.  ALWAYS_STRICT may be overridden for those built-in Codecs
    # which want `errors=strict' and nothing else, in which case the
    # `errors' argument to `encode' and `decode' gets ignored.

    always_strict = False

    def encode(self, input, errors='strict'):
        if self.always_strict:
            errors = 'strict'
        output = input.encode(self.external_coding, errors)
        if self.external_coding == 'quopri_codec':
            # Grrr!  `quopri_codec' recodes embedded spaces to `=20'.
            output = output.replace('=20', ' ')
            # Grrr!  `quopri_codec' does not use all allowed 76 characters.
            # Dirty patch in the test suite for now...
        return output, len(input)

    def decode(self, input, errors='strict'):
        if self.always_strict:
            errors = 'strict'
        if self.external_coding == 'base64_codec' and not input:
            # Grrr!  `base64_codec' does not accept empty input.
            return '', 0
        output = input.decode(self.external_coding, errors)
        return output, len(input)

    def unicode_mapping(self, method):
        assert method == self.decode, (method, self.decode)
        if self.external_coding == 'latin_1':
            return map(unichr, range(256))
        coding = self.external_coding
        module = getattr(__import__('encodings.' + coding), coding)
        try:
            translate = module.decoding_map
        except AttributeError:
            pass
        else:
            mapping = []
            for code in range(256):
                if translate[code] is None:
                    mapping.append(None)
                else:
                    mapping.append(unichr(translate[code]))
            return mapping

# Base Step class for generic rewriting rules.

class GenericStep(Step):
    # Through sub-classing, a generic Step receives a DATA table which
    # is a list of rewriting rules.  Each rewriting rule is a 2-tuple,
    # putting into correspondence some internal writing, given first,
    # with an external writing, given second.  Encoding "goes" from left
    # to right, decoding "goes" from right to left.  A writing is either
    # a string of one or more characters, an integer giving the ordinal
    # of a single character, or a tuple of alternative writings, in which
    # case the first is meant to be canonical: all alternative writings
    # are recognised, but only the canonical one is produced.

    # Unicode strings may be used in rewriting rules either for the internal
    # coding or the external coding, but this should be consistent with the
    # the fact that either the internal or external coding is UNICODE_STRING.

    # Recoding sequentially proceeds from the beginning of input towards its
    # end, there is no kind of attempt at global optimisation about which
    # mix of rewritings to use when there are many possible interpretations.
    # However, at a given point, the longest matching rewriting is always
    # preferred.  Single characters with ordinal between 0 and 255 are
    # also rewritten to themselves when there is no explicit rewriting
    # rule for them.

    def __init__(self):
        self.encoding_table = None
        self.decoding_table = None

    def encode(self, input, errors='strict'):
        table = self.encoding_table
        if table is None:
            table = self.encoding_table = {}
            for before, after in self.data:
                self.add_rule(before, after, table)
            self.complete_rules(self.internal_coding == UNICODE_STRING,
                                self.external_coding == UNICODE_STRING,
                                table)
        return self.process(input, errors, table)

    def decode(self, input, errors='strict'):
        table = self.decoding_table
        if table is None:
            table = self.decoding_table = {}
            for after, before in self.data:
                self.add_rule(before, after, table)
            self.complete_rules(self.external_coding == UNICODE_STRING,
                                self.internal_coding == UNICODE_STRING,
                                table)
        return self.process(input, errors, table)

    def unicode_mapping(self, method):
        if method == self.encode:
            table = self.encoding_table
        else:
            assert method == self.decode, (method, self.decode)
            table = self.decoding_table
        return [table[chr(code)][0] for code in range(256)]

    def add_rule(self, before, after, table):
        if isinstance(before, tuple):
            for element in before:
                self.add_rule(element, after, table)
            return
        if isinstance(after, tuple):
            after = after[0]
        if isinstance(before, int):
            before = chr(before)
        if isinstance(after, int):
            after = chr(after)
        for counter in range(1, len(before)):
            fragment = before[:counter]
            if fragment in table:
                table[fragment] = table[fragment][0], True
            else:
                table[fragment] = None, True
        if before in table:
            assert table[before][0] is None, (before, after, table[before][0])
            table[before] = after, True
        else:
            table[before] = after, False

    def complete_rules(self, unicode_before, unicode_after, table):
        if unicode_before:
            chr_before = unichr
        else:
            chr_before = chr
        if unicode_after:
            chr_after = unichr
        else:
            chr_after = chr
        for counter in range(256):
            character = chr_before(counter)
            if character in table:
                if table[character][0] is None:
                    table[character] = chr_after(counter), True
            else:
                table[character] = chr_after(counter), False

    def process(self, input, errors, table):
        output = []
        start = 0
        while start < len(input):
            end = start
            best_end = None
            while end < len(input):
                end += 1
                token = input[start:end]
                try:
                    fragment, more = table[token]
                except KeyError:
                    end -= 1
                    break
                else:
                    if fragment is not None:
                        best_end = end
                        best_fragment = fragment
                    if not more:
                        break
            if best_end is None:
                if errors == 'strict':
                    raise ValueError
                if errors == 'replace':
                    # FIXME: Poor choice!
                    output.append('?')
                start += 1
                continue
            output.append(best_fragment)
            start = best_end
        return ''.join(output), len(input)

# Base Step class for codings described through strips.

STRIP_SIZE = 8

class StripStep(Step):
    # A strip Step relates Unicode and a 256-character set.  Through
    # sub-classing, a strip Step receives a STRIP_POOL of many Unicode
    # characters, and a DATA table which is a list of indices into the strip
    # pool.  Each slice of STRIP_SIZE characters from the the 256-character
    # set, starting from 0 and upwards, is represented by a single index
    # in DATA.  The index itself is an offset in STRIP_POOL, and STRIP_SIZE
    # consecutive Unicode characters starting at this position in the pool
    # correspond to the characters in the slice.  Some memory savings result
    # from sharing the same strip pool for many different 256-character sets.

    internal_coding = UNICODE_STRING

    # The default value for INDICES is meant for when DATA is a sequence
    # of 256 Unicode characters in natural order.
    indices = range(0, 256, STRIP_SIZE)

    # The following tables are defaulted as base class attributes, and are
    # later overridden, as needed, by derived class attributes instead of
    # instance attributes, so they get built at most once per derived class.
    encoding_table = None
    decoding_table = None

    def encode(self, input, errors='strict'):
        table = self.encoding_table
        if table is None:
            table = {}
            data = self.data
            indices = self.indices
            for counter in range(256):
                index, offset = divmod(counter, STRIP_SIZE)
                value = data[indices[index] + offset]
                if value != NOT_A_CHARACTER:
                    table[value] = chr(counter)
            self.__class__.encoding_table = table
        output = []
        for character in input:
            if character not in table:
                if errors == 'strict':
                    raise ValueError
                if errors == 'replace':
                    output.append('?')
            else:
                output.append(table[character])
        return ''.join(output), len(input)

    def decode(self, input, errors='strict'):
        table = self.decoding_table
        if table is None:
            table = []
            data = self.data
            indices = self.indices
            for counter in range(256):
                index, offset = divmod(counter, STRIP_SIZE)
                value = data[indices[index] + offset]
                if value == NOT_A_CHARACTER:
                    table.append(None)
                else:
                    table.append(value)
            self.__class__.decoding_table = table
        output = []
        for character in input:
            value = table[ord(character)]
            if value is None:
                if errors == 'strict':
                    raise ValueError
                if errors == 'replace':
                    output.append(REPLACEMENT_CHARACTER)
            else:
                output.append(value)
        return ''.join(output), len(input)

    def unicode_mapping(self, method):
        assert method == self.decode, (method, self.decode)
        return self.decode_table

# Recodec class for all requests implying sequences of steps.

registry = Registry()

def search_function(coding):
    codec = Recodec('%s..%s' % (UNICODE_STRING, coding))
    return (codec.encode, codec.decode,
            codecs.StreamReader, codecs.StreamWriter)

codecs.register(search_function)

class Recodec(Step):
    # As many recoding requests may be unrelated to Unicode, and also
    # because some codings are only connected to Unicode through more than
    # one recoding step, a Recodec object is meant to represent zero, one or
    # more recoding steps taken as a whole.  A Recodec may be sub-classed,
    # but it usually does not need to.

    def __init__(self, request, implied=True):
        # Handle implied surfaces only if IMPLIED is True.
        self.segments = segments_from_request(request, implied)
        self.encode_methods = None
        self.decode_methods = None
        # For most requests, self.internal_coding and self.external_coding
        # just cannot represent all of what the combined recoding does, and
        # consequently, not being meaningful, they do not get initialised.

    def encode(self, text, errors='strict'):
        if self.encode_methods is None:
            self.encode_methods = methods_from_sequence(self.encoding_arcs())
        length = len(text)
        for method in self.encode_methods:
            text, _ = method(text, errors)
        return text, length

    def decode(self, text, errors='strict'):
        if self.decode_methods is None:
            self.decode_methods = methods_from_sequence(self.decoding_arcs())
        length = len(text)
        for method in self.decode_methods:
            text, _ = method(text, errors)
        return text, length

    def encoding_arcs(self):
        return sequence_from_segments(self.segments)

    def decoding_arcs(self):
        segments = [(after, before) for before, after in self.segments]
        segments.reverse()
        return sequence_from_segments(segments)

def segments_from_request(request, implied):
    # Return list of segments for representing REQUEST.  Each segment
    # is a (BEFORE, AFTER) pair, where BEFORE and AFTER are each either
    # canonical coding name, or a sequence of such in fallback order.
    # Handle implied surfaces if IMPLIED is True.
    segments = []
    for segment in request.split(','):
        chains = segment.split('..')
        if len(chains) == 1:
            chains.append('')
        before = chains[0]
        for after in chains[1:]:
            befores = before.split('/')
            if len(befores) == 1:
                coding, surface = registry.aliases[befores[0] or IMPLIED_ALIAS]
                if implied and surface is not None:
                    befores.append(surface)
            afters = after.split('/')
            if len(afters) == 1:
                coding, surface = registry.aliases[afters[0] or IMPLIED_ALIAS]
                if implied and surface is not None:
                    afters.append(surface)
            befores.reverse()
            for surface in befores[:-1]:
                if surface:
                    segments.append((registry.aliases[surface][0],
                                     TRIVIAL_SURFACE))
            segments.append((registry.aliases[befores[-1] or IMPLIED_ALIAS][0],
                             registry.aliases[afters[0] or IMPLIED_ALIAS][0]))
            for surface in afters[1:]:
                if surface:
                    segments.append((TRIVIAL_SURFACE,
                                     registry.aliases[surface][0]))
            before = after
    return segments

def sequence_from_segments(segments):
    # Return a tree of arcs for representing all request SEGMENTS.
    # ARCS describe the graph of all possible elementary recodings.
    # The tree is a sequence of either @@@
    sequence = []
    for before, after in segments:
        if before == after:
            subsequence = []
        elif (before, after) in registry.methods:
            subsequence = [(before, after)]
        elif ((before, UNICODE_STRING) in registry.methods
              and (UNICODE_STRING, after) in registry.methods):
            subsequence = [(before, UNICODE_STRING), (UNICODE_STRING, after)]
        else:
            # Optimisation of some usual cases failed.  Try the hard way!
            import graph
            subsequence = graph.path(before, after, registry.methods_keys)
            if subsequence is None:
                raise UnresolvedRecodecError, (before, after)
        sequence += subsequence
    return sequence

def methods_from_sequence(sequence):
    # Return a list of methods from a SEQUENCE of arcs.
    # While doing so, import modules and cache methods.
    methods = []
    for arc in sequence:
        method = registry.methods[arc]
        if isinstance(method, tuple):
            if len(method) == 2:
                module_name, function_name = method
                module = getattr(__import__('Recode.' + module_name),
                                 module_name)
                method = getattr(module, function_name)
            else:
                module_name, codec_name, use_encode = method
                module = getattr(__import__('Recode.' + module_name),
                                 module_name)
                codec = getattr(module, codec_name)()
                if use_encode:
                    method = codec.encode
                else:
                    method = codec.decode
            registry.methods[arc] = method
        methods.append(method)
    return methods
