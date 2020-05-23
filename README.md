# PORTFOLIO API

Django REST API backend for portfolio page deployed on Heroku.

## What is it?

This is a Django REST application to provide models for an SQL-based database (in my case, PostgreSQL). 

## Contents

### Authentication and Authorisation

This contains Django Admin's User and Group model and is used to provide authentication so only I can edit or delete model instances, as this is the backend for my personal portfolio page. 

_That doesn't mean that you're not allowed to Fork this repo and use it for your own project. You will need to link up a database of your own and run the superuser command ```python manage.py createsuperuser``` to create an account with permissions for your own use. Please to refer back to this repo in your README.md if you do. Thank you._

### Code Projects

Contains the models Language and Projects, which are linked together through the model ProjectLanguage. 

Every instance of ProjectLanguage must be unique, that is to say: a coding language can only be added to a project once or vice versa. This is to prevent accidentally adding the same language or framework multiple times in the same project. 

Additionally, the Language model contains the name, logo and official URL for each instance.

The Project model contains a bit more information, to be specific:
- the title of the project
- the live link, aka the URL where the page is deployed, so a visitor to the portfolio can visit the page
- the code link, aka the Github URL where the code is stored, like this one where you're currently reading this README
- a preview image, for display purposes
- the type of project: a choice field with the following options:
  - Tutorial
  - Graded Coursework
  - Individual project
  - Commission
 - the course this project is linked to. This field is not required. The model uses a foreign key to link to the relevant course if applicable
 - a short description of the project. If you're thinking of using this project, you'll be using this textbox to "pitch" your project.
 
### Education
 
This app only contains one model: Course.
 
The Course model contains the following information:
- the course name
- the name of the school
- the URL for the school's website
- a boolean field to indicate whether or not there is a certificate for the course mentioned
- a non-required field for the certificate image if applicable
- date finished (aka graduation date) which is a DateField
- a short description of the course
 
### Experience
 
As the name says, this is where my work experience is stored, in the Job model. I also included a choice field in here for the type of job, including volunteer work and internships, which will be used for filtering on the front-end side.

Apart from the aforementioned type choice field, the Job model also contains:
- the job title
- the name of the company
- the URL of the company website
- the company logo (not required, in case none is available to display)
- the description
- start date
- end date (not required, in case this is the current job)
- a boolean field to indicate whether or not the job is code-related. This will also be used for filtering on the front-end side.

### Hobbies

As the name indicates, this is where the details are saved for other hobbies and interests. In other words: what do I do when I'm not actually working or coding. As in Education and Experience, this also contains only one model: Hobby. This model is also pretty straight-forward, it only contains three fields:
- the name
- an image for display purposes
- a description field to add some more information
