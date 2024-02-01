import subprocess


def run_command(command):
    return subprocess.run(command, shell=True, capture_output=True, text=True)

while True:
    print("Welcome to github configuration!")
    
    while True:
        email: str = input("Enter your email: ")
        print(f"The email you entered is: {email}")
        answer_email: str = input(" Is it correct? (y/n)\n")
        if (answer_email == "y" or answer_email == "Y"):
            run_command(f"git config user.email '{email}'")
            break
        else: 
            continue
    

    while True:
        username: str = input("Enter your username: ")
        print(f"The username you entered is {username}")
        answer_username: str = input("Is it correct? (y/n)\n")
        if (answer_username == "y" or answer_username == "Y"):
            run_command(f"git config user.name '{username}'")
            break
        else:
            continue
    break