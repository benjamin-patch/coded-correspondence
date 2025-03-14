# message one
coded_message_1 = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"

def caesar_cipher_decode(encoded_message, shift):
  """
  Decode a message that was encoded using a Caesar cipher.
    
  Args:
    encoded_message (str): The message to decode
    shift (int): Number of positions each character was shifted by
    
  Returns:
    str: The decoded message
  """
  decoded_message = ""

  for char in encoded_message:
    # check if character is a letter
    if char.isalpha():
      pass
    else:
      # keep non-alphabetic characters unchanged
      decoded_message += char

  return decoded_message

# output
encoded = coded_message_1
decoded = caesar_cipher_decode(encoded, 3)

print('Encoded Message:', encoded)
print('Decoded Message:', decoded)