# Vulnerability Report

Reviewer1: Chris Turner
Reviewer2: Andrew Baik
Date: Oct/10/2018


## A1. Injection
### Exposure
In the TaskManager app, there are two types of file uploads - profile pictures, and files related to projects. One type, the project files utilizes the  curs.execute() without any evaluation of the content. This allows attackers to run SQL queries without checking them first. 

### Repair
Check the users imput and sanatize it before allowing any code to run. 

## A2. Broken Auth
### Exposure
It includes an incomplete blacklist of the User model attributes that cannot be set via this form; is_superuser is not included. Due to this, an attacker could manually enable the is_superuser flag by appending it to the form prior to submitting it to the application.

### Repair
Ensure that the blacklist is complete and up-to-date to make sure people cannot register themselves as super users.

## A3. Cross Site Script
### Exposure
The application renders back a user's username (user-supplied data) by leveraging a call to the safe method within the view. This means the content will not be HTML encoded and will be interpreted as valid JS or HTML code.

### Repair
Remove the safe method within the backend/base.html and tutorials/base.html files. Consider setting X-XSS-Protection in your webserver configuration as well.

## A4. Insecure DOR
### Exposure
The view functions all fail to ensure the user is properly authorized to perform the action.
### Repair
Make sure the user is authorized to actually preform the function that they are requesting. 