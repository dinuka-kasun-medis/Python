import re

s = 'abccba'
ss = 'facebookgooglemsmsgooglefacebook'
p = 'xyzzyx'

def match(s, p):
    nr = {}
    regex = []
    for c in p:
        if c not in nr:
            regex.append('(.+)')
            nr[c] = len(nr) + 1
        else:
            regex.append('\\%d' % nr[c])
    return bool(re.match(''.join(regex) + '$', s))

print(match(s, p))
print(match(ss, p))