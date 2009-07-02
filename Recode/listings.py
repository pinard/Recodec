import sys
import recode

# Print a concise, tabular CHARSET description presented according to BASE.
def list_concise_charset(charset, base, write=sys.stdout.write):
    table = unicode_mapping(charset)
    format = {8: '%0.3o', 10: '%3d', 16: '%0.2x'}[base] + ' %-3s'
    blanks = ' ' * ({8: 3, 10: 3, 16: 2}[base] + 4)
    dots = '.' * len(blanks)
    empty_half = [None] * 128
    import rfc1345
    write('%s\n' % recode.registry.aliases[charset][0])
    for half in range(0, 256, 128):
        if table[half:half+128] != empty_half:
            write('\n')
            for line in range(16):
                fragments = []
                for counter in range(half+line, half+line+128, 16):
                    translation = table[counter]
                    if translation is None:
                        fragments.append(blanks)
                    elif len(translation) == 1:
                        unicode = translation[0]
                        fragments.append(format % (
                            ord(unicode), rfc1345.table.get(ord(unicode), '')))
                    else:
                        # Multi-character.
                        fragments.append(dots)
                write('  '.join(fragments).rstrip() + '\n')

# Print a full CHARSET description.
def list_full_charset(charset, write=sys.stdout.write):
    table = unicode_mapping(charset)
    import rfc1345
    write("Dec  Oct Hex   UCS2  Mne  %s\n"
          % recode.registry.aliases[charset][0])
    insert_white = True
    for code in range(256):
        text = table[code]
        if text is None:
            insert_white = True
        else:
            if insert_white:
                write('\n')
                insert_white = False
            for character in text:
                unicode = ord(character)
                if code is None:
                    write(' +    +   + ')
                else:
                    write('%3d  %.3o  %.2x' % (code, code, code))
                write('   %.4X' % unicode)
                fragments = ['  %-3s' % rfc1345.table.get(unicode, '')]
                description = recode.unicode_description(unicode)
                if description is not None:
                    fragments.append(description)
                write('  '.join(fragments).rstrip() + '\n')
                code = None

# Discover some Unicode mapping for given CHARSET.
def unicode_mapping(charset):
    codec = recode.Recodec(
        '%s..%s' % (charset, recode.UNICODE_STRING), implied=False)
    codec.encode('')                    # force full initialisation
    if len(codec.encode_methods) == 0:
        return map(unichr, range(256))
    if len(codec.encode_methods) == 1:
        method = codec.encode_methods[0]
        mapping = method.im_self.unicode_mapping(method)
        if mapping is not None:
            return mapping
    raise recode.ComplexRecodecError, (charset, recode.UNICODE_STRING)

# List all available symbols.
# FIXME: Obey restrictions for an AFTER charset if any.
def list_all_codings(write=sys.stdout.write):
    spaces = {recode.TRIVIAL_SURFACE: 'surface'}
    codings = {recode.TRIVIAL_SURFACE: []}
    # Find official coding names from recoding methods.
    for before, after in recode.registry.methods:
        if before == recode.TRIVIAL_SURFACE:
            spaces[after] = 'surface'
            if after not in codings:
                codings[after] = []
        elif after == recode.TRIVIAL_SURFACE:
            spaces[before] = 'surface'
            if before not in codings:
                codings[before] = []
        else:
            if before not in codings:
                spaces[before] = 'charset'
                codings[before] = []
            if after not in codings:
                spaces[after] = 'charset'
                codings[after] = []
    # Tie various aliases with their official name.
    for alias, (coding, surface) in recode.registry.aliases.iteritems():
        if coding in codings:
            codings[coding].append((alias, surface))
    # Produce the synthetic report.
    items = [(recode.cleaned_alias(coding), coding, aliases)
             for (coding, aliases) in codings.iteritems()]
    items.sort()
    for key, coding, aliases in items:
        # Write the coding official name and surface.
        if spaces[coding] == 'surface':
            write('/')
        write(coding)
        handy_alias = recode.cleaned_alias(coding)
        surface = recode.registry.aliases[handy_alias][1]
        if surface is not None:
            write('/' + recode.registry.aliases[surface][0])
        # Write all available aliases.
        aliases.sort()
        for alias, surface in aliases:
            if alias != recode.cleaned_alias(coding):
                write(' ')
                write(alias)
                if surface is not None:
                    write('/' + recode.registry.aliases[surface][0])
            while alias:
                if len(alias) < len(handy_alias):
                    handy_alias = alias
                elif len(alias) == len(handy_alias) and alias < coding:
                    handy_alias = alias
                alias = alias[:-1]
                if not alias:
                    break
                try:
                    check, _ = recode.registry.aliases[alias]
                except recode.AmbiguousWordError:
                    break
                if check != coding:
                    break
        # Write the shortest acceptable writing of an alias.
        write(' [%s]\n' % handy_alias)

# /* Charset contents.  */
#
# /*-----------------------------------------------------------------.
# | Decode a known PAIRS argument, given in STRING, constructing the |
# | pair_restriction array out of it.                                |
# `-----------------------------------------------------------------*/
#
# bool
# decode_known_pairs (RECODE_OUTER outer, const char *string)
# {
#   const char *cursor;
#   char *after;
#   int left_value;
#   int right_value;
#   int *pointer;
#
#   if (!ALLOC (outer->pair_restriction, 16, struct recode_known_pair))
#     return false;
#
#   left_value = -1;
#   right_value = -1;
#   pointer = &left_value;
#
#   cursor = string;
#   while (*cursor)
#     switch (*cursor)
#       {
#       default:
#	return false;
#
#       case '0':
#       case '1':
#       case '2':
#       case '3':
#       case '4':
#       case '5':
#       case '6':
#       case '7':
#       case '8':
#       case '9':
#	*pointer = strtoul (cursor, &after, 0);
#	cursor = after;
#	if (*pointer > 255)
#	  return false;
#	break;
#
#       case ':':
#	cursor++;
#	if (left_value < 0 || pointer != &left_value)
#	  return false;
#	pointer = &right_value;
#	break;
#
#       case ',':
#	cursor++;
#	if (left_value < 0 || right_value < 0)
#	  return false;
#
#	outer->pair_restriction[outer->pair_restrictions].left
#	  = (unsigned char) left_value;
#	outer->pair_restriction[outer->pair_restrictions].right
#	  = (unsigned char) right_value;
#	outer->pair_restrictions++;
#
#	if (outer->pair_restrictions % 16 == 0)
#	  if (!REALLOC (outer->pair_restriction,
#			outer->pair_restrictions + 16,
#			struct recode_known_pair))
#	    return false;
#
#	left_value = -1;
#	right_value = -1;
#	pointer = &left_value;
#	break;
#       }
#
#   if (left_value < 0 || right_value < 0)
#     return false;
#
#   outer->pair_restriction[outer->pair_restrictions].left
#     = (unsigned char) left_value;
#   outer->pair_restriction[outer->pair_restrictions].right
#     = (unsigned char) right_value;
#   outer->pair_restrictions++;
#
#   return true;
# }
