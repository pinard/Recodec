import common

# FIXME!!!

class Tests(common.Test):

    def many_tests(setup, before, after, method, variant):
        pass

#    if variant == 'filter':
#        [recode --quiet --force --sequence=method < copying before..after \
#         | recode --quiet --force --sequence=method after..before > data]
#    elif variant == 'squash':
#        [cp copying data
#         chmod +w data
#         recode --quiet --force --sequence=method before..after data
#         recode --quiet --force --sequence=method after..before data])
#        diff copying data
#
#copying = file('$at_top_srcdir/COPYING').read()
#
#for before, after in (('texte', 'texte'),
#                      ('texte', 'latin1'),
#                      ('texte', 'bangbang'),
#                      ('texte', 'ibmpc'),
#                      ('texte', 'iconqnx'),
#                      ('ascii-bs', 'ebcdic')):
#    for method in 'memory', 'files', 'pipe':
#        for variant in 'filter', 'squash':
#            many_tests(("%s:%s through %s while %sing"
#                        % (before, after, method, variant)),
#                        before, after, method, variant)

if __name__ == '__main__':
    import unittest
    unittest.main()
