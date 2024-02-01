# Local Repository Credentials Config

This script streamlines the process of setting up local Git repository credentials, especially when using different GitHub accounts for university and work/personal projects. Instead of manually typing Git configuration commands, the program prompts you for your email and username, confirms the input, and executes the commands automatically.

## Usage:

To make the program accessible from any directory, you need to build it first.

1. Run the following command to build the executable using PyInstaller:

   ```bash
   pyinstaller --onefile github-repo.py
   ```
this will create a directory called `dist` in the folder.

- Add the dist directory to the PATH variable to make the executable globally accessible.
- Now, you can run the script with the following command:
```bash
github-repo
```

The program will guide you through the process of configuring your Git credentials for the current project.