#replace one pattern with the other
import re
s="she sells sea shells at the seashore"
p="sea"
rp="ocean"
#re.sub(pattern, repl, string, count=0, flags=0)
new=re.sub(p,rp,s,1)
print(new)