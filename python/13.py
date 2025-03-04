#phone number
import re
text="123-456-7890, 345-678-9012, 567-890-1234"
p=r"\d{3}-\d{3}-\d{4}"
matches=re.finditer(p,text)
for match in matches:
    print("match of group:",match.group())
    print("start:",match.start())
    print("end",match.end())
    print("span:",match.span())