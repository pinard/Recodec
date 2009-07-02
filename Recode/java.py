import recode

# See `http://www.ugrad.cs.ubc.ca/~cs411/docs/modified/3.doc.html',
# and also `http://www.webreference.com/js/column25/unicode.html'.

# FIXME: Python implements a Unicode-escape a bit far from the Java
# specification.  So, we append `-X' for now.
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
            count, code = self.study_escape(input, end + 2)
            output.append(self.encode_helper(input[start:end], errors))
            output.append('\\uu%s%0.4X' % ('u' * count, code))
            start = end + count + 5
            end = input.find('\\u', start)
        output.append(self.encode_helper(input[start:], errors))
        return ''.join(output), len(input)

    def encode_helper(self, input, errors):
        output = []
        for character in input:
            code = ord(character)
            if code < 128:
                output.append(chr(code))
            else:
                output.append('\\u%0.4X' % code)
        return ''.join(output)

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
            count, code = self.study_escape(input, end + 2)
            output.append(self.encode_helper(input[start:end], errors))
            if count == 0:
                output.append(unichr(code))
            else:
                output.append('\\%s%0.4X' % ('u' * count, code))
            start = end + count + 6
            end = input.find('\\u', start)
        output.append(self.decode_helper(input[start:], errors))
        return ''.join(output), len(input)

    def decode_helper(self, input, errors):
        output = []
        for character in input:
            code = ord(character)
            if code < 128:
                output.append(unichr(code))
            else:
                raise ValueError
        return ''.join(output)

    def study_escape(self, input, start):
        count = 0
        while start < len(input) and input[start] == 'u':
            count += 1
            start += 1
        if start+4 > len(input):
            raise ValueError
        return count, int(input[start:start+4], 16)
