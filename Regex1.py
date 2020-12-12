import re
from string import ascii_letters
import string

print('Enter your @mail: ')
mytext = input();

s = []
s.append(mytext)

pat = '^[a-zA-Z{}]+$'.format(re.escape(string.punctuation))
k = bool(re.match(pat, mytext))
if (k == True):
	print('Right form!')
# if (k == False):
	# s.pop()
print('mytext')	
print(s)

print('\n')

lookinFor = r"@ukr.net"

resaults = re.findall(lookinFor, mytext)
print(resaults)

if resaults == "@ukr.net":
	print('Access Allowed!')
else:
	print("But not right mail! Access Denied!")