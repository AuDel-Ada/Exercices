# LEVEL 1
# Download tresor1.rar
# Shell from the files : unrar e tresor1.rar


# LEVEL 2
# from binary to alphanumeric
binaryList = ['01101010', '00100111', '01101001', '01110010', '01100001', '01101001', '00100000']
response1 = ""
for item in binaryList :
    letter = (chr(int(item, 2)))
    response1 += letter
print ("Step1 :", response1, type(response1))

# from decimal to hexadecimal
HexValue = hex(3499)
response2 = HexValue[2::]
print("Step2 :", response2, type(response2))

# from hexadecimal to alphanumeric
HexNumber = '65722073757220766f7320746f6d6265732021'
response3 = bytearray.fromhex(HexNumber).decode()
print("Step3 :", response3, type(response3))

Password = response1 + response2 + response3
print ("Password to enter to tresor2 :", Password)
print ("##### NEXT LEVEL #####")


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
