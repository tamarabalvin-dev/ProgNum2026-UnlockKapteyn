import hashlib
import base64

hashed_code = "e2dd675897e442e27b39579ad16919a6"  
base_code = "dW5sb2NrLWthcHRleW4tc3VjY2Vzcw=="

# Verify user input
user_input = input("Enter password: ")
if hashlib.md5(user_input.encode()).hexdigest() == hashed_code:
    print("Correct Password!")
    print()
    print("To disable the Autoprotection Mode, use the following code in Task 3:") 
    print()
    print(base64.b64decode(base_code.encode()).decode())
    print()
else:
    print("Incorrect!!!")
