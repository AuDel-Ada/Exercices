# LEVEL 1
# Download tresor1.rar
# Shell from the files : unrar e tresor1.rar

# LEVEL 2
# from binary to alphanumeric
binaryList = ['01101010', '00100111', '01101001', '01110010', '01100001', '01101001', '00100000']
letter = []
for item in binaryList :
    part = (chr(int(item, 2)))
    letter.append(part)
print ("Test 'letter' : ", letter, type(letter))
response1 = ""
for item in letter :
    response1 += item
print (response1)
# response1 = chr(int(BinaryNumber, 2))
# print("Step1 :", response1, type(response1))

# from decimal to hexadecimal
HexValue = hex(3499)
response2 = HexValue[2::]
print("Step2 :", response2, type(response2))

# from hexadecimal to alphanumeric
HexNumber = '65722073757220766f7320746f6d6265732021'
# response3 = int(HexNumber,16)
# print("Step3 :", response3, (type(response3)))
response3 = bytearray.fromhex(HexNumber).decode()
print("Step3 :", response3, type(response3))

# Password = (str(response1)) + response2 + response3
# print (Password)