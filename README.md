    Note: This project is in no way secure. 
    ***********************
       HOW TO ENCRYPT
    ***********************
    The general concept behind the "security" of this algorithm is that nobody knows the length of
       your tokens. 
    For right now, tokens are randomly generated 1's and 0's between 20-30 char length. So a= 27ch, but b= 21ch. 
        As of right now, reading multiple letter like de = 20 char length doesn't work. It just won't be read.
        I plan on implementing this.
    I plan on implementing some XOR logic to further "security"
    The logic of encryption works as follows: 
    
    Plaintext: "PI"
    Token for P: 010 Token for for I: 001
    CIPHER: ABDEFG
    
    0 1 0 0 0 1
    A B D E F G 
       B      G
    
    Encrypted: BG
    
    Obviously, in most cases, your encrypted text will be much larger than your plaintext. The simplicity is just for the sake of example. 
    To see an example of an encryption using this program see EXAMPLE.txt 
    
      **********************
         HOW TO DECRYPT
      **********************
    
     -Not programmed yet
     Think of it like this table              E | C | OUT 
     CIPHER = ABDEFG                          B   A   0
     TOKEN = 010001                           B   B   1
     ENCRYPTED = BG                           G   D   0
                                              G   E   0
                                              G   F   0
                                              G   F   1
                                              
        [010] = P [001] = I
