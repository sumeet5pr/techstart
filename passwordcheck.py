import re

def evaluate_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if re.search("[a-z]", password):
        strength += 1
    if re.search("[A-Z]", password):
        strength += 1
    if re.search("[0-9]", password):
        strength += 1
    if re.search("[!@#$%^&*()_+=-]", password):
        strength += 1

    return strength

def password_strength(password):
    strength = evaluate_strength(password)
    if strength == 5:
        return "Very Strong"
    elif strength == 4:
        return "Strong"
    elif strength == 3:
        return "Moderate"
    else:
        return "Weak"

def get_feedback(password):
    feedback = []
    if len(password) < 8:
        feedback.append("Password should be at least 8 characters long.")
    if not re.search("[a-z]", password):
        feedback.append("Password should include at least one lowercase letter.")
    if not re.search("[A-Z]", password):
        feedback.append("Password should include at least one uppercase letter.")
    if not re.search("[0-9]", password):
        feedback.append("Password should include at least one number.")
    if not re.search("[!@#$%^&*()_+=-]", password):
        feedback.append("Password should include at least one special character.")
    
    return feedback

password = input("Enter your password: ")
strength = password_strength(password)
feedback = get_feedback(password)

print(f"Password Strength: {strength}")
if feedback:
    print("Recommendations:")
    for item in feedback:
        print(f"- {item}")

input("Press Enter to exit...")
