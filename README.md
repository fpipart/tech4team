Install required environment:

pip install -r requirement.txt
export FLASK_APP=tech4Team.py
flask db init
flask db upgrade
flask run