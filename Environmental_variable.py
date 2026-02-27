
import os
from dotenv import load_dotenv

# 1. This "loads" the variables from the .env file into your system
load_dotenv()

# 2. Access them using os.getenv
a = os.getenv("CARD_PIN")
b = os.getenv("LAPTOP_PASSWORD")
c = os.getenv("CNIC_NUMBER")
d = os.getenv("House_no")

# Now you can use them safely
print(f"Accessing data for CNIC: {c}...") 
print(f"Accessing data for CARD_PIN: {a}, {d}...") 
# (Note: In a real app, don't even print them!)
