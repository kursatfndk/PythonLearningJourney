#camelCase
#snake_case method, değişken
#PascalCase sınıf

#PEP8 Python Standarları ***
#Boelan değerler True/False

username = "kursatemrefndk"
password = "123456"
age = 22
gender = 0 # Eğer 0 ise Erkek 1 ise Kadın 2 ise Diğer
is_active = True

customer_data = f"{username} {password} {age} {gender}"

def get_gender(gender):
  gender_text = ""
  if gender == 0:
    gender_text = "Erkek"
  elif gender == 1:
    gender_text = "Kadın"
  else:
    gender_text = "Diğer"
  print(f"Cinsiyet: {gender_text}")

if (username == "kursatemrefndk" and password == "123456"):
  if(is_active):
    print("Welcome!")
    print(f"Username: {username}")
    get_gender(gender)
  else:
    print("User exist! But inactive!")
else:
  print("Password wrong! Try again!")

