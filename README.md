django.nV
=========

django.nV is a purposefully vulnerable Django application provided by [nVisium](https://www.nvisium.com/).

###System Requirements & Setup###

First, make sure Python 3.4+ is installed on your machine. On OSX, this can be installed with Homebrew (eg. `brew install python3`). If you receive an error about conflicting PYTHONPATH, try updating the variable to reflect your python version.

```
export PYTHONPATH="/usr/local/lib/python3.4/site-packages"
```

Before using django.nV, you'll also need to install virtualenv. You should be able to use `pip install virtualenv`, using the pip package manager, to install it. On most systems, pip should be installed alongside python.

To set up the repository, use `virtualenv --python=python3 venv`, which will create a virtualenv using Python 3. To enter this environment, run `source venv/bin/activate`. You should see your $PS1 update to include `(venv)`, to remind you that you are in the virtual environment. You can also leave the environment by simply typing `deactivate`.

###Installation of Dependencies###

To install the dependencies, simply run `pip install -r requirements.txt`.

###Database Setup###

django.nV provides you with a script that removes a db if present, automatically creates the database as well as populates it with data. This script is titled `reset_db.sh`. django.nV does not ship with the database, so in order to run the application properly, you'll need to use this script:
 
    ./reset_db.sh
    
###Running the application###
To run the app in its application folder type:

    ./runnapp.sh
    
You should then be able to access the web interface at `http://localhost:8000/`
