#  Patients Survey Testing.MD

[Back to README.md](<#  Patients Survey>)

## [PAGE CONTENTS](#page_contents)

 * [Testing User Stories](#testing_user_stories)
 * [Code Validation](#code_validation)
 * [Additional Testing](#additional_testing)
 * [Known Bugs](#known_bugs)


 ## Testing Using Stories

  1. As a Site User, I want to access the home page straight away, so that I can immediately view the site's key information. [#2](https://github.com/benjackson3811/pp4_medical_survey/issues/2)

 ### ACCEPTANCE CRITERIA
 [&check;] Home Page visible on opening
 [&check;] Site's key information, call to arms, navigation, log on and sign up clearly visible.
 [&check;] No error message stopping access


 2. As a Site User, I want to be able to navigate the website, so that I can view information on different parts of the website [#3](https://github.com/benjackson3811/pp4_medical_survey/issues/3)

 ### ACCEPTANCE CRITERIA
 [&check;] Fixed Navbar on top of the webpage
 [&check;] Working links
 [&check;] Clear Descriptions

 3. As a Site User, I want to be able to create a user account, so that I can sign up for the medical survey  [#4](https://github.com/benjackson3811/pp4_medical_survey/issues/4)

 ### ACCEPTANCE CRITERIA
 [&check;] Able to create a user account.
 [&check;] Add User details (Name, mobile number email address).
 [&check;] Can not sign in without valid username and/ or password.

 4. As a Site User, I want to be able to Log in to my account, so that I can View, edit or delete information on my account.  [#5](https://github.com/benjackson3811/pp4_medical_survey/issues/5)

 ### ACCEPTANCE CRITERIA
 [&check;] Able to log in with Username and password
 [&check;] Able to access account.
 [&check;] Can not sign in without valid username and/ or password.

 5. As a Site User, I want to be able to log out of my account, so that I can leave my account safely.  [#6](https://github.com/benjackson3811/pp4_medical_survey/issues/6)

 ### ACCEPTANCE CRITERIA
 [] Confirmed log out message /alert or notification.

 6. As a Site User, I want to add my patient data, so that I can sign up for the medical survey  [#7](https://github.com/benjackson3811/pp4_medical_survey/issues/7)

 ### ACCEPTANCE CRITERIA
 [&check;] Complete form with personal data (first name, last name, DOB etc).
 [&check;] Be able to schedule an appointment for a further appointment. ( on a valid time and day, when there isn't another appointment).
 [&check;] Be alerted if any of the data added is incorrect (ie email address with a @)

 7. As a Site User, I want to get a view screen before confirmation , so that I can confirm the accuracy of my data inputted into the form.  [#8](https://github.com/benjackson3811/pp4_medical_survey/issues/8)

### ACCEPTANCE CRITERIA
 [] Before confirmation. Get a notification screen asking if the data inputted into the form is correct.

8. As a Site User, I want to have the ability to make changes/ update patient data, so that I can ensure it is correctly added and updated.  [#9](https://github.com/benjackson3811/pp4_medical_survey/issues/9)

### ACCEPTANCE CRITERIA
 [] Ability to edit typed input data.
 [] Ability to edit Appointment date and time
 [] Clearly marked edit buttons on key details form.

 9. As a Site User, I want to get an email confirmation confirming data has been added/ edited/ deleted, so that I can have awareness of the change  [#10](https://github.com/benjackson3811/pp4_medical_survey/issues/10)

 ### ACCEPTANCE CRITERIA
 [] Receiving a change email notification.

10. As a Site admin, I want to be able to view a list of patients, so that I can have awareness of the size of the survey [#11](https://github.com/benjackson3811/pp4_medical_survey/issues/11)

### ACCEPTANCE CRITERIA
 [&check;] Being able to see and search for the patients recruited.

11. As a Site User, I want to *be able to search for inputted patients, so that I can access their details. [#12](https://github.com/benjackson3811/pp4_medical_survey/issues/12)

### ACCEPTANCE CRITERIA
 [] Have Search functionality.
 [] No errors stopping data from getting the details/
 [] Getting correct data back in the search.

 12. As a Site User, I want to be able to delete incorrectly added data, so that I can ensure correct data is added to survey  [#13](https://github.com/benjackson3811/pp4_medical_survey/issues/13)

 ### ACCEPTANCE CRITERIA
 [] A delete button.
 [] Notification to user to confirm they want this action to be completed.

 13. As a Site Admin, I want to be able to approve which patient data is deleted, so that I can ensure there is an audit trail. [#14](https://github.com/benjackson3811/pp4_medical_survey/issues/14)

 ### ACCEPTANCE CRITERIA
 [] Patient Details arent automatically deleted.
 [] Site Admin has finally approval


[Back to Top](#page_contents)

 ## Additional Testing
[Back to Top](#page_contents)

In addition to tests stated above I have performed a series of manual tests. Below the list of tests that has been conducted can be found.

| Status | **Home Page - User Logged Out**
|:-------:|:--------|

| Status | **Main Website - User Logged In**
|:-------:|:--------|

| Status | **Main Website - Admin Logged In**
|:-------:|:--------|

 Status | **Create A Patient  - User Logged In**
|:-------:|:--------|

Status | **Create A New User - User Logged Out**
|:-------:|:--------|

### Automated Testing
None were completed

### Responsiveness Test
The responsive design tests were carried out manually with [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/) and [Responsive Design Checker](https://www.responsivedesignchecker.com/).

| Desktop    | Display <1280px       | Display >1280px    |
|------------|-----------------------|--------------------|
| Render     |                   |                |
| Images     |                   |                |
| Links      |                   |                |

### Browser Compatibility

### Lighthouse

### WAVE

 ## Fixed Bugs
1. IntegrityError at /add_appointment duplicate key value violates unique constraint "appointments_appointment_slug_key"
DETAIL:  Key (slug)=() already exists.
https://stackoverflow.com/questions/46498168/duplicate-key-value-violates-unique-constraint-auth-user-username-keydetail-k
2. Django/Python: Tried to update field with a model instance. Use a value compatible with CharField
https://stackoverflow.com/questions/38936573/django-python-tried-to-update-field-with-a-model-instance-use-a-value-compatib

 [Back to Top](#page_contents)

 ## Unfixed Bugs
 [Back to Top](#page_contents)

  ## Code Validation
- HTML
- CSS
- JShint
- Python linter

[Back to Top](#page_contents)