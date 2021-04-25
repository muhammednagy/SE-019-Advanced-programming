import re
import sys


if len(sys.argv) < 3:
    print("email.script requires 2 paramters emails file and new emails file")
    exit(500)


txt = open(sys.argv[1], 'r').read()
newfile = open(sys.argv[2], "w")
regx = r'''(
<
[a-zA-Z0-9._%+-]+      # username
@                      # @ symbol
[a-zA-Z0-9.-]+         # domain name
(\.[a-zA-Z]{2,4})       # dot-something
>
)'''
x = re.findall(regx, txt, flags=re.DOTALL | re.MULTILINE | re.VERBOSE)

emailsList = set()
for i in x:
    emailsList.add(i[0].replace('<', '').replace('>', ''))

emails = ('\n'.join(map(str, emailsList)))
newfile.write(emails)
newfile.close()