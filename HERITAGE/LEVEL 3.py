#LEVEL 3

# Construct the password
from itertools import chain, combinations

print("List of Password to try with tresor3 :")
PasswordEnd = ["Linus", "docker", "if", "opéra", "468153084652"]

def powerset(list_name):
    s = list(list_name)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

for world in powerset(PasswordEnd):
    
    set1 = "91Grace"+""
    for element in world:
        set1 += element
    
    set2 = "91Margaret"+""
    for element in world:
        set2 += element
        
    print (type(set1))
    Password = set1 + set2
    print(Password)

# Command lines from script :

# import pexpect
# import time

# child = pexpect.spawn ("unrar", ["e", "tresor3.rar"])

# child.expect ("password")
# time.sleep (0.1)
# child.sendline (set1)
# choices = child.expect (["incorrect", "xtracting"])
# if choices == 0 :
#     print ("Wrong password")
# if choices == 1 :
#     time.sleep (2)
#     print ("Process completed")