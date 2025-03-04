#findall 
import re
p=r"[a-zA-Z]+ \d+"
matches=re.findall(p,"LXI 2013,VSI 20104,VDI 2015,aditi")
for match in matches:
    print(match,end=" ")