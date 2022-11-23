import random
import string

# first name and last name
firstName = "Rifat"
lastName = "Rahman"

# date of birth : day, month, year
date = random.randint(1, 31)
month = "February"
year = random.randint(1900, 2000)

# Email Field
email = ''.join(random.choice(string.ascii_lowercase) for i in range(10)) + "@gmail.com"

# Company field
company = "Red.Digital Limited"

# password
password = "Robi@123"
