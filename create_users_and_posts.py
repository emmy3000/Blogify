#!/usr/bin/env python3
"""
Populate the database with dummy users and posts
for initial project data.

- This script initializes the database by creating sample users
  and posts, simulating initial data for the project.
- It ensures a clean slate by dropping existing tables
  and recreating fresh ones.
- The use of Flask-Bcrypt enhances security by hashing user passwords
  before storage.

Author: [Emeka Emodi] <emodiemeka@gmail.com>
"""

from blogify_app import db, create_app, bcrypt, User, Post
from blogify_app.config import Config


def create_users():
    users_data = [
        {
            "firstname": "Emeka",
            "lastname": "Emodi",
            "username": "mex619",
            "email": "emodiemeka@gmail.com",
            "password": "password",
        },
        {
            "firstname": "Olivia",
            "lastname": "Juma",
            "username": "sweet_olive100",
            "email": "olivia@example.com",
            "password": "password",
        },
        {
            "firstname": "Mousa",
            "lastname": "Diop",
            "username": "mdiop2real",
            "email": "moussa@example.com",
            "password": "password",
        },
        {
            "firstname": "Lerato",
            "lastname": "Ndlovu",
            "username": "terra.lera3000",
            "email": "lerato@example.com",
            "password": "password",
        },
        {
            "firstname": "Abdul",
            "lastname": "Kadir",
            "username": "gentle_abdul",
            "email": "abdul@example.com",
            "password": "password",
        },
        {
            "firstname": "Mariam",
            "lastname": "Ejeh",
            "username": "queen_mariam_d_first",
            "email": "mariam@example.com",
            "password": "password",
        },
        {
            "firstname": "Anna",
            "lastname": "Schmidt",
            "username": "pretty-anna10",
            "email": "anna@example.com",
            "password": "password",
        },
        {
            "firstname": "Carlos",
            "lastname": "Gutierrez",
            "username": "carlosGstylo",
            "email": "carlos@example.com",
            "password": "password",
        },
        {
            "firstname": "Ikenna",
            "lastname": "Okafor",
            "username": "ikemannn808",
            "email": "ikenna@example.com",
            "password": "password",
        },
        {
            "firstname": "Adien",
            "lastname": "O'Connor",
            "username": "doc_connor",
            "email": "aiden@example.com",
            "password": "password",
        },
    ]

    hashed_passwords = [
        bcrypt.generate_password_hash(user_data["password"]).decode("utf-8")
        for user_data in users_data
    ]
    users = [
        User(
            firstname=user_data["firstname"],
            lastname=user_data["lastname"],
            username=user_data["username"],
            email=user_data["email"],
            password=hashed_password,
        )
        for user_data, hashed_password in zip(users_data, hashed_passwords)
    ]
    return users


