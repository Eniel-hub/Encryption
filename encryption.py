#simple encryption algorithm

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

EnOrDe = input('''Do you want to encrypt or decrypt a text?
Enter "E" to encrypt or "D" for decrypt''')

while (EnOrDe.upper() != 'E' and EnOrDe.upper() != 'D'):
    EnOrDe = input('''Wrong input.
Enter "E" to encrypt or "D" for decrypt''')

text = input('enter a text')

key = input('enter the key')

def encryption():
    ciText = ''
    j = 0
    
    for i in text :
        eL = 0 #encryption letter index
        
        if not i.isalpha() :
            ciText += i
            continue
        
        eL = (alphabet.index(i.upper()) + alphabet.index(key[j].upper())) % 26
        ciText += alphabet[eL]
        j = (j + 1) % len(key)
        
    return ciText

def decryption():
    deText = ''
    j = 0
    
    for i in text :
        dL = 0 #decryption letter index
        
        if not i.isalpha() :
            deText += i
            continue
        
        dL = alphabet.index(i.upper()) - alphabet.index(key[j].upper())
        if(dL < 0):
            dL += 26
            
        deText += alphabet[dL]
        j = (j + 1) % len(key)
        
    return deText



if EnOrDe.upper() == 'E' :
    encryption = encryption()
    print('the encryption of', text, 'is', encryption.capitalize())
else :
    decryption = decryption()
    print('the decryption of', text, 'is', decryption.capitalize())
    
