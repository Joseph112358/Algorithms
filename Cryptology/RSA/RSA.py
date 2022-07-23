# Alphabet and associated code.
letters ={
  'A' : 2,
  'B' : 3,
  'C' : 4,
  'D' : 5,
  'E' : 6,
  'F' : 7,
  'G' : 8,
  'H' : 9,
  'I' : 10,
  'J' : 11,
  'K' : 12,
  'L' : 13,
  'M' : 14,
  'N' : 15,
  'O' : 16,
  'P' : 17,
  'Q' : 18,
  'R' : 19,
  'S' : 20,
  'T' : 21,
  'U' : 22,
  'V' : 23,
  'W' : 24,
  'X' : 25,
  'Y' : 26,
  'Z' : 27
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
# Letters causing crash: M,N
# Write algorithm to generate keys
encryption_result = rsa_algorithm_string(encryption_key,"Z")
print(encryption_result)
decryption_result = rsa_algorithm_string(decryption_key, encryption_result)
print(decryption_result)
