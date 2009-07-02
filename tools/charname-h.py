def main(*arguments):
    import getopt
    options, arguments = getopt.getopt(arguments, 'F')
    french = False
    for option, value in options:
        if option == '-F':
            french = True
    assert not arguments, arguments
    import common
    if french:
        from Recode import fr_charname as charname
        write = common.Output('charname.h', 'C').write
    else:
        from Recode import charname
        write = common.Output('fr-charname.h', 'C').write
    write('\n')
    write('#define NUMBER_OF_SINGLES %d\n' % charname.number_of_singles)
    write('#define MAX_CHARNAME_LENGTH %d\n' % charname.max_charname_length)
    write('#define NUMBER_OF_CHARNAMES %d\n' % charname.number_of_charnames)
    write('\n'
          'static const char *const word[%d] =\n'
          '  {\n'
          % len(charname.word))
    char1 = 0
    char2 = 255
    for word in charname.word:
        if char1 < charname.number_of_singles:
            char1 += 1
            write('    %-28s/* \\%0.3o */\n'
                  % ('"%s",' % word.replace('"', r'\"'), char1))
        else:
            if char2 == 255:
                char1 += 1
                char2 = 1
            else:
                char2 += 1
            write('    %-28s/* \\%0.3o\\%0.3o */\n'
                  % ('"%s",' % word.replace('"', r'\"', 1), char1, char2))
    write('  };\n'
          '\n'
          'struct charname\n'
          '  {\n'
          '    recode_ucs2 code;\n'
          '    const char *crypted;\n'
          '  };\n'
          '\n'
          'static const struct charname charname[NUMBER_OF_CHARNAMES]'
          ' =\n'
          '  {\n')
    charnames = charname.charname.items()
    charnames.sort()
    for unicode, characters in charnames:
        write('    {0x%04X, "' % unicode)
        for character in characters:
            write('\\%0.3o' % ord(character))
        write('"},\n')
    write('  };\n')

if __name__ == '__main__':
    import sys
    main(*sys.argv[1:])
