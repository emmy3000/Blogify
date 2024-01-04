#!/usr/bin/env python3

"""
Script to populate the database with dummy users and posts
for the project's initial data.
"""

# Import necessary modules and models
from blogify_app import db, create_app, User, Post
from blogify_app.config import Config

# Ensure you're in the app context
app = create_app(Config)

with app.app_context():
    # Sanitize the database by dropping all tables and creating fresh ones
    db.drop_all()
    db.create_all()

    # Create additional users representing various nations
    user_1 = User(
        firstname="Emeka",
        lastname="Emodi",
        username="mex619",
        email="emodiemeka@gmail.com",
        password="password",
    )
    user_2 = User(
        firstname="Olivia",
        lastname="Juma",
        username="sweet_olive100",
        email="olivia@example.com",
        password="password",
    )
    user_3 = User(
        firstname="Mousa",
        lastname="Diop",
        username="mdiop2real",
        email="moussa@example.com",
        password="password",
    )
    user_4 = User(
        firstname="Lerato",
        lastname="Ndlovu",
        username="terra.lera3000",
        email="lerato@example.com",
        password="password",
    )
    user_5 = User(
        firstname="Abdul",
        lastname="Kadir",
        username="gentle_abdul",
        email="abdul@example.com",
        password="password",
    )
    user_6 = User(
        firstname="Mariam",
        lastname="Ejeh",
        username="queen_mariam_d_first",
        email="mariam@example.com",
        password="password",
    )
    user_7 = User(
        firstname="Anna",
        lastname="Schmidt",
        username="pretty-anna10",
        email="anna@example.com",
        password="password",
    )
    user_8 = User(
        firstname="Carlos",
        lastname="Gutierrez",
        username="carlosGstylo",
        email="carlos@example.com",
        password="password",
    )
    user_10 = User(
        firstname="Ikenna",
        lastname="Okafor",
        username="ikemann808",
        email="ikenna@example.com",
        password="password",
    )
    user_9 = User(
        firstname="Adien",
        lastname="O'Connor",
        username="doc_connoz",
        email="aiden@example.com",
        password="password",
    )

    # Add users to the session
    db.session.add_all(
        [
            user_1,
            user_2,
            user_3,
            user_4,
            user_5,
            user_6,
            user_7,
            user_8,
            user_9,
            user_10,
        ]
    )
    db.session.commit()

    # Create sample posts for users
    post_content_1 = "I'm excited to start my blogging journey with just two simple words... " \
                     "Hello World!"
    post_1 = Post(
        title="My First Blog Post",
        content=post_content_1,
        user_id=1
    )

    post_content_2 = "Delving into the intricacies of Python magic! Discovered the elegance " \
                     "of list comprehensions and their impact on code readability. " \
                     "Magical coding at its finest! ✨ #PythonElegance"
    post_2 = Post(
        title="Exploring Python Elegance",
        content=post_content_2,
        user_id=1
    )

    post_content_3 = "Embarking on a journey through the vast landscapes of machine learning. " \
                     "Today, I trained my first neural network to recognize patterns in data. " \
                     "The power of AI is truly awe-inspiring! 🤖 #MachineLearningOdyssey"
    post_3 = Post(
        title="Journey into Machine Learning",
        content=post_content_3,
        user_id=3
    )

    post_content_4 = "Navigating the labyrinth of code review! Shared my latest project " \
                     "with the team, and the collaborative effort led to the creation of a robust " \
                     "and error-free masterpiece. " \
                     "Code review adventures continue! 💻🚀 #CodeReviewMasterpiece"
    post_4 = Post(
        title="Code Review Masterpiece",
        content=post_content_4,
        user_id=4
    )

    post_content_5 = "Crafting the foundations of a web empire! Explored the latest front-end " \
                     "frameworks and their influence on user experience. Every line of code " \
                     "is a step toward web development excellence! 🌐 #WebEmpireCrafting"
    post_5 = Post(
        title="Web Development Excellence",
        content=post_content_5,
        user_id=5
    )

    post_content_6 = "Architecting scalable systems for the future! Explored the principles " \
                     "of microservices architecture and its impact on large-scale applications. " \
                     "Designing the future of software systems! 🏗️ #FutureSystemsDesign"
    post_6 = Post(
        title="Future-Ready Systems Architecture",
        content=post_content_6,
        user_id=1
    )

    post_content_7 = "Finding inspiration in the serenity of nature! Took a coding break " \
                     "to absorb the beauty of the great outdoors. A moment of tranquility " \
                     "before diving back into the algorithmic storm! 🌲 #NatureCodingInspiration"
    post_7 = Post(
        title="Coding Amidst Nature",
        content=post_content_7,
        user_id=7
    )

    post_content_8 = "Adapting to the revolutionary era of the cloud! Explored serverless " \
                     "computing and its transformative impact on modern application development. " \
                     "Sky's not the limit; it's the beginning! ☁️ #CloudRevolution"
    post_8 = Post(
        title="Embracing Serverless Computing",
        content=post_content_8,
        user_id=8
    )

    post_content_9 = "Embarking on debugging adventures! Tackled a formidable bug today, " \
                     "unraveling its mysteries through careful code dissection. " \
                     "Every bug conquered is a step toward coding mastery! 🐞💡 #DebuggingMastery"
    post_9 = Post(
        title="Mastery in Debugging",
        content=post_content_9,
        user_id=9
    )

    post_content_10 = "Deciphering the language of machines! Explored the nuances of assembly " \
                      "language programming, unraveling the simplicity of machine instructions. " \
                      "A coding journey to the core! 💻 #AssemblyLanguageJourney"
    post_10 = Post(
        title="Journey in Assembly Language",
        content=post_content_10,
        user_id=10
    )

    post_content_11 = "Reflecting on a triumphant coding feat! Successfully optimized a critical " \
                      "section of my code, unlocking new levels of efficiency. " \
                      "The pursuit of coding excellence knows no bounds! " \
                      "⚙️🚀 #CodingExcellenceReflection"
    post_11 = Post(
        title="Reflection on Coding Excellence",
        content=post_content_11,
        user_id=1
    )

    post_content_12 = "Immersing in community-driven coding! Joined a vibrant coding community " \
                      "and engaged in insightful discussions. Collaboration fuels innovation, " \
                      "and the coding journey becomes richer! 👩‍💻👨‍💻 #CommunityDrivenCoding"
    post_12 = Post(
        title="Community-Driven Coding Immersion",
        content=post_content_12,
        user_id=2
    )

    post_content_13 = "Crafting elegant and maintainable code! Embracing clean code principles " \
                      "to ensure scalability and ease of collaboration. " \
                      "What's your favorite code refactoring technique? 💻🌟 #CleanCodeCrafting"
    post_13 = Post(
        title="Crafting Elegant Code",
        content=post_content_13,
        user_id=3
    )

    post_content_14 = "Innovation through coding! Explored the realms of artificial intelligence, " \
                      "crafting models that simulate human-like thinking. " \
                      "The future of AI is now! 🤖🌐 #AIFutureCrafting"
    post_14 = Post(
        title="Crafting the Future of AI",
        content=post_content_14,
        user_id=4
    )

    post_content_15 = "Tackling the challenges of software scalability! Delved into strategies " \
                      "for scaling applications and ensuring seamless user experiences. " \
                      "Scaling to new heights in the world of software! 🚀 #SoftwareScalingChallenges"
    post_15 = Post(
        title="Challenges in Software Scalability",
        content=post_content_15,
        user_id=5
    )

    post_content_16 = "Adventures in the world of microservices! Explored the architecture " \
                      "of microservices, enhancing the agility and efficiency of software systems. " \
                      "Microservices, macro-impact! 🏗️ #MicroservicesAdventure"
    post_16 = Post(
        title="Microservices Architecture Adventure",
        content=post_content_16,
        user_id=6
    )

    post_content_17 = "Finding the balance between code and nature! Took a coding hiatus " \
                      "to reconnect with the tranquility of the natural world. " \
                      "Nature's inspiration for coding brilliance! 🌳💻 #CodingBalanceWithNature"
    post_17 = Post(
        title="Balancing Code with Nature",
        content=post_content_17,
        user_id=7
    )

    post_content_18 = "Navigating the waves of serverless computing! Explored the landscape " \
                      "of serverless architecture, transforming the way applications are developed " \
                      "and deployed. Riding the serverless wave! 🌊 #ServerlessTransformation"
    post_18 = Post(
        title="Serverless Transformation Journey",
        content=post_content_18,
        user_id=8
    )

    post_content_19 = "Cracking the code of elusive bugs! Successfully debugged complex issues, " \
                      "unraveling the mysteries behind software malfunctions. " \
                      "Every bug conquered is a victory! 🐞💻 " \
                      "#BugCrackingAdventure"
    post_19 = Post(
        title="Adventure in Bug Cracking",
        content=post_content_19,
        user_id=9
    )

    post_content_20 = "Diving into the realm of low-level programming! Explored the intricacies " \
                      "of assembly language, understanding the language of machines. " \
                      "Coding at the core! 💻 #LowLevelProgrammingDive"
    post_20 = Post(
        title="Dive into Assembly Language Programming",
        content=post_content_20,
        user_id=10,
    )

    post_content_21 = "Celebrating coding triumphs! Successfully optimized critical sections " \
                      "of code, unlocking new levels of efficiency and performance. " \
                      "The coding journey continues! ⚙️🎉 #CodingTriumphCelebration"
    post_21 = Post(
        title="Celebrating Coding Triumphs",
        content=post_content_21,
        user_id=1
    )

    post_content_22 = "Engaging in coding community dynamics! Joined an active coding community, " \
                      "contributing insights and gaining inspiration. " \
                      "Together, we elevate the coding experience! 👩‍💻👨‍💻 #CodingCommunityElevation"
    post_22 = Post(
        title="Elevation in Coding Community",
        content=post_content_22,
        user_id=2
    )

    post_content_23 = "Mastering the art of code craftsmanship! Adhering to clean code principles " \
                      "for maintainability and scalability. " \
                      "What's your favorite code crafting technique? 💻🌟 #CodeCraftsmanshipMastery"
    post_23 = Post(
        title="Mastery in Code Craftsmanship",
        content=post_content_23,
        user_id=3
    )

    post_content_24 = "Pioneering AI frontiers! Explored cutting-edge artificial intelligence " \
                      "models, shaping the future of intelligent systems. " \
                      "AI innovation at its finest! 🤖🚀 #AIFrontierPioneering"
    post_24 = Post(
        title="Pioneering AI Frontiers",
        content=post_content_24,
        user_id=4)

    post_content_25 = "Scaling the heights of software architecture! Tackled challenges " \
                      "in software scalability, ensuring robust applications and enhanced user " \
                      "experiences. Scaling toward new horizons! 🚀 #SoftwareArchitectureScaling"
    post_25 = Post(
        title="Scaling Software Architecture Heights",
        content=post_content_25,
        user_id=1,
    )

    # Add posts to the session
    db.session.add_all(
        [
            post_1,
            post_2,
            post_3,
            post_4,
            post_5,
            post_6,
            post_7,
            post_8,
            post_9,
            post_10,
            post_11,
            post_12,
            post_13,
            post_14,
            post_15,
            post_16,
            post_17,
            post_18,
            post_19,
            post_20,
            post_21,
            post_22,
            post_23,
            post_24,
            post_25,
        ]
    )

    # Commit the newly created posts to the database
    db.session.commit()
