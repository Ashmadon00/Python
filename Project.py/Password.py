#password strength checker
import re #library module
def check_password_strength(password):
    """" 
    function to check the strength of a password.
    """
    if len(password) < 8:
        return "Weak : Password must be at least 8 characters long."
    if not any (char.isdigit() for char in password):
        return "Weal : Password must include at least one number." #not incase if the password is wrong it will print
    
    if not any (char.isupper() for char in password):
        return "Weak : Password must include ar least one lowercase letter."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Medium: Add special characters to make your password stronger."
    return "strong: Your password is secure!"
def password_checker():
    """" 
    Main function to take user input and check password strength.
    """
    print("Welcome to the password strength checker!")
while True:
        password = input("\nEnter your password (or type 'exit' to quit): ")
        if password.lower() == "exit":
            print("Thankyou for using the password strength checker! Goodbye!")
            break
        result = check_password_strength(password)
        print(result)
        
#run the password checker
if __name__ == "__main__":
    password_checker()