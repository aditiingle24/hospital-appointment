#finditer
import re
p=r"[a-zA-z]+ \d+"
matches=re.finditer(p,"ADITI 234,KUYVF 75432,BNTJM 388,aditi")
for match in matches:
    print("match found at start index is:",match.start())
    print("match found at end index is:",match.end())
    print("match found at starting and ending index is:",match.span())