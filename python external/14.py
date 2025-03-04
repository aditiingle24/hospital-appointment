import re
text="aditi@gmail.com"
p=r"(\w+)@(\w+).(\w+)"
matches=re.finditer(p,text)
for match in matches:
    print("grp1",match.group(1))
    print("grp2",match.group(2))
    print("grp3",match.group(3))