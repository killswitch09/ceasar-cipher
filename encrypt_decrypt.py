import string
import getpass
letter_to_int = dict(zip(string.ascii_lowercase,range(26)))
int_to_letter = dict(zip(range(26),string.ascii_lowercase))

key = 3
print("Hello There!")

#print(plaintext)  #<--- incase you want to check whether your input is right or not(remove the first #)
ciphered_text = ""
deciphered_text = ""

while bool:
  print("Do You Want To:\n1.Create A New Encrypted Text\n2.See The Encrypted Text\n3.See The Decrypted Text\n4.Quit\nSelect An Option(Enter The Number!)!\n\n")
  option = int(input())
  if option ==1:
    plaintext = getpass.getpass(prompt = 'Enter Your Message!\n')

    # encipher
    
    for c in plaintext.lower():
        if c.isalpha(): 
          ciphered_text += int_to_letter[ (letter_to_int[c] + key)%26 ] 
          #mapping through by taking advantage of dictionaries aka hashing
        else: 
          ciphered_text += c

    # decipher
    
    for c in ciphered_text.lower():
        if c.isalpha(): 
          deciphered_text += int_to_letter[ (letter_to_int[c] - key)%26 ]
        else: 
          deciphered_text += c
    option = 0
  elif option ==2:
    print ("\n\n ciphered text = ",ciphered_text,"\n\n")
    option = 0
    ciphered_text = ""
  elif option ==3:
   print ("\n\n deciphered text = ",deciphered_text,"\n\n")
   option = 0
   deciphered_text = ""
  else:
   print("\n\nTerminating The Program!!\n\n")
   break

