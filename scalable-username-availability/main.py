from services.username_service import UsernameService
from utils.validation import validate_username

service = UsernameService()

while True:
       print("MENU OPTIONS")
       print("1. Register username")
       print("2. Popular usernames")
       print("3. Exit")
       try:
          choice =  int(input("Enter your choice here : "))
          if choice == 1 :
            username = input("Enter your username: ")
            if not validate_username(username):
                print("Username should contains only letters and numbers")
            elif service.registerUsername(username):
                  print("Username registered successfully...")
            else:
                  print("Username already taken!!!")
          elif choice == 2 :
             print(service.popular_usernames())
          else :
            exit(0)
       except ValueError:
          print("Invalid input!!! please enter 1,2 or 3")
       except Exception as e:
         print("Unexpected error",e)