# PythonLearningJourney

## Today's Python Topics

### Naming Conventions:
- **camelCase:** Used for method and variable naming.
- **snake_case:** Used for method and variable naming.
- **PascalCase:** Used for class naming.

### PEP8 Python Standards:
- **Boolean Values:** Written as True/False.

### Working on Sample Code:
- I wrote sample code containing user information. It includes username, password, age, and gender checks.
- I added an example using the `get_gender` function to print the gender.
- I created a structure that welcomes the user or displays an incorrect password message based on username and password validation.

### Sample Code:
```python
username = "kursatemrefndk"
password = "123456"
age = 22
gender = 0 # If 0, Male; if 1, Female; if 2, Other
is_active = True

customer_data = f"{username} {password} {age} {gender}"

def get_gender(gender):
    gender_text = ""
    if gender == 0:
        gender_text = "Male"
    elif gender == 1:
        gender_text = "Female"
    else:
        gender_text = "Other"
    print(f"Gender: {gender_text}")

if (username == "kursatemrefndk" and password == "123456"):
    if(is_active):
        print("Welcome!")
        print(f"Username: {username}")
        get_gender(gender)
    else:
        print("User exists but inactive!")
else:
    print("Password wrong! Try again!")
