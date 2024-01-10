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
    
    - Configuration settings.

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

This section outlines the purpose of key directories and files within the project. It provides a high-level overview, making it easier for contributors and developers to navigate and understand the organization of the codebase.

## Installation:

To set up the project locally, follow these steps:

- Clone the project repository.

```shell
git clone https://github.com/emmy3000/Blogify.git
```