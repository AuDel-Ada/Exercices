# LEVEL 1
# Download tresor1.rar
# Shell from the files : unrar e tresor1.rar


# LEVEL 2
# Construct the password
# -> from binary to alphanumeric
binaryList = ['01101010', '00100111', '01101001', '01110010', '01100001', '01101001', '00100000']
response1 = ""
for item in binaryList :
    letter = (chr(int(item, 2)))
    response1 += letter
print ("Step1 :", response1, type(response1))

# -> from decimal to hexadecimal
HexValue = hex(3499)
response2 = HexValue[2::]
print("Step2 :", response2, type(response2))

# -> from hexadecimal to alphanumeric
HexNumber = '65722073757220766f7320746f6d6265732021'
response3 = bytearray.fromhex(HexNumber).decode()
print("Step3 :", response3, type(response3))

Password = response1 + response2 + response3
print ("Password to enter to tresor2 :", Password)

# Command lines from script :

import pexpect
import time

child = pexpect.spawn ("unrar", ["e", "tresor2.rar"])

child.expect ("password")
time.sleep (0.1)
child.sendline (Password)
choices = child.expect (["incorrect", "xtracting"])
if choices == 0 :
    print ("Wrong password")
if choices == 1 :
    time.sleep (2)
    print ("Process completed")