# drf_squibler_assessment

## Setting up the Django Project

1. Clone the repo
2. In the project directory, create a local pipenv environment using "python -m pipenv install". Then activate it by "python -m pipenv shell".
3. Install the requirements by running "pip install -r requirements.txt"
4. Test if the project is running by running "python manage.py runserver"

## Creating, Adding, and Viewing Data

1. In the terminal, run "python manage.py createsuperuser" and follow the steps to create a user.
2. Repeat this again so now we have 2 users.
3. Go to http://localhost:8000/ where our development server is running, it will tell you that you are not authenticated to view the data.
4. Login from the top right corner of the screen. We are now viewing the list API.
5. At the bottom, we can add a new section. Once added, it gets inserted into our DB and appears in the list of possible parents if we want to create a subsection. To create a new main section, leave parent as null.
6. To view the details of a particular section (or subsection), add the slug to the end of the list API's url (so for a section who's slug is section-1, that would be http://localhost:8000/section-1). The section can be updated as well from here. 

## User Separation and BUG
1. Now logout and login again with the second user's credentials. The list API will be empty at first as no sections have been made against this user. The above process can be repeated for adding sections. The only bug in this part is that when the dropdown for assigning a parent is opened, it shows **all** sections from the DB, instead of only the ones against this user. This is confusing as the queryset for this view has been filtered according to the user. It can probably be overcome by creating a separate view for the create/update requests  and pointing them to a custom template which appropriately filters the queryset so that the dropdown doesn't show all the sections.

## Frontend
1. A barebones, skeletal frontend for the list API built on React can be accessed. For this, first close the server by pressing ctrl+c. Now, run "npm install" in the frontend directory, then run "npm install" again in the root directory. Then, in the main django project directory run "python manage.py runserver react". The list API can be seen at http://localhost:8000/frontend/
