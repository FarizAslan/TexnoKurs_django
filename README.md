#TexnoCourse
TexnoCourse is a full-stack website written in Python/Django that allows users to enroll, delete, pay, and write comments for various courses. The website also features a keyword and tag filtering system, as well as a robust authentication function.

##Technologies Used
The TexnoCourse website was built using the following technologies:

Python (3.9.5)
Django (3.2.6)
SQLite3
HTML
CSS
Bootstrap
JavaScript
Jazzmin (Django Admin customization package)
Features
The TexnoCourse website offers the following features:

User authentication and registration
Course enrollment, deletion, and payment
Commenting system
Keyword and tag filtering system
Responsive design
Customized admin panel using the Jazzmin package
Getting Started
To get started with TexnoCourse, you'll need to have Python and Django installed on your computer. Once you've cloned the repository, navigate to the project directory and run the following command:

##Copy code
python manage.py runserver
This will start the development server, and you can access the website by navigating to http://localhost:8000/ in your web browser.

##File Structure
The TexnoCourse website has the following file structure:

texnocourse/
├── texnocourse/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── courses/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── ...
├── templates/
│   ├── base.html
│   ├── course_detail.html
│   ├── course_list.html
│   └── ...
└── ...
The texnocourse/ directory contains the main settings and URL configuration for the project. The courses/ directory contains the models, views, and admin configuration for the courses app. The templates/ directory contains the HTML templates used to render the website.

##Contributing
If you'd like to contribute to TexnoCourse, please fork the repository and create a new branch for your changes. Once you've made your changes, submit a pull request for review.

##Credits
The TexnoCourse website was developed FarizAslan.
