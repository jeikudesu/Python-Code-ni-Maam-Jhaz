# REGULAR EXPRESSION

import re

email = "sample@email.com"

if re.match(r"[^@]+@[^@]+\.[^@]+", email):
    print("Valid email format")
else:
    print("Invalid email format")
