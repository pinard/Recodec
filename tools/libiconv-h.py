# -*- coding: UTF-8 -*-
from Recode import libiconv
import common

def main(*arguments):
    assert not arguments, arguments
    write = common.Output('libiconv.h', 'C').write
    # There is a supplementary NULL at the far end.
    count = 1
    for data in libiconv.iconv_data:
        # The comment is included, but this will count for the needed NULL.
        count += len(data)
    write('\n'
          "/* This is derived from Bruno Haible's `libiconv' package.  */\n"
          '\n'
          'static const char *iconv_name_list[%d] =\n'
          '  {\n'
          % count)
    for data in libiconv.iconv_data:
        comment = data[0]
        write('\n'
              '    /* %s */\n'
              '\n'
              % comment)
        for group in data[1:]:
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
