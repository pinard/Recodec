# -*- coding: UTF-8 -*-
import os, time
from Recode import version
import common

def main(*arguments):
    mtime = None
    for file in arguments:
        value = os.path.getmtime(file)
        if mtime is None or value > mtime:
            mtime = value
    common.Output('inc-stamp.txt', 'ReST').write(
        '\n'
        '.. |package| replace:: %s\n'
        '.. |version| replace:: %s\n'
        '.. |date| replace:: %s\n'
        % (version.package, version.version,
           time.strftime('%Y-%m-%d', time.localtime(mtime))))

if __name__ == '__main__':
    import sys
    main(*sys.argv[1:])
