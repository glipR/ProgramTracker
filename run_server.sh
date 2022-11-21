if [[ "$OSTYPE" == "cygwin" ]]; then
    source venv/Scripts/activate
elif [[ "$OSTYPE" == "msys" ]]; then
    source venv/Scripts/activate
elif [[ "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate
else
	source venv/bin/activate
fi

cd server

python manage.py runserver
