# caesar cipher decode function
def caesar_cipher_decode(encoded_message, offset):
  """
  decode a message that was encoded using a caesar cipher.
    
  args:
    encoded_message (str): The message to decode
    offset (int): Number of positions each character shifts
    
  returns:
    str: the decoded message
  """
  decoded_message = ''

  for char in encoded_message:
    # check if character is a letter
    if char.isalpha():
      # determine ASCII offset based on case (uppercase or lowercase)
      ascii_offset = ord('A') if char.isupper() else ord('a')

      # convert to 0-25 range, shift forward, and handle wrap-around with modulo
      # note: we use (+)offset because we're decoding (going forward)
      offset_position = (ord(char) - ascii_offset + offset) % 26

      # convert back to ASCII and then to character
      decoded_char = chr(offset_position + ascii_offset)
      decoded_message += decoded_char
    else:
      # keep non-alphabetic characters unchanged
      decoded_message += char

  return decoded_message

# caesar cipher encode function
def caesar_cipher_encode(decoded_message, offset):
  """
  same pattern as 'caesar_cipher_decode' above,
  but encodes by shifting characters to the left
  """
  encoded_message = ''

  for char in decoded_message:
    # check if character is a letter
    if char.isalpha():
      # determine ASCII offset based on case (uppercase or lowercase)
      ascii_offset = ord('A') if char.isupper() else ord('a')

      # convert to 0-25 range, shift backward, and handle wrap-around with modulo
      # note: we use (-)offset because we're encoding (going backward)
      offset_position = (ord(char) - ascii_offset - offset) % 26

      # convert back to ASCII and then to character
      encoded_char = chr(offset_position + ascii_offset)
      encoded_message += encoded_char
    else:
      # keep non-alphabetic characters unchanged
      encoded_message += char
  
  return encoded_message

# input

# messages
coded_message_1 = 'xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!'

decoded_message_2 = 'Hi there! This message was written by Ben and encoded using a Caesar cipher.'
coded_message_2 = 'Xy jxuhu! Jxyi cuiiqwu mqi mhyjjud ro Rud qdt udsetut kiydw q Squiqh syfxuh.'

coded_message_3 = 'jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.'

coded_message_4 = 'bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!'

brute_force_coded_message_5 = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

offset_value = 14
decoded = caesar_cipher_decode(coded_message_4, offset_value)
# encoded = caesar_cipher_encode(decoded_message_2, offset_value)

# output
print('Encoded Message:', coded_message_4)
print('Decoded Message:', decoded)