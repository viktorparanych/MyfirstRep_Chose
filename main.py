#def + <name> + ():             function signature
#funtion declaration
def encrypt_by_key(message, key): # parameters
    # function body

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher = ""

    message = message.upper()

    for letter in message:
        if letter in alpha:
            index = (alpha.find(letter) + key) % len(alpha)


            cipher += alpha[index]
        
        else:
            cipher += letter

    print (cipher)


#function call
encrypt_by_key("To be or not to be", 5) # arguments

print ("*" * 100) #*****************************

encrypt_by_key("YT GJ TW STY YT GJ", -5)  