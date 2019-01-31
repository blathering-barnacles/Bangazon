# BangazonAPI

This is an API for Bangazon INC. This API will allow user to GET/POST/PUT and (sometimes) DELETE items from the Bangazon Database. Before you can utilize the database, there are a few things you need to make sure you have installed.

# Installing Core Technologies

## 1. SQLite

### For OSX Users

```
brew install sqlite
```

### For Windows Users

Visit the [SQLite downloads](https://www.sqlite.org/download.html) and download the 64-bit DLL (x64) for SQLite version, unzip and install it.

## 2. SQL Browser

The [DB browser for SQLite](http://sqlitebrowser.org/) will let you view, query and manage your databases for this project.

## 3. Visual Studio Code

[Visual Studio Code](https://code.visualstudio.com/download) is Microsoft's cross-platform editor that you can use to view Python and Django code.

# Setting up environment and installing dependencies

## 1. Set up your virtual environment

Within the terminal, navigate to the location where you'd like to create the new environment and Bangazon project. Create a folder called BangazonProject and navigate within the new folder. Then, enter this text to create the new environment:
```
virtualenv ENV
```
Then activate your environment:
```
source ENV/bin/activate
```
Note that you can type "deactivate" to end the new environment at any time.

## 2. Install Django

Within your new BangazonProject folder, download the Django code by typing:
```
pip install django
```

## 3. Download the Bangazon project

Within your new BangazonProject project folder, download the source code by typing:
```
git clone https://github.com/blathering-barnacles/Bangazon.git
```

## 4. Starting the project server

After downloading the Banagzon project, you should have a new folder within the BangazonProject folder that you created. The new folder will also be called Bangazon.  Navigate within this folder.  Start the server by typing:
```
python manage.py runserver
```

## 5. Navigate to the Bangazon workforce webpage

Within your web browser, navigate to http://localhost:8000/workforce/  From here, you should see the main links for the Bangazon workforce application.


# Creating the Bangazon DB

While inside the BangazonProject/Bangazon folder, enter this command:
```
python manage.py makemigrations Workforce
```
Then enter
```
python manage.py migrate
```
You now have a database named sqlite3.sql within your existing folder.  Use the DB Browser for SQLite to open the new database.

### Employees

* GET You can access a list of all employees by running a Get call to `http://localhost:8000/employees`
* GET one You can get the information on a single employee by runnning a Get call to `http://localhost:8000/employees/{employeeID}`
>Note you need to have a valid employee unique ID number to get the correct information

* POST You can enter a new employee by running a Post call to `http://localhost:8000/addEmployee`

    * You must put a `firstName`, `lastName`, `startDate`, `isSupervisor` and `department` with the Post.
    * Example: `{'firstName': 'Bill', 'lastName': 'Ryland', 'startDate': '2018-01-02', 'isSupervisor': '1', 'department': '1'}`
    * Note that there must be at least one Department in the department table in order for the POST to work.

### Departments

* GET You can access a list of all departments by running a Get call to `http://localhost:8000/departments`
* GET one. You can get the information on a single department by runnning a Get call to `http://localhost:8000/departmentDetail/{departmentID}`
>Note you need to have at least one department unique ID number to get the correct information

* You can update the info on a specific department by running a POST call to `http://localhost:8000/department/{departmentID}`
    * Running a Put requires that you submit the entire object.
    * Example: `{ "departmentID": 1, "name": "Professional Services", "budget": 200000 }`

* POST You can enter a new payment type by running a Post call to `http://localhost:8000/addDepartment`
    * You must put a `name` and `budget` with a Post.
    * Example: `{ "name": "Professional Services", "budget": 100 }`

### Training Programs

* GET You can access a list of all training programs by running a Get call to `http://localhost:8000/trainingprogram`
* GET one. You can get the information on a single training program by runnning a Get call to `http://localhost:8000/trainingprogram/{trainingprogramID}`
>Note you need to have a training program unique ID number to get the correct information

* PUT You can update the info on a specific training program by running a Put call to `http://localhost:8000/trainingprogram/{trainingprogramID}`
    * Running a Put requires that you submit the entire object.
    * Example: `{ "trainingProgramID": 1 "dateStart": "02-14-2018", "dateEnd": "02-15-2018", "maxAttendees": 50 }`

* DELETE You can delete a training program by running a Delete call to `http://localhost:8000/trainingprogram{trainingprogramID}`
>Note - you can only delete a training program if the current date is before the start date of a program. You cannot delete programs that have already happened.

* POST You can enter a new training program by running a Post call to `http://localhost:8000/trainingProgram`
    * You must put a `name`, `dateStart`, `dateEnd`, and `maxAttendees` with a Post.
    * Example: `{ "name": "Learning Vim", "dateStart": "02-14-2018", "dateEnd": "10-15-2018", "maxAttendees": 50 }`

## Unit Testing

Navigate within the BangazonProject/Bangazon project and enter this command:
```
python manage.py test
```

This will run all of the Unit Testing files created within the BangazonProject/Bangazon/bangazon_1/workforce/tests folder.



Bangazon was created by the Blathering Barnacles - Cohort 28:

[Jessica Barnett](https://github.com/jessicabarnett8219)

[Alfonzo Miranda](https://github.com/Kazathur92)

[Sam Webber](https://github.com/buffard)

[Dillon Williams](https://github.com/CosignMyCodesign)

[Richard Lancaster](https://github.com/rjlancaster)