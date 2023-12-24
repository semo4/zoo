echo "Building project packages ...."
python3 -m pip3 install -r requirements.txt

echo "Migrating Database ...."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

echo "Collecting static files ...."
python3 manage.py collectstatic --noinput