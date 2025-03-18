# vigenère cipher encode/decode function
def vigenere_cipher(text, keyword, mode='decode'):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  result = []
  key_index = 0
  
  keyword = keyword.lower()
  
  for char in text:
    if not char.isalpha():
      result.append(char)
      continue
        
    # get corresponding keyword letter
    key_char = keyword[key_index % len(keyword)]
    key_pos = alphabet.index(key_char)
    
    # determine shift direction
    if mode == 'encode':
      shift = -key_pos  # encoding uses subtraction
    else:  # decode
      shift = key_pos   # decoding uses addition
    
    # calculate new position
    char_pos = alphabet.index(char.lower())
    new_pos = (char_pos + shift) % 26
    
    # preserve case
    new_char = alphabet[new_pos]
    if char.isupper():
      new_char = new_char.upper()
        
    result.append(new_char)
    key_index += 1
    
  return ''.join(result)

# input
message_1 = "barry is the spy"
keyword_1 = "dog"
coded_message_2 = 'txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztylktoikqq!'
keyword_2 = 'friends'

# output
decoded = vigenere_cipher(coded_message_2, keyword_2)
print(f"Decoded: {decoded}")

encoded = vigenere_cipher(decoded, keyword_2, 'encode')
print(f"Encoded: {encoded}")