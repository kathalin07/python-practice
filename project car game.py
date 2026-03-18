print("type 'help' for more details!")
started = False
while True:
  command = input('command:').lower()
  if command == "help":
    print(""""
    start - to start the car
    stop - stop the car
    quit - to exit
    """)
  elif command == "start":
        if started :
             print('car is already started')
        else:
             started = True
             print("car is started")         
  elif command == "stop":
        if not started:
             print("car is already stopped!")
        else:
             started = False
             print('car is stopped')
  elif command == "quit":
        break    
  else:
        print("sorry i didn't understand that")