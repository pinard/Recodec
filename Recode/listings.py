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
    write('%s\n' % recode.registry.unalias(charset)[0])
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
          % recode.registry.unalias(charset)[0])
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
    codec.encode('')
    if len(codec.encode_sequence) == 0:
        return map(unichr, range(256))
    if len(codec.encode_sequence) == 1:
        method = recode.registry.methods[codec.encode_sequence[0]]
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
        if coding in codings and alias != recode.clean_alias(coding):
            codings[coding].append((alias, surface))
    # Produce the synthetic report.
    items = [(recode.clean_alias(coding), coding, aliases)
             for (coding, aliases) in codings.iteritems()]
    items.sort()
    for key, coding, aliases in items:
        if spaces[coding] == 'surface':
            write('/')
        write(coding)
        surface = recode.registry.aliases[recode.clean_alias(coding)][1]
        if surface is not None:
            write('/' + recode.registry.unalias(surface)[0])
        aliases.sort()
        for alias, surface in aliases:
            write(' ')
            write(alias)
            if surface is not None:
                write('/' + recode.registry.unalias(surface)[0])
        write('\n')

# This is a diagnostic tool.  Report all charsets which are a subset of
# another, or are identical.  Return true only if there are no such subsets.
def find_and_report_subsets():
    pass
#   bool success = true;
#   RECODE_SYMBOL charset1;
#
#   for (charset1 = outer->symbol_list;
#        charset1;
#        charset1 = charset1->next)
#     {
#       const struct strip_data *table1 = charset1->data;
#       RECODE_SYMBOL charset2;
#
#       if (charset1->ignore || charset1->data_type != RECODE_STRIP_DATA)
#	continue;
#
#       for (charset2 = outer->symbol_list;
#	   charset2;
#	   charset2 = charset2->next)
#	{
#	  const struct strip_data *table2 = charset2->data;
#
#	  if (charset2->ignore || charset2->data_type != RECODE_STRIP_DATA
#	      || charset2 == charset1)
#	    continue;
#
#	  {
#	    bool subset = true;
#	    unsigned distance = 0;
#	    unsigned counter;
#	    unsigned slider;
#
#	    for (counter = 0; counter < 256/STRIP_SIZE; counter++)
#	      {
#		const recode_ucs2 *pool1 = table1->pool;
#		const recode_ucs2 *pool2 = table2->pool;
#		const short offset1 = table1->offset[counter];
#		const short offset2 = table2->offset[counter];
#
#		if (pool1 != pool2 || offset1 != offset2)
#		  for (slider = 0; slider < STRIP_SIZE; slider++)
#		    {
#		      recode_ucs2 value1 = pool1[offset1 + slider];
#		      recode_ucs2 value2 = pool2[offset2 + slider];
#
#		      if (value1 != value2)
#			{
#			  if (value1 == MASK (16))
#			    distance++;
#			  else
#			    {
#			      subset = false;
#			      break;
#			    }
#			}
#		    }
#		if (!subset)
#		  break;
#	      }
#
#	    if (subset)
#	      {
#		if (distance == 0)
#		  printf ("[  0] %s == %s\n",
#			  charset1->name, charset2->name);
#		else
#		  printf ("[%3d] %s < %s\n", distance,
#			  charset1->name, charset2->name);
#
#		success = false;
#	      }
#	  }
#	}
#     }

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
