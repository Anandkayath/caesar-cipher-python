print("""   
_____   ______               _____   ______   _____ 
/ ____| |  ____|     /\      / ____| |  ____| |  __ \ 
| |      | |__       /  \    | (___   | |__    | |__) |
| |      |  __|     / /\ \    \___ \  |  __|   |  _  / 
| |____  | |____   / ____ \   ____) | | |____  | | \ \ 
\_____| |______| /_/    \_\ |_____/  |______| |_|  \_\ 
_____   _____              _____    _    _   ______   _____ 
/ ____| |_   _|     /\     |  __ \  | |  | | |  ____| |  __ \ 
| |        | |      /  \    | |__) | | |__| | | |__    | |__) |
| |        | |     / /\ \   |  ___/  |  __  | |  __|   |  _  / 
| |____   _| |_   / ____ \  | |      | |  | | | |____  | | \ \ 
\_____| |_____| /_/    \_\ |_|      |_|  |_| |______| |_|  \_\ 
""")

import datetime

# initialization of variables
letters = [
    " ","!","@","#","$","%","^","&","*","(",")","-","=","+",".",
    "0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i",
    "j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
    "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
]

ask_text = input("Enter your text that you wanna 'encrypt' or 'decrypt':- ").lower()
ask_user = int(input("""
Enter 1 for encryption
Enter 2 for decryption
Enter your choice:-"""))
ask_shift = int(input("Please enter your shift number:- "))

# the encryption function
def encrypt(text):
    final_text = ""
    for i in text:
        no = letters.index(i) + ask_shift
        final_text += letters[no]
    return final_text

# decryption function
def decrypt(text):
    final_text = ""
    for i in text:
        no = letters.index(i) - ask_shift
        final_text += letters[no]
    return final_text

# process the choice
if ask_user == 1:
    ans = encrypt(ask_text)
    print("The encrypted message is:")
    print(ans)
    with open("encrypt.txt","w") as p:
        p.write("encrypted message is following:-\n")
        p.write("Date:-" + str(datetime.datetime.now()) + "\n")
        p.write(ans + "\n")

elif ask_user == 2:
    ans = decrypt(ask_text)
    print(f"The decrypted message of '{ask_text}' is:")
    print(ans)
    with open("decrypt.txt","w") as p:
        p.write("Date:-" + str(datetime.datetime.now()) + "\n")
        p.write(f"the encrypted message of '{ask_text}' decryption is following:\n")
        p.write(ans + "\n")
else:
    print("wrong input")
