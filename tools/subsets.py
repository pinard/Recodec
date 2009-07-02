"""\
Report all charsets which are a subset of another, or are identical.
Only strip-described charsets are handled.
"""

import sys
from Recode import recode, listings
import common

def main(*arguments):
    assert not arguments, arguments
    strip_data = list(common.all_strip_data())
    results = []
    for charset1, data1, indices1 in strip_data:
        for charset2, data2, indices2 in strip_data:
            if charset1 == charset2:
                continue
            distance = 0
            subset = True
            for index1, index2 in zip(indices1, indices2):
                if data1 != data2 or index1 != index2:
                    for character1, character2 in zip(
                        data1[index1:index1+recode.STRIP_SIZE],
                        data2[index2:index2+recode.STRIP_SIZE]
                        ):
                        if character1 != character2:
                            if character1 == recode.NOT_A_CHARACTER:
                                distance += 1
                            else:
                                subset = False
                                break
                    if not subset:
                        break
            else:
                results.append((distance, charset1, charset2))
    results.sort()
    write = sys.stdout.write
    for distance, charset1, charset2 in results:
        if distance == 0:
            write('[  0] %s == %s\n' % (charset1, charset2))
        else:
            write('[%3d] %s < %s\n' % (distance, charset1, charset2))

if __name__ == '__main__':
    main(*sys.argv[1:])
