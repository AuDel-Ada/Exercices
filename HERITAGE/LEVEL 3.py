#LEVEL 3
from itertools import chain, combinations
import subprocess

print("List of Password to try with tresor3 :")
PasswordEnd = ["Linus", "docker", "if", "opéra", "468153084652"]


def powerset(list_name):
    s = list(list_name)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

for world in powerset(PasswordEnd):
    
    set1 = "91Grace"+""
    for element in world:
        set1 += element
    print(set1)
    
    set2 = "91Margaret"+""
    for element in world:
        set2 += element
    print(set2)

# Command line
subprocess.Popen(['unrar', 'e', 'tresor3.rar'])