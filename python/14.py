#extract email
import re
text="aditi@gmail.com"
p=r"(\w+)@(\w+).(\w+)"
match=re.search(p,text)
if match:
    print("username:",match.group(1))
    print("mail:",match.group(2))
    print("extension:",match.group(3))