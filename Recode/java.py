# -*- coding: utf-8 -*-
import recode

# See http://www.ugrad.cs.ubc.ca/~cs411/docs/modified/3.doc.html for Java,
# http://www.webreference.com/js/column25/unicode.html for Javascript,
# http://java.sun.com/products/jdk/1.1/docs/tooldocs/solaris/native2ascii.html
# for a converter program.

# FIXME: Python implements a Unicode-escape a bit far from the Java
# specification.  So, we append `-X' for now.

# FIXME: This does not satisfactorily handle coding errors.

declares = [('Unicode-Escape-X', 'ue', 'Java')]

class Java(recode.Step):
    internal_coding = recode.UNICODE_STRING
    external_coding = 'Unicode-Escape-X'

    def encode(self, input, errors='strict'):
        output = []
        start = 0
        end = input.find('\\u', start)
        while end >= 0:
            index = end
            while index > start and input[index-1] == '\\':
                index -= 1
            if (end-index) % 2 != 0:
                end = input.find('\\u', end + 2)
                continue
            count, code = study_escape(input, end + 2)
            output.append(encode_helper(input[start:end], errors))
            output.append('\\uu%s%0.4X' % ('u' * count, code))
            start = end + count + 6
            end = input.find('\\u', start)
        output.append(encode_helper(input[start:], errors))
        return ''.join(output), len(input)

    def decode(self, input, errors='strict'):
        output = []
        start = 0
        end = input.find('\\u', start)
        while end >= 0:
            index = end
            while index > start and input[index-1] == '\\':
                index -= 1
            if (end-index) % 2 != 0:
                end = input.find('\\u', end + 2)
                continue
            count, code = study_escape(input, end + 2)
            output.append(decode_helper(input[start:end], errors))
            if count == 0:
                output.append(unichr(code))
            else:
                output.append('\\%s%0.4X' % ('u' * count, code))
            start = end + count + 6
            end = input.find('\\u', start)
        output.append(decode_helper(input[start:], errors))
        return ''.join(output), len(input)

def encode_helper(input, errors):
    output = []
    for character in input:
        code = ord(character)
        if code < 128:
            output.append(chr(code))
        else:
            output.append('\\u%0.4X' % code)
    return ''.join(output)

def decode_helper(input, errors):
    output = []
    for character in input:
        code = ord(character)
        if code < 128:
            output.append(unichr(code))
        else:
            raise ValueError
    return ''.join(output)

def study_escape(input, start):
    index = start
    while index < len(input) and input[index] == 'u':
        index += 1
    if index+4 > len(input):
        raise ValueError
    return index-start, int(input[index:index+4], 16)
