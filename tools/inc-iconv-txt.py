# -*- coding: UTF-8 -*-
from Recode import libiconv
import common

def main(*arguments):
    import re
    assert not arguments, arguments
    margin = '  '
    write = common.Output('inc-iconv.txt', 'ReST', margin=margin).write
    for data in libiconv.iconv_data:
        comment = data[0]
        write('\n'
              '%s+ *%s*\n'
              % (margin, comment))
        for group in data[1:]:
            charset = group[0]
            aliases = group[1:]
            write('\n'
                  '%s  :charset:`%s`\n'
                  % (margin, charset))
            if aliases:
                write('%s    .. :tindex %s, aliases\n'
                      % (margin, re.sub(':([0-9]+)', r'(\1)', charset)))
                for alias in aliases:
                    write('%s    .. :tindex %s\n'
                          % (margin, re.sub(':([0-9]+)', r'(\1)', alias)))
                write('\n')
                if len(aliases) == 1:
                    write('%s    :charset:`%s` is an alias for this charset.\n'
                          % (margin, aliases[0]))
                else:
                    write('%s    :charset:`%s` and :charset:`%s` are aliases'
                          ' for this charset.\n'
                          % (margin, '`, :charset:`'.join(aliases[:-1]),
                             aliases[-1]))
            else:
                write('%s    .. :tindex %s\n'
                       % (margin, re.sub(':([0-9]+)', r'(\1)', charset)))

if __name__ == '__main__':
    import sys
    main(*sys.argv[1:])
