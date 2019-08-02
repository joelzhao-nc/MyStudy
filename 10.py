prompt="\nTell me:"
prompt+="\nEnter 'quit'."

message =""
while True:
    message =input(prompt)

    if message=='quit':
        break
    else:
        print(message)