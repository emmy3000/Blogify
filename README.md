# Blogify - Minimalistic Blogging Web Application

**ALX Africa Software Engineering: Backend Engineering Specialization**

## Project Overview:

Blogify is a minimalistic blogging web application developed as a part of the ALX Africa Software Engineering Backend Engineering Specialization. The project serves as a practical demonstration of utilizing the Flask web framework for creating a dynamic and user-friendly platform.

## Features:

**User Authentication:**

- Users can sign up for new accounts.
- Existing users can sign in securely.

**Blog Functionality:**

- Users can create new blog posts.
- Existing posts can be updated.
- Users have the ability to delete posts.

**Password Management:**

- Users can reset their passwords securely.

## Technology Stack:

The project is built using Python's Flask web framework, chosen for its robust set of components and the strong support it receives from the developer community. Flask provides a solid foundation for handling user authentication, managing blog posts, and implementing secure password reset functionality.

**Database:**

The project utilizes SQLite3, a lightweight and efficient relational database management system. SQLite3 was chosen for its simplicity and seamless integration with Flask, making it ideal for the minimalistic nature of the Blogify application.

## Project Structure

Key Directories and Files:

**blogify_app:**

- Main application directory containing the core functionality of the app.

    **config.py:**
    
    - Configuration settings mostly concerned with environment variables.

    **errors:**

    - Handling error pages and related logic.

    **landing_bp:**
                
    - Landing page routes and functionality.

    **main:**

    - Main application routes.

    **posts:**

    - Posts related logic and routes.

    **static:**

    - Static files like CSS and images.

    **templates:**

    - HTML templates for different pages.

    **users:**

    - User-related functionality.

**instance:**
                          
- Database or instance files.

**requirements.txt:**
                          
- List of required Python packages.

**run.py:**

- Entry point for running the application.

**template.env:**

- Template file describing the format environment variables are defined in the `.env` file.

Other Files:

**create_users_and_posts.py:**

- Script used in creating dummy users and posts.

**exp_token.py:**

- Script illustrating a basic example of how tokens are serialized and signed. This helps explain the foundation of 
how users' password reset abilities can be achieved.

*Purpose:*

This section outlines the purpose of key directories and files within the project. It provides a high-level overview,
making it easier for contributors and developers to navigate and understand the organization of the codebase.

## Installation:

To set up the project locally, follow these steps:

- Create & Activate a virtual environment.

    - It is important to create a separate virtual environment to ensure the project's dependencies and operations 
      are isolated to avoid being compromised which can lead to undefined behaviours on interaction with certain 
      global applications found on the machine:
    ```shell
    #  Create a virtual environment.
    python3 -m venv <venv_name>
  
    # Activate the virtual environment
  
    # For Windows
    <venv_name>\Scripts\activate.bat
  
   # For Unix/Linux
   source <venv_name>/bin/activate
   # or
   . <venv_name>/bin/activate 
   ```

- Clone the project repository.

```shell
git clone https://github.com/emmy3000/Blogify.git
```

- Make sure `SQLite3` is installed on your machine:

    - *Windows*:
  
        - Visit the SQLite download page at https://www.sqlite.org/download.html.

        - Scroll down to the "Precompiled Binaries for Windows" section and find the "Precompiled Binaries for 
      Windows" header.

        - Underneath the header, you'll find a list of available downloads. Look for the 
      "sqlite-tools-win32-x86-xxxxxx.zip" link (where "xxxxxx" represents the version number).

        - Download the ZIP file corresponding to your system's architecture (32-bit or 64-bit).

        - Extract the contents of the ZIP file to a directory of your choice.

        - Open the extracted directory and locate the sqlite3.exe file. This is the SQLite command-line shell.

        - You can now open a Command Prompt window (CMD) and navigate to the directory where you extracted the SQLite 
      files.

        - In the Command Prompt window, run sqlite3 to start the SQLite command-line shell.

    - *Linux (Ubuntu/Debian)*:

        - Open a terminal window.

        - Run the following command to install SQLite:
        ```bash
        sudo dnf install sqlite

        # or

        sudo yum install sqlite
        ```

        - After the installation is complete, you can start using SQLite by running the sqlite3 command in the 
      terminal.

    - *macOS*:

        - SQLite is included as part of the macOS operating system by default, so you don't need to install it 
      separately on a MacBook. You can access SQLite directly from the terminal.

        - To use SQLite on your MacBook, follow these steps:

        - Open the Terminal application. You can find it in the "Utilities" folder within the "Applications" folder, 
      or you can use Spotlight search (Cmd + Space) and type "Terminal" to launch it.

        - Once the Terminal is open, type `sqlite3` and press `Enter`. This will start the SQLite command-line shell.

        - You should now see the SQLite prompt, which looks like sqlite>. You can now start using SQLite commands and 
      interact with databases.

        - If you want to create a new SQLite database or work with an existing one, you can use SQLite commands 
      within the SQLite prompt. For example, to create a new database, you can use the following command:
        ```shell
        sqlite> .open instance/site.db
        ```
      
        - This will create a new SQLite database file named database_name.db.

        - To exit the SQLite prompt, you can use the .exit command:
        ```shell
        sqlite> .exit
        ```

- Initialize the Database with Dummy Data (Optional):

    The project includes scripts like `create_users_and_posts.py` to create dummy users and posts, you can run it to 
  populate the database. The script is located at the root of the project's repository.
    ```shell
    python create_users_and_posts.py
    ```

- Verify Database Initialization:

    Check your instance directory for the SQLite database file (usually named `site.db`). If it's present, the database setup is successful.
    ```sqlite
    -- Establish a connection to the specified database file.
    sqlite3 instance/site.db
  
    -- Show tables
    .tables

   -- Describe a specific table (replace 'table_name' with the actual table name)
   .schema table_name

   -- Execute SQL queries
   SELECT * FROM table_name;
  
   -- exit the SQLite shell
   .quit
   ```

- Install dependencies needed for the project.

    - The project has a file named `requirements.txt` which contains all the package dependencies along with their 
      versions needed for the project to run smoothly, to install these dependencies run the command:
    ```shell
    pip install -r requirements.txt
    ```

- Run the application

    - After following all previous instructions concerning the project's installation the application can now be 
      executed using the syntax:
    ```shell
    python run.py
    ```

## Usage:

The application provides a user-friendly interface for navigating through the blog, creating and updating posts, and 
managing user accounts. Detailed usage instructions can be found in the documentation.

## Contributing:

Contributions to the project are welcome! If you'd like to contribute, please follow the guidelines outlined in the [Contribution Guide](CONTRIBUTING.md).

## License:

This project is licensed under the [MIT License](LICENSE).

## Author:

[Emeka Emodi Obiora](https://github.com/emmy3000)