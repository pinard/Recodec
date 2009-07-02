from Recode import rfc1345
import common

def main(*arguments):
    assert not arguments, arguments
    write = common.Output('rfc1345.h', 'C').write
    inverse_map = {}
    write('\n')
    write('#define TABLE_LENGTH %d\n' % len(rfc1345.table))
    write('#define MAX_MNEMONIC_LENGTH %d\n' % rfc1345.max_mnemonic_length)
    write('\n'
          'struct entry\n'
          '  {\n'
          '    recode_ucs2 code;\n'
          '    const char *rfc1345;\n'
          '  };\n'
          '\n'
          'static const struct entry table[TABLE_LENGTH] =\n'
          '  {\n')
    items = rfc1345.table.items()
    items.sort()
    count = 0
    import re
    for unicode, mnemonic in items:
        write('    /* %4d */ {0x%04X, "%s"},\n'
              % (count, unicode, re.sub(r'([\"])', r'\\\1', mnemonic)))
        inverse_map[mnemonic] = count
        count += 1
    write('  };\n'
          '\n'
          'static const unsigned short inverse[TABLE_LENGTH] =\n'
          '  {')
    count = 0
    items = inverse_map.items()
    items.sort()
    for mnemonic, unicode in items:
        if count % 10 == 0:
            if count != 0:
                write(',')
            write('\n    /* %4d */ ' % count)
        else:
            write(', ')
        write('%4d' % unicode)
        count += 1
    write('\n'
          '  };\n')

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
