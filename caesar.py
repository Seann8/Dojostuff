'''
Caesar cipher

A simple Caesar cipher that uses the standard library to code and decode
strings. The project will teach kids about :
    1. String processing/Iteration 

    2. Functional programming

    3. Converting Data Types 

    4. building a rudimentary interface with raw input()

'''
#### functions :
'''
This function carries out the meat of the conversion , it takes the users choice ,message and private key 
and uses them to carry out the action. 

the great thing about the Caesar cipher is that you can get both the coding and decoding done with one function
if the key is a positive number  you are encrypting . To decrypt, make the key negative 
how it works :
    the function takes  the string and evaluates it character by character ;for each character it takes the following steps 
    
    1* check to see if the character is part of the english alphabet using .isalpha()
    2* if the symbol is ,the string is converted to it's ordinal value and the key is added 
    3* Next the edge cases are handled ,a and z will go out of scale if they have a key value subtracted or added respectively .
       This essentially wraps the number back around to the start of the alphabet
       
    The ordinal value is then converted back to its new string representation and added to the empty string out 
    
    '''

def crypto(choice,code,key):
    if choice == 2:
        key = -key
    out =''
    for symbol in code:
        if symbol.isalpha():  # makes sure the character is part of the alphabet 
            num =ord(symbol)  # Convert the string character to its ordinal version 
            num += key        # Adds the key value, to the ordinal number 

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
               if num >ord('z'):
                   num -= 26
               elif num < ord('a'):
                   num += 26
            out +=chr(num)
        else:
          out += symbol # if the character cannot be converted , it is just added to the message  
    return out 


# Step 1 a menu :


print (30 *'-')
print ("C O D E _ M A C H I N E ")
print (30 * '-')

print ("1. Encode Message")
print ("2. Decode Message")


choice = input('Enter your choice [1-2]:')

usrchoice = int(choice) 

## Step 2 work with menu option :

if usrchoice == 1:
   usrcode = input("please enter message:")
elif usrchoice == 2:
   usrcode = input("please enter coded message:")
elif usrchoice == 3:
    usrcode = input("Code breaker mode-- please enter message :")
    for i in range(26):     # this could be a fun little mode , creates a brute force cracking program
        cipher = crypto(usrchoice,usrcode,i)
        print('i #%s: %s:' %(i,cipher))
else :
    print("Invalid option. Try again")
# step 3 ask for key
if usrchoice in (1,2):
    
    cipherkey = int(input("what is your secret key?:"))

    if cipherkey in range (1,26):
        print("ok")

    else:
        print("key won't work, pick a number between 1 and 26")


    cipher = crypto(usrchoice,usrcode,cipherkey)

    print("your secret message is:")

    print(cipher)







    
