import subprocess

def run_command(command) -> None:
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        print(e.stderr)

def get_user_input(prompt: str) -> str:
    while True:
        user_input = input(prompt)
        confirmation = input(f"You entered: {user_input}. Is it correct? (y/n)\n")
        if confirmation.lower() == 'y':
            return user_input

def configure_git() -> None:
    print("Welcome to GitHub configuration!")

    email = get_user_input("Enter your email: ")
    run_command(f"git config user.email '{email}'")

    username = get_user_input("Enter your username: ")
    run_command(f"git config user.name '{username}'")

    print("Git configuration completed successfully.")

if __name__ == "__main__":
    configure_git()
