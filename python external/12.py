import re
p=r"[a-zA-Z]+ \d+"
matches=re.finditer(p,"NBV 76645,aditi , 9876, HYRFV 8764")
for match in matches:
    print("starting index",match.start())
    print("ending index",match.end())
    print("span index",match.span())