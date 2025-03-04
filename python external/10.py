import re
s="she sells sea shells at the sea shore"
p="sea"
rp="ocean"
new=re.sub(p,rp,s,2)
print(new)