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

def crypto(choice,code,key):
    if choice == 2:
        key = -key
    out =''
    for symbol in code:
        if symbol.isalpha():
            num =ord(symbol)
            num += key

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
          out += symbol
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
    for i in range(26):
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







    
