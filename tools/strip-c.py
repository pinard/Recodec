from Recode import recode, listings
import common

class Main:

    def main(self, *arguments):
	assert not arguments, arguments
	# Rewrite strip data, merging common strips as we go.
	self.strips = []
	self.strip_index = {}
	self.add_strip(u'\uFFFF' * recode.STRIP_SIZE)
	strip_data = []
	for charset, data, indices in common.all_strip_data():
	    strip_data.append(
		(recode.cleaned_alias(charset), charset,
		 [self.add_strip(data[index:index+recode.STRIP_SIZE])
		  for index in indices]))
	# Write the strip pool.
	write = common.Output('strip.c', 'C').write
	write('\n'
	      '#include \"common.h\"\n'
	      '\n'
	      'const recode_ucs2 ucs2_data_pool[%d] =\n'
	      '  {'
	      % (len(self.strips) * recode.STRIP_SIZE))
	count = 0
	for strip in self.strips:
	    for character in strip:
		if count % 8 == 0:
		    if count != 0:
			write(',')
		    write('\n    /* %4d */ ' % count)
		else:
		    write(', ')
		write('0x%0.4X' % ord(character))
		count += 1
	write('\n'
	      '  };\n')
	# Write out all strip codecs.
	strip_data.sort()
	ordinal = 0
	for key, charset, indices in strip_data:
	    write('\n'
		  '/* %s */\n'
		  '\n'
		  'static struct strip_data data_%d =\n'
		  '  {\n'
		  '    ucs2_data_pool,\n'
		  '    {\n'
		  % (charset, ordinal))
	    count = 0
	    for indice in indices:
		if count % 12 == 0:
		    if count != 0:
			write(',\n')
		    write('      ')
		else:
		    write(', ')
		write('%4d' % indice)
		count += 1
	    write('\n'
		  '    }\n'
		  '  };\n')
	    ordinal += 1
	# Print the collectable initialisation function.
	write('\n'
	      'bool\n'
	      'module_strips (struct recode_outer *outer)\n'
	      '{\n'
	      '  RECODE_ALIAS alias;\n')
	charsets = {}
	for key, charset, indices in strip_data:
	    charsets[charset] = []
	for alias, (charset, surface) in recode.registry.aliases.iteritems():
	    if charset in charsets:
		charsets[charset].append((alias, surface))
	ordinal = 0
	for key, charset, indices in strip_data:
            write('\n'
                  '  if (!declare_strip_data (outer, &data_%d, "%s"))\n'
		  '    return false;\n'
		  % (ordinal, charset))
	    for alias, surface in charsets[charset]:
		if surface is None:
		    write('  if (!declare_alias (outer, "%s", "%s"))\n'
			  '    return false;\n'
			  % (alias, charset))
		else:
		    write('  if (alias = declare_alias (outer, "%s", "%s"),'
			  ' !alias)\n'
			  '    return false;\n'
			  % (alias, charset))
		    write('  if (!declare_implied_surface (outer, alias,'
			  ' outer->%s_surface))\n'
			  '    return false;\n'
			  % surface)
	    ordinal += 1
	write('\n'
	      '  return true;\n'
	      '}\n')
	#write('\n'
	#      'void\n'
	#      'delmodule_strips (struct recode_outer *outer)\n'
	#      '{\n'
	#      '}\n')

    def add_strip(self, strip):
	# Retrieve an existing strip, or create one as necessary.
	try:
	    index = self.strip_index[strip]
	except KeyError:
	    index = len(self.strips) * recode.STRIP_SIZE
	    self.strips.append(strip)
	    self.strip_index[strip] = index
	return index

main = Main().main

if __name__ == '__main__':
    import sys
    main(*sys.argv[1:])
