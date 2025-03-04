import re
p=r"[a-zA-Z]+ \d+"
matches=re.findall(p,"LXI 20188,aditi,NHGFD 98765")
for match in matches:
    print(match,end=" ")