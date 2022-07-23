# Alphabet and associated code.
letters ={
  'A' : 0,
  'B' : 1,
  'C' : 2,
  'D' : 3,
  'E' : 4,
  'F' : 5,
  'G' : 6,
  'H' : 7,
  'I' : 8,
  'J' : 9,
  'K' : 10,
  'L' : 11,
  'M' : 12,
  'N' : 13,
  'O' : 14,
  'P' : 15,
  'Q' : 16,
  'R' : 17,
  'S' : 18,
  'T' : 19,
  'U' : 20,
  'V' : 21,
  'W' : 22,
  'X' : 23,
  'Y' : 24,
  'Z' : 25
}

# Method for converting number to letter.
def number_to_letter(dictionary, lookup_number):
   for letter, number in dictionary.items():
       if lookup_number == number:
           return letter

# RSA encrypter/decrypter. Takes in a key and message.
# Disclaimer: this done not generate 2 keys, only utilizes generated ones.
def rsa_algorithm_string(key, string):
    return_string = ""
    for letter in string:
      # convert char to number
      number = letters[letter]
      # encrypt
      cipher_num = (number**encryption_key[0])%encryption_key[1]
      #convert to char
      cipher_char = number_to_letter(letters,cipher_num)
      return_string += cipher_char
    return(return_string)



encryption_key = (5,14)
decryption_key = (11,14)

# Letters with wrong encryption: O,P,Q,R,S,T,U,V,W,X,Y,Z
# Write algorithm to generate keys
encryption_result = rsa_algorithm_string(encryption_key,"ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(encryption_result)
decryption_result = rsa_algorithm_string(decryption_key, encryption_result)
print(decryption_result)
