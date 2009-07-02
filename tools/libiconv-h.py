from Recode import libiconv
import common

def main(*arguments):
    assert not arguments, arguments
    write = common.Output('libiconv.h', 'C').write
    count = len(libiconv.iconv_name_list) + 1 # NULLs
    for group in libiconv.iconv_name_list:
        count += len(group)
    write('\n'
          "/* This is derived from Bruno Haible's `libiconv' package.  */\n"
          '\n'
          'static const char *iconv_name_list[%d] =\n'
          '  {\n'
          % count)
    for group in libiconv.iconv_name_list:
        if len(group) == 1:
            write('    "%s", NULL,\n' % group[0])
        else:
            write('    "%s",\n' % group[0])
            for alias in group[1:-1]:
                write('\t"%s",\n' % alias)
            write('\t"%s", NULL,\n' % group[-1])
    write('    NULL\n'
          '  };\n')

if __name__ == '__main__':
    import sys
    main(*sys.argv[1:])
