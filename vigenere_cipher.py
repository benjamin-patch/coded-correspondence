# vigenère cipher decode function
def vigenere_decode(coded_message, keyword):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  decoded_message = []
  key_position = 0  # track our position in the keyword
  
  # convert keyword to lowercase for consistency
  keyword = keyword.lower()
  
  for letter in coded_message:
    if not letter.isalpha():
      # keep non-letters as-is
      decoded_message.append(letter)
      continue
      
    # get corresponding keyword letter (cycles using modulo)
    key_char = keyword[key_position % len(keyword)]
    
    # find positions in alphabet
    cipher_pos = alphabet.index(letter.lower())
    key_pos = alphabet.index(key_char)
    
    # reverse the original shift (add instead of subtract)
    decoded_pos = (cipher_pos + key_pos) % 26
    
    # preserve original case
    decoded_char = alphabet[decoded_pos]
    if letter.isupper():
      decoded_char = decoded_char.upper()
        
    decoded_message.append(decoded_char)
    key_position += 1  # move to next keyword letter
    
  return ''.join(decoded_message)

# input
coded_message_1 = 'txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztylktoikqq!'
keyword_1 = 'friends'

# function call
decoded = vigenere_decode(coded_message_1, keyword_1)

# output
print('Encoded Message:', coded_message_1)
print('Decoded Message:', decoded)