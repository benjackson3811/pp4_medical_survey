#  Patients Survey

[Website image]()
---

## [CONTENTS](#table_of_contents)

 * [Object_of_the_website](#object-of-the-website)

* [UX](#UX)
  * [Target Audience](#target-audience)
  * [User Stories](#user-stories)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [Wireframes](#wireframes)

* [Features](#features)
  * [Home Page](#home_page)
  * [Navigation](#navigation)
  * [Registration](#registration)
  * [Login](#login)
  * [Logout](#logout)
  * [Future Implementations](#future-implementations)
  

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)
  * [Local Development](#local-development)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)

* [Testing](#testing)

* [Credits](#credits)
  * [Code Used](#code-used)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)

---

## Object of the Website

Patients Survey is a responsive website for a fictional medical survey. It allows the user to view inputted patient details, view a list of appointments and make appointments for a patient’s repeat visit.

The app has two purposes 
An online repository for storing patient details who have signed up for a survey. 
A booking tool for follow up appointments for the survey.

The users will be able to;
- View, make/ edit/ delete an account.
- View, input / edit the patient details who have been recruited,
- View, input / edit/ delete their follow up appointment scheduled for them to return 3 months later. 

[Back to Top](#table_of_contents)

## UX

### Target audience

The primary users of the survey of the planner will be;

Medical Professionals.
- Will need an account .
- To input/ edit/ update the participant data if they are on the survey.
- To contact the participant.
- Check daily appointments.
- Schedule appointments for their visits.
- Validate the data.
- Receive notification of change.

Secondart Users

Participant, 
- Will need a notification of their data if they are on the survey.
- They will;
  - Receive notification of change.
  - Validate the data.

Data Scientist/ Researcher.
- Will need an output to;
-View the participant data if they are on the survey.
- Export the data.
-To analysis/ view trends

[Back to Top](#table_of_contents)

### User Stories

  1. As a Site User, I want to access the home page straight away, so that I can immediately view the site's key information. [#2](https://github.com/benjackson3811/pp4_medical_survey/issues/2)
  2. As a Site User, I want to be able to navigate the website, so that I can view information on different parts of the website [#3](https://github.com/benjackson3811/pp4_medical_survey/issues/3)
  3. As a Site User, I want to be able to create a user account, so that I can sign up for the medical survey  [#4](https://github.com/benjackson3811/pp4_medical_survey/issues/4)
  4. As a Site User, I want to be able to Log in to my account, so that I can View, edit or delete information on my account.  [#5](https://github.com/benjackson3811/pp4_medical_survey/issues/5)
  5. As a Site User, I want to be able to log out of my account, so that I can leave my account safely.  [#6](https://github.com/benjackson3811/pp4_medical_survey/issues/6)
  6. As a Site User, I want to add my patient data, so that I can sign up for the medical survey  [#7](https://github.com/benjackson3811/pp4_medical_survey/issues/7)
  7. As a Site User, I want to get a view screen before confirmation , so that I can confirm the accuracy of my data inputted into the form.  [#8](https://github.com/benjackson3811/pp4_medical_survey/issues/8)
  8. As a Site User, I want to have the ability to make changes/ update patient data, so that I can ensure it is correctly added and updated.  [#9](https://github.com/benjackson3811/pp4_medical_survey/issues/9)
  9. As a Site User, I want to get an email confirmation confirming data has been added/ edited/ deleted, so that I can have awareness of the change  [#10](https://github.com/benjackson3811/pp4_medical_survey/issues/10)
 10. As a Site admin, I want to be able to view a list of patients, so that I can have awareness of the size of the survey [#11](https://github.com/benjackson3811/pp4_medical_survey/issues/11)
 11. As a Site User, I want to *be able to search for inputted patients, so that I can access their details. [#12](https://github.com/benjackson3811/pp4_medical_survey/issues/12)
 12. As a Site User, I want to be able to delete incorrectly added data, so that I can ensure correct data is added to survey  [#13](https://github.com/benjackson3811/pp4_medical_survey/issues/13)
 13. As a Site Admin, I want to be able to approve which patient data is deleted, so that I can ensure there is an audit trail. [#14](https://github.com/benjackson3811/pp4_medical_survey/issues/14)

The user stories are further detailed in the [TESTING.md](TESTING.MD). The user acceptance criteria is defined.

Please note the numbering of the user stories does not match the user story in GitHub. This is due to the first user story being created in error. 
[Back to Top](#table_of_contents)

### colour-scheme
![Coolors Colour Scheme](/static/images/readme_images/coolors_color_schema.png)

Generated through [Coolors](https://coolors.co/) the colour picked in the palette are accessible, bold and work well together. They allow the website user to easily read and understand the writen information. 

[Back to Top](#table_of_contents)

### Typography

Open Sans: chosen as primary font because its is clear and elegant. The typed letters are easy to read.

Raleway: chosen for headings because it pairs well with the Caveat font.

### Imagery

Imagery of the site is from [Pexels](https://www.pexels.com/). 

![stethoscope](/static/images/stethoscope.png)

The Stethoscope picture was taken because it is a common image of going to the doctors. With the forms beneath the image this allows the reader a visual queue of them going to dcotors and getting their details collected.

[Back to Top](#table_of_contents)

### Wireframes

[Back to Top](#table_of_contents)

### ERP Database model

[Back to Top](#table_of_contents)

## Languages and libraries used

### Languages

The languages used in this project are:

- [HTML](https://www.w3schools.com/html/)
- [CSS](https://www.w3.org/Style/CSS/Overview.en.html)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Python](https://www.python.org/)

[Back to Top](#table_of_contents)

### Libraries and other resources

- [Django](https://www.djangoproject.com/) Django is a high-level Python web framework
- [Flask](https://flask.palletsprojects.com/en/2.2.x/): Flask is a Python-based web application framework tool designed to be lightweight, flexible and easy to use.
- [Figma](https://www.figma.com/): Figma is a web-based design and prototyping tool used for creating UI, desktop and mobile app designs.
- [Bootstrap](https://getbootstrap.com/): Bootstrap is a CSS library used to facilitate the design responsiveness of a web application and mobile-first web pages.
- [Google Fonts](https://fonts.google.com/): used to import font utilised throughout the site.
- [Font Awesome](https://fontawesome.com/): used for icons across website.
- [Gitpod](https://www.gitpod.io/) Acloud development environment
- [GitHub](https://github.com/): used to store, develop and maintain project code.
- [Heroku](https://dashboard.heroku.com/apps): a cloud-based platform that allows developers to store, manage and deploy web applications.
- [DBDiagram](https://dbdiagram.io/home): A Relational Database Diagram Design Tool.
- [Elephant SQL](https://www.elephantsql.com/) Postgres SQL as a Service.
- [Cloudinary](https://cloudinary.com/) Free Media Management System.
- [Coolors](https://coolors.co/) Online Colour Palette generator
- [Pexels](https://www.pexels.com/) Free stock photos.

[Back to Top](#table_of_contents)

### Deployment

---
- Development Environment - Github
    -  Regular commits and pushes to Github have been employed to be able to track and trace the development process of the website.

---
- Create app on heroku
    - Create heroku account or sign in
    - Click create new app in the top right corner
    - Give app a name and choose location nearest to you
    
- Attach the database
    - Click resources tab
    - Search for postgres and add heroku postgres

- Prepare your enviroment and settings.py
    - Click settings tab
    - Click reveal config vars
    - Copy adress to database
    - Add secret key variable from project
    - Create an env.py file
    - Add env.py file to gitignore
    - Create enviroment variables for database and secret key 
    - Attache heroku database as default in settings.py 
    - Add heroku app name in Allowed hosts ['bookings2022ci.herokuapp.com', 'localhost']
    - Create a procfile with content: web: gunicorn django_bookings.wsgi

- Get static and media files stored on cloudinary
    - Login/Register a Cloudinary account
    - Go to dashboard and copy API Enviroment variable
    - Add Cloudinary url to env.py (Delete prefix Cloudinary_url=)
    - Copy Cloudinary url in config vars in heroku settings
    - Add Config vars DISABLE_COLLECTSTATIC 1
    - Add Cloudinary_storage and Cloudinary to Installed apps in settings.py
    - Add these lines of code to settings.py
        - STATIC_URL = '/bookings/static/'

        - STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
        - STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
        - STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

        - MEDIA_URL = '/media/'
        - DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    - Add TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates') to settings.py
    - In TEMPLATTES  in settinggs.py add [TEMPLATES_DIR] to Dirs: field

- Deployment on Heroku
    - Click deployment tab
    - Connect github account
    - Search for repository
    - Click deploy branch

- Final deployment
    - DEBUG flag must be set to false in settings.py
    - Add X_FRAME_OPTIONS = 'SAMEORIGIN' to settings.py
    - Remove Disablestatic config var
    - Click deploy branch in deploy menu.

[Back to Top](#table_of_contents)

 ### Local Development
[Back to Top](#table_of_contents)

#### How to Fork
[Back to Top](#table_of_contents)

#### How to Clone
[Back to Top](#table_of_contents)

### Testing 
Please see [TESTING.md](TESTING.MD) for all testing performed
[Back to Top](#table_of_contents)

 ### Credits
 [Back to Top](#table_of_contents)

#### Code Used

- [I think therefore i Blog](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/b31493372e764469823578613d11036b/fe4299adcd6743328183aab4e7ec5d13/) - Introduction to Django walkthrough.
- [Dev Genuis](https://blog.devgenius.io/django-tutorial-on-how-to-create-a-booking-system-for-a-health-clinic-9b1920fc2b78)- Help with designing the booking system.
- [CSE Stack](https://www.csestack.org/create-html-form-insert-data-database-django/#Step_4_Create_Form_to_Take_the_User_Input) Creating a form in Django
- [Simple is better than Complex](https://simpleisbetterthancomplex.com/tutorial/2019/01/03/how-to-use-date-picker-with-django.html) How to use a date picker in Django
- [Codemy.com](https://www.youtube.com/watch?v=6-XXvUENY_8)-Style Django Forms With Bootstrap - Django Blog #5.
- [Djangoproject](https://docs.djangoproject.com/en/4.2/topics/email/)- Sending email through Django.
- [geeksforgeeks](https://www.geeksforgeeks.org/setup-sending-email-in-django-project/) - Tutorial for sending emails in a Django project.
- [QuestionPro](https://www.questionpro.com/blog/health-survey/#:~:text=A%20health%20survey%20is%20a,a%20community%20acts%20towards%20health.)Sample information on a health survey.
- [mdnweb docs](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/) - Used for details on the Authorisation and Forms 

[Back to Top](#table_of_contents)