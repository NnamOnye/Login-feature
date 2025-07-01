#Python User Login Feature

users = {
#here instead of hardcoding the password you can ask the user for an input --> getinput() and store it 
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
    #add action: getinput()

  password = input() #will prompt for password
  if users[username] == password:
    print("Access granted")
    #add action: unlockdoor()
    return True
  else:
    print("Access Denied Re-enter Info Or Exit System")
    #add action: getinput()
  return False
  
if __name__ == "__main__":
# Simple loop to keep prompting for login until successful
  while not login():
    continue
  
  print("Access granted. You can now proceed with your tasks.")
  #add action: unlockdoor()
