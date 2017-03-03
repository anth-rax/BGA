###################
##------BoolGate Algo
##------Proof of Concept
##------Developed by Kris 2017
###################
import random
import string
import os
#GenKeys + GenCipher>Get Input>Proccess Keys>Proccess Input>Print Processed Input

def pull_plaintext_values(keys):
    """
Pull relevant plaintext values and form a new list 
Pass through function for unprocessed tokens
Parent: setup() or custom()
    """
    _PLAIN_TEXT  = list(input("Please enter the plaintext you wish to encrypt\n>"))
    _PULLED_VALUES = []
    for p in _PLAIN_TEXT:
        for c in range(len(keys)):
            if '###{}###'.format(p) in keys[c]:
                _PULLED_VALUES += keys[c]
    sort_values(_PULLED_VALUES)
    
def upload_cipher_keys():
    """
Reads files containing ONE cipher per file & ONE key per file of the same name
in different directories
Parent: setup()
    """
    nme = input("Please enter the name of the file you would like to import\n>")
    with open("STORE/Ciphers/{}".format(nme), "r") as ciph:
        for line in ciph:
            global CIPHER
            CIPHER = line
    with open("STORE/Tokens/{}".format(nme), "r") as tokens:
        for line in tokens:
            KEEZ = [line]
    pull_plaintext_values(KEEZ,CIPHER)
    

def  setup(): 
    """
Beginning function. Sends seed inputs to put all generators in motion.
Parent: None
    """
    _set = input("Enter a command, or type '/Commands' for a list of all commands\n>")
    set_all = list(string.printable) 
    set_low_digits = list(string.ascii_lowercase + string.digits)
    if _set == "ALL":
        get_cipher(1024) 
        get_methods(len(set_all),set_all)
    elif _set == "DLOW":
        get_cipher(1024)
        get_methods(len(set_low_digits),set_low_digits) 
    elif _set == "CUSTOM":
        tempinx = int(input("Please enter your KEY TOKEN length\n>"))
        tempiny = int(input("Please enter your desired CIPHER SIZE in BITS"))
        get_cipher(tempiny)     
        custom(tempinx,len(set_all), set_all)
    elif _set == "UPLOAD_":
        upload_cipher_keys()
    elif _set == "/Commands":
        print("""
[-]ALL - Generate key token values for all printable characters
[-]DLOW - Generate values for lowercase letters and digits
[-]CUSTOM - generate custom seed values for your encryption
[-]UPLOAD_ - Reads from an preselected directories for your keys and ciphers(one key per file + one cipher per file ---- Files must have same name
[-]/Commands - Shows this text
""")
        
def get_cipher(BITS):
    """
Generate Cipher
Parent: setup()
    """
    global CIPHER
    CIPHER = '' 
    for x in range(len(os.urandom(BITS))):
        CIPHER += random.SystemRandom().choice(str(string.ascii_letters + string.digits + "~!@#$%^&*()_+=-`"))
    
def custom(LENGTH, KEYSLOTS, SET):
    """
Generate methods --- Outputs tokens -- Specific For Custom Inputs
Parent if Invoked: setup() 
    """
    global KEYS
    KEYS = []
    print("Building your data...")
    for K in range(KEYSLOTS):
        hold_this = list()  
        for r in range(LENGTH):
            random.SystemRandom().choice("010101")
        if hold_this not in KEYS:
            KEYS.append(['###{}###'.format(SET[K]), hold_this])                                                                                                                                  
        if hold_this in KEYS:
            print("A fatal error or clash of indexes occured. Please rerun the program.")
    pull_plaintext_values(KEYS)
    
def get_methods(KEYSLOTS, SET):
    """
Generate methods --- Outputs tokens.
Parent: setup()
    """
    global KEYS
    KEYS = []
    print("Building your data...")
    for K in range(KEYSLOTS):
        LENGTH = random.SystemRandom().randrange(20,30)
        hold_this = list()  
        for r in range(LENGTH):
            x = random.SystemRandom().choice('010101')
            hold_this += x
        if hold_this not in KEYS and len(hold_this) == LENGTH :
            KEYS.append(['###{}###'.format(SET[K]), hold_this])                                                                                                                                  
        else:
            print("A fatal error or clash of indexes occured. Please rerun the program.")
    pull_plaintext_values(KEYS)
    
def sort_values(pulled):
    """
Sort values into a readable string
Parent: pull_plaintext_values()
    """
    _FINDEX = ''
    FINDEX = ''
    for k in range(len(pulled)):
        for r in range(len(pulled[k])):
            if '0' or '1' in pulled[k][r]:
                _FINDEX += pulled[k][r]
    for x in _FINDEX:   #LIST
        if x  == '0' or x == '1':
            FINDEX += x     #STRING
    encrypt(FINDEX,CIPHER)
    
def encrypt(indexstring,cipher):
    """
Reads sorted values from FINDEX
Parent: sort_values()

    """
    cipher = list(cipher)
    inx = indexstring
    ENCRYPTED = ''
    counter = 0
    mult = 2
    for x in indexstring:
        if x == '1':
            ENCRYPTED += cipher[counter]
        if counter >= len(cipher):
            cipher = cipher * mult
            mult = mult + 1
        counter = counter + 1
    print(ENCRYPTED)
    _save = input("Do you wish to save your cipher and keys?(Y/N)\n>")
    if _save == 'Y' or  _save == 'y':
        name = input("What would you like to name your file?(File will output in the same directory as BGA.py)\n>")
        with open("STORE/Ciphers/{}".format(name), "w+") as ciph:
            ciph.write("{}".format(CIPHER)) #Make sure not to include quotes when using these.. These will not appear in a cipher
        with open("STORE/Tokens/{}".format(name), "w+")as tokens:
            tokens.write("{}".format(KEYS))
setup()  ##Starting Function
