def cred_checker(username,age_str,e_mail):
    name = username.strip()
    if len(name) < 3 or len(name) > 12:
           return "Error:Invalid username length"

    clean_age = age_str.strip()
    if not clean_age.isdigit():
        return "Age must be between 13 and 120"

    age = int(clean_age)
    if age < 13 or age > 120:
         return "Age must be between 13 and 120"
    
    mail = e_mail.strip().lower() 
    if "@" not in mail or "." not in mail:
              return "Error Invalid email format"


    return f"User {name} successfully registered with email {mail}"


print(cred_checker("  alex_dev  ", "24", "ALEX@example.COM"))
print(cred_checker("al", "24", "alex@test.com"))
print(cred_checker("alex", "10", "alex@test.com"))
print(cred_checker("alex", "abc", "alex@test.com"))
print(cred_checker("alex", "25", "invalidemail.com"))