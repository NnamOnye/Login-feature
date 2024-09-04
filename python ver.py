#RUN CODE HERE
#PRACTICE:LOGIN IF-ELSE STATEMENT FOR USERNAME AND PASSWORD ENTRY

users = {
  "user1": "password1",
  "user2": "password2",
  "user3": "password3"
}
def login():
  
  print("Hello! Please Enter Username")
  
  username  = input() #will prompt for username
  if username in users:
    print("Welcome enter your password")
    return True
  else:
    print("INCORRECT")
    return False

  password = input() #will prompt for password
  if users[username] == password:
    print("Access granted")
    return True
  else:
    print("Access Denied Re-enter Info Or Exit System")
  return False
  
if __name__ == "__main__":
# Simple loop to keep prompting for login until successful
  while not login():
    continue
  
  print("Access granted. You can now proceed with your tasks.")