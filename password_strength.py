import re 

import re

def validate_password(password):
    
    if len(password) < 8:
        return "Weak password: Too short!"
  
    if not re.search(r'[A-Z]', password):
        return "Weak password: Add at least one uppercase letter"

    if not re.search(r'[a-z]', password):
        return "Weak password: Add at least one lowercase letter."
 
    if not re.search(r'\d', password):
        return "Weak password: Add at least one number."
 
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Weak: Add at least one special character."

    return "Strong Password!"

password = input("Enter your password: ")
result = validate_password(password)
print(result)
