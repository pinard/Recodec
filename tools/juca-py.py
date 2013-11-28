# -*- coding: utf-8 -*-
import os, sys

def main(*arguments):
    assert len(arguments) == 1, arguments
    infos = read_infos(arguments[0])
    produce_translit(infos, sys.stdout.write)

def produce_translit(infos, write):
    write('import recode\n'
          '\n'
          'declares = [(\'BPI-JUCA-Translit\', \'tjuca\')]\n'
          '\n'
          'class JucaTranslit(recode.GenericStep):\n'
          '    internal_coding = recode.UNICODE_STRING\n'
          '    external_coding = \'BPI-JUCA-Translit\'\n'
          '    data = [\n')
    pairs = [(info.ucs, info.kbd) for info in infos
             if (info.ucs is not None and info.kbd is not None
                 and info.ucs != info.kbd)]
    pairs.sort()
    for ucs, kbd in pairs:
        sys.stdout.write('        (%r, %r),\n' % (ucs, kbd))
    write('        ]\n')

def read_infos(file_name):
    infos = []
    names = ['ucs', 'cm', 'ec', 'fc', 'j', 'texinfo', 'kbd',
             'ty', 'ln', 'mm', 'base', 'tri', 'f']
    for line in file(file_name):
        # Skip comments.
        if line[0] in '#\n':
            continue
        # Split line into a Info object.
        fields = line.replace('#?', '# ?').split('# ', 1)
        assert len(fields) == 2, line
        description = fields[1][:-1]
        text = fields[0].replace(' }', '\0}').replace(' >', '\0>')
        values = [value.replace('\0', ' ') for value in text.split()]
        assert len(values) == 13, line
        info = Info(names, values)
        # Adjust ucs.
        if info.ucs == '-':
            info.ucs = None
        else:
            info.ucs = ''.join([unichr(int(text.replace('U', ''), 16))
                                for text in info.ucs.split('+')])
        # Adjust cm.
        if info.cm == '-':
            info.cm = None
        # Adjust ec.
        if info.ec == '-':
            info.ec = None
        # Adjust fc.
        if info.fc == '-':
            info.fc = None
        # Adjust j.
        if info.j == '-':
            info.j = None
        # Adjust texinfo.
        if info.texinfo == '-':
            info.texinfo = None
        # Adjust kbd.
        if info.kbd == '-':
            info.kbd = None
        else:
            assert info.kbd.startswith('<'), info.kbd
            assert info.kbd.endswith('>'), info.kbd
            info.kbd = info.kbd[1:-1].replace('\\\\', '\\')
        # Adjust ty.
        if info.ty == '-':
            info.ty = None
        # Adjust ln.
        if info.ln == '-':
            info.ln = None
        # Adjust mm.
        if info.mm == '-':
            info.mm = None
        # Adjust base.
        if info.base == '-':
            info.base = None
        # Adjust tri.
        if info.tri == '-':
            info.tri = None
        # Adjust f.
        if info.f == '-':
            info.f = None
        # Adjust description.
        info.description = description
        # Save result.
        infos.append(info)
    return infos

class Info:
    def __init__(self, names, values):
        self.__dict__.update(dict(zip(names, values)))

if __name__ == '__main__':
    main(*sys.argv[1:])
