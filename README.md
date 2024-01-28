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

This section provides an in-depth look at the repository's content, showcasing its architecture and interconnections.

**Project's Tree Directory Structure:**

```markdown
❯ tree
.
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── blogify_app
│   ├── __init__.py
│   ├── config_development.py
│   ├── config_production.py
│   ├── errors
│   │   ├── __init__.py
│   │   └── handlers.py
│   ├── landing_bp
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── main
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── models.py
│   ├── posts
│   │   ├── __init__.py
│   │   ├── forms.py
│   │   └── routes.py
│   ├── static
│   │   ├── img
│   │   │   ├── engage_community_image.jpg
│   │   │   ├── group_discussion.jpg
│   │   │   ├── responsive_design_image.jpg
│   │   │   ├── seamless_sharing_image.jpg
│   │   │   ├── share_posts.jpg
│   │   │   ├── streamlined_navigation_image.jpg
│   │   │   ├── testimonial_aisha.jpg
│   │   │   ├── testimonial_chijioke.jpg
│   │   │   ├── testimonial_emily.jpg
│   │   │   ├── testimonial_faith.jpg
│   │   │   ├── testimonial_javier.jpg
│   │   │   ├── testimonial_mensah.jpg
│   │   │   ├── testimonial_pierre.jpg
│   │   │   ├── user_accounts_image.jpg
│   │   │   ├── user_accounts_image_resized.jpg
│   │   │   ├── write_posts.jpg
│   │   │   ├── write_publish_image.jpg
│   │   │   └── write_publish_image_resized.jpg
│   │   ├── main.css
│   │   └── profile_pics
│   │       ├── 62633c87aa000ef4.jpg
│   │       └── f053e6693594d69d.jpg
│   ├── templates
│   │   ├── about.html
│   │   ├── account.html
│   │   ├── create_post.html
│   │   ├── errors
│   │   │   ├── 403.html
│   │   │   ├── 404.html
│   │   │   └── 500.html
│   │   ├── home.html
│   │   ├── landing_page.html
│   │   ├── layout.html
│   │   ├── login.html
│   │   ├── post.html
│   │   ├── register.html
│   │   ├── reset_request.html
│   │   ├── reset_token.html
│   │   └── user_posts.html
│   └── users
│       ├── __init__.py
│       ├── forms.py
│       ├── routes.py
│       └── utils.py
├── create_users_and_posts.py
├── exp_token.py
├── instance
│   └── site.db
├── requirements.txt
├── run.py
└── template.env

13 directories, 63 files

```

### Key Directorys and Files

**`blogify_app/`**

- The main application directory contains the core functionality of the app.

  **`__init__.py`**

  - A central initialization module that orchestrates the setup of crucial components like the database, user 
    authentication, and email handling. It plays a pivotal role in configuring and initializing the entire Flask application.

  **`config_production.py`**

  - Configuration settings for the production environment. Tailored for deployment with specific environment 
    variables and settings.

  **`config_development.py`**

  - Configuration settings for the development environment. Optimized for debugging and testing during local 
    development.

  **`errors/handlers.py`**

  - Handling error pages and related logic.

  **`landing_bp/`**

  - Landing page routes and functionality.

  **`main/`**

  - Main application routes.

  **`posts/`**

  - Posts related logic and routes.

  **`static/`**

  - Static files containing the project's style sheet and images.

  **`templates/`**

  - HTML templates for different pages.

  **`users/`**

  - User-related functionality.

**`instance/`**

- Database or instance files.

**`.env`**

- Environment Configuration customized for saving important data assigned to certain environment variables such as 
  database URLs, API keys, and other sensitive information. Referenced by `template.env`.

**`.gitignore`**

- Version Control Ignore List for specifying intentionally untracked files that Git should ignore, preventing 
  unnecessary or sensitive files from being included in version control.

**`requirements.txt`**

- List of required Python packages necessary for the project's development.

**`run.py`**

- Project's entry point for running the application.

**`template.env`**

- A template file describing the format of environment variables defined in the `.env` file.

### Example Test Files:

**`create_users_and_posts.py`**

- Script for creating dummy users and posts.

**`exp_token.py`**

- A script illustrating a basic example for demonstrating how tokens can be serialized and signed. Illustrates the 
  foundation of users' password reset abilities.

### Other Files:

**`CODE_OF_CONDUCT.md`**

- Outlines expected behavior for contributors, maintainers, and participants, fostering an inclusive and welcoming community.

**`CONTRIBUTING.md`**

- Guidelines provide information on how individuals can contribute to the project, including reporting issues, 
  submitting feature requests, and guidelines for code contributions.

**`LICENSE`**

- Specifies the terms and conditions under which the project's source code and assets are distributed. Legally 
  governs how others can use, modify, and distribute the project.

**`README.md`**

- The project's documentation provides essential information for users and contributors. Includes an overview of the project, installation instructions, usage examples, and other relevant details. A well-crafted readme enhances the project's accessibility and encourages collaboration.

### Purpose:

This organized structure offers a clear and comprehensive guide, making it easier for contributors and developers to 
navigate and understand the organization of the codebase.

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
    ```sql
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
managing user accounts. If you'd like to explore the deployed version of Blogify, you can access it through your web browser.

**Access the Deployed Project:**

To access the deployed version of Blogify, simply open your web browser and enter the following IP address:

[http://54.219.130.128](http://54.219.130.128)

This will direct you to the live web application, where you can experience the features of Blogify firsthand.

**Note:** Make sure you have a stable internet connection before accessing the deployed version.

Detailed usage instructions for the locally hosted version can be found in the documentation.


## Contributing:

Contributions to the project are welcome! If you'd like to contribute, please follow the guidelines outlined in the [Contribution Guide](CONTRIBUTING.md).

## License:

This project is licensed under the [MIT License](LICENSE).

## Author:

[Emeka Emodi Obiora](https://github.com/emmy3000)