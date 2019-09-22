import keyword
s = 'for'
s1 = 'joker'
s2 = 'True'

if keyword.iskeyword(s):
    print('it is keyword')
else:
    print('its not a keyword')
if keyword.iskeyword(s1):
    print('its keyword')
else:
    print('why so serious')
if keyword.iskeyword(s2):
    print('its keyword')
else:
    print('not a keyword')

# How to print keywordlist
import  keyword
print('the list of keyword')
print(keyword.kwlist)