def create_posts(users):
    posts_data = [
        {
            "title": "My First Blog Post",
            "content": "I'm excited to start my blogging journey with just two simple words... Hello World!",
            "user_id": 1,
        },
        {
            "title": "Exploring Python Elegance",
            "content": "Delving into the intricacies of Python magic! Discovered the elegance of list comprehensions "
            "and their impact on code readability. Magical coding at its finest! ✨ #PythonElegance",
            "user_id": 1,
        },
        {
            "title": "Journey into Machine Learning",
            "content": "Embarking on a journey through the vast landscapes of machine learning. "
            "Today, I trained my first neural network to recognize patterns in data. "
            "The power of AI is truly awe-inspiring! 🤖 #MachineLearningOdyssey",
            "user_id": 3,
        },
        {
            "title": "Code Review Masterpiece",
            "content": "Navigating the labyrinth of code review! Shared my latest project "
            "with the team, and the collaborative effort led to the creation of a robust "
            "and error-free masterpiece. "
            "Code review adventures continue! 💻🚀 #CodeReviewMasterpiece",
            "user_id": 4,
        },
        {
            "title": "Web Development Excellence",
            "content": "Crafting the foundations of a web empire! Explored the latest front-end "
            "frameworks and their influence on user experience. Every line of code "
            "is a step toward web development excellence! 🌐 #WebEmpireCrafting",
            "user_id": 5,
        },
        {
            "title": "Future-Ready Systems Architecture",
            "content": "Architecting scalable systems for the future! Explored the principles "
            "of microservices architecture and its impact on large-scale applications. "
            "Designing the future of software systems! 🏗️ #FutureSystemsDesign",
            "user_id": 1,
        },
        {
            "title": "Coding Amidst Nature",
            "content": "Finding inspiration in the serenity of nature! Took a coding break "
            "to absorb the beauty of the great outdoors. A moment of tranquility "
            "before diving back into the algorithmic storm! 🌲 #NatureCodingInspiration",
            "user_id": 7,
        },
        {
            "title": "Embracing Serverless Computing",
            "content": "Adapting to the revolutionary era of the cloud! Explored serverless "
            "computing and its transformative impact on modern application development. "
            "Sky's not the limit; it's the beginning! ☁️ #CloudRevolution",
            "user_id": 8,
        },
        {
            "title": "Mastery in Debugging",
            "content": "Embarking on debugging adventures! Tackled a formidable bug today, "
            "unraveling its mysteries through careful code dissection. "
            "Every bug conquered is a step toward coding mastery! 🐞💡 #DebuggingMastery",
            "user_id": 9,
        },
        {
            "title": "Journey in Assembly Language",
            "content": "Deciphering the language of machines! Explored the nuances of assembly "
            "language programming, unraveling the simplicity of machine instructions. "
            "A coding journey to the core! 💻 #AssemblyLanguageJourney",
            "user_id": 10,
        },
        {
            "title": "Reflection on Coding Excellence",
            "content": "Reflecting on a triumphant coding feat! Successfully optimized a critical "
            "section of my code, unlocking new levels of efficiency. "
            "The pursuit of coding excellence knows no bounds! "
            "⚙️🚀 #CodingExcellenceReflection",
            "user_id": 1,
        },
        {
            "title": "Community-Driven Coding Immersion",
            "content": "Immersing in community-driven coding! Joined a vibrant coding community "
            "and engaged in insightful discussions. Collaboration fuels innovation, "
            "and the coding journey becomes richer! 👩‍💻👨‍💻 #CommunityDrivenCoding",
            "user_id": 2,
        },
        {
            "title": "Crafting Elegant Code",
            "content": "Crafting elegant and maintainable code! Embracing clean code principles "
            "to ensure scalability and ease of collaboration. "
            "What's your favorite code refactoring technique? 💻🌟 #CleanCodeCrafting",
            "user_id": 3,
        },
        {
            "title": "Crafting the Future of AI",
            "content": "Innovation through coding! Explored the realms of artificial intelligence, "
            "crafting models that simulate human-like thinking. "
            "The future of AI is now! 🤖🌐 #AIFutureCrafting",
            "user_id": 4,
        },
        {
            "title": "Challenges in Software Scalability",
            "content": "Tackling the challenges of software scalability! Delved into strategies "
            "for scaling applications and ensuring seamless user experiences. "
            "Scaling to new heights in the world of software! "
            "🚀 #SoftwareScalingChallenges",
            "user_id": 5,
        },
        {
            "title": "Microservices Architecture Adventure",
            "content": "Adventures in the world of microservices! Explored the architecture "
            "of microservices, enhancing the agility and efficiency of software systems. "
            "Microservices, macro-impact! 🏗️ #MicroservicesAdventure",
            "user_id": 6,
        },
        {
            "title": "Balancing Code with Nature",
            "content": "Finding the balance between code and nature! Took a coding hiatus "
            "to reconnect with the tranquility of the natural world. "
            "Nature's inspiration for coding brilliance! 🌳💻 #CodingBalanceWithNature",
            "user_id": 7,
        },
        {
            "title": "Serverless Transformation Journey",
            "content": "Navigating the waves of serverless computing! Explored the landscape "
            "of serverless architecture, transforming the way applications are developed "
            "and deployed. Riding the serverless wave! 🌊 #ServerlessTransformation",
            "user_id": 8,
        },
        {
            "title": "Adventure in Bug Cracking",
            "content": "Cracking the code of elusive bugs! Successfully debugged complex issues, "
            "unraveling the mysteries behind software malfunctions. "
            "Every bug conquered is a victory! 🐞💻 "
            "#BugCrackingAdventure",
            "user_id": 9,
        },
        {
            "title": "Dive into Assembly Language Programming",
            "content": "Diving into the realm of low-level programming! Explored the intricacies "
            "of assembly language, understanding the language of machines. "
            "Coding at the core! 💻 #LowLevelProgrammingDive",
            "user_id": 10,
        },
        {
            "title": "Celebrating Coding Triumphs",
            "content": "Celebrating coding triumphs! Successfully optimized critical sections "
            "of code, unlocking new levels of efficiency and performance. "
            "The coding journey continues! ⚙️🎉 #CodingTriumphCelebration",
            "user_id": 1,
        },
        {
            "title": "Elevation in Coding Community",
            "content": "Engaging in coding community dynamics! Joined an active coding community, "
            "contributing insights and gaining inspiration. "
            "Together, we elevate the coding experience! 👩‍💻👨‍💻 #CodingCommunityElevation",
            "user_id": 2,
        },
        {
            "title": "Mastery in Code Craftsmanship",
            "content": "Mastering the art of code craftsmanship! Adhering to clean code principles "
            "for maintainability and scalability. "
            "What's your favorite code crafting technique? 💻🌟 "
            "#CodeCraftsmanshipMastery",
            "user_id": 3,
        },
        {
            "title": "Pioneering AI Frontiers",
            "content": "Pioneering AI frontiers! Explored cutting-edge artificial intelligence "
            "models, shaping the future of intelligent systems. "
            "AI innovation at its finest! 🤖🚀 #AIFrontierPioneering",
            "user_id": 4,
        },
        {
            "title": "Scaling Software Architecture Heights",
            "content": "Scaling the heights of software architecture! Tackled challenges "
            "in software scalability, ensuring robust applications and enhanced user "
            "experiences. Scaling toward new horizons! 🚀 #SoftwareArchitectureScaling",
            "user_id": 1,
        },
    ]

    posts = [
        Post(
            title=post_data["title"],
            content=post_data["content"],
            user_id=post_data["user_id"],
        )
        for post_data in posts_data
    ]
    return posts


def populate_database():
    with app.app_context():
        # Sanitize the database by dropping all tables and creating fresh ones
        db.drop_all()
        db.create_all()

        # Create users
        users = create_users()
        db.session.add_all(users)

        # Create posts for users
        posts = create_posts(users)
        db.session.add_all(posts)

        # Commit the changes
        db.session.commit()


if __name__ == "__main__":
    # Ensure you're in the app context
    app = create_app(Config)
    populate_database()
