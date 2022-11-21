#!/bin/bash

echo "It is assumed you have install npm, python and postgresql before continuing."
echo "Additionally for postgres it is assumed you've setup a database and user according to the contents of `server/server/settings.py`, in the DATABASE dictionary, or made your own settings in server/server/local_settings.py."

echo "Please enter what you use to invoke python (py|python|python3): "
read python

$python --version

echo "Installing venv and creating a virtual environment..."
$python -m pip install virtualenv
$python -m venv venv


if [[ "$OSTYPE" == "cygwin" ]]; then
    source venv/Scripts/activate
elif [[ "$OSTYPE" == "msys" ]]; then
    source venv/Scripts/activate
elif [[ "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate
else
	source venv/bin/activate
fi

echo "Installing server requirements..."

$python -m pip install --upgrade pip
$python -m pip install -r server/requirements.txt

echo "Creating DB & Installing Fixtures..."

# Create local_settings.py if it doesn't exist.
FILE=server/server/local_settings.py
if test -f "$FILE"; then
    echo "Using the local_settings.py file you've already created.."
else
    touch server/server/local_settings.py
    echo "DEBUG = True" > server/server/local_settings.py
fi

cd server

# Migrate
$python manage.py migrate

$python manage.py loaddata fixtures/initial.json

cd ../

echo "Installing client requirements..."
cd client
npm install
cd ../

echo "All done! To start the server first run 'run_client.sh'. Once this has completed, you can run 'run_server.sh'"
echo "To login, navigate to localhost:8000/admin and user credentials 'admin' and '123'."
echo "By default, this user has my codeforces handle linked, and so going to the main page (localhost:8000) should load in 48 problem submissions after a few seconds (reload to see the effects)"
