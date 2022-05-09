import random
import string

def password_generator():
  # Characters used to generate the password
  upper = string.ascii_uppercase
  lower = string.ascii_lowercase
  num = string.digits
  symbols = string.punctuation

  # Structure of characters
  others = lower + num + symbols
  samp_others = random.sample(others, 17)
  samp_upper = random.sample(upper, 1)
  samp_all = samp_upper + samp_others

  # Printing the password
  print("".join(samp_all))
  
  password_generator()
  
