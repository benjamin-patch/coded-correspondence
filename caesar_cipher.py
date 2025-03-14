# caesar cipher decode function
def caesar_cipher_decode(encoded_message, offset):
  """
  Decode a message that was encoded using a Caesar cipher.
    
  Args:
    encoded_message (str): The message to decode
    offset (int): Number of positions each character shifts
    
  Returns:
    str: The decoded message
  """
  decoded_message = ''

  for char in encoded_message:
    # check if character is a letter
    if char.isalpha():
      # determine ASCII offset based on case (uppercase or lowercase)
      ascii_offset = ord('A') if char.isupper() else ord('a')

      # convert to 0-25 range, shift backward, and handle wrap-around with modulo
      # note: we use (+)offset because we're decoding (going forward)
      offset_position = (ord(char) - ascii_offset + offset) % 26

      # convert back to ASCII and then to character
      decoded_char = chr(offset_position + ascii_offset)
      decoded_message += decoded_char
    else:
      # keep non-alphabetic characters unchanged
      decoded_message += char

  return decoded_message

# input

# message one
coded_message_1 = 'xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!'

encoded = coded_message_1
offset_value = 10
decoded = caesar_cipher_decode(encoded, offset_value)

# output
print('Encoded Message:', encoded)
print('Decoded Message:', decoded)