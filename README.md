# Phoenix
Project Manager App
اپ مدیر آنلاین


create a venv:
```bash
python -m venv venv
```
activate it in linux:
```bash
source ./venv/bin/avtivate
```
or activate it in windows:
```bash
./venv/Scripts/avtivate.bat
```
install requirement:
```python
pip install -r requirements.txt
```

put your site root address,'/' , '/phoenix/' eg:
```python
echo "SITE_URL='/'" >> phoenix2/settings_pars.py
```
or for special subdomain (for example '/phoenix/'):

```python
echo "SITE_URL='/phoenix/'" >> phoenix/server_settings.py
```
generate and view secret key:
```python
rm phoenix2/secret_key.py
echo "SECRET_KEY = 'yj)%c-)__z_null-_l-ned!$6*cs)_=w@g&t=0vj^wg)knwm3z'" >> phoenix/secret_key.py
python manage.py djecrety
```
copy and put it in specific file:
```bash
vi phoenix2/secret_key.py
```


put my sql db credential in files like right below:

```
[client]
database = your_database_name
host = your_host_name
user = your_user_name
password = your_password
default-character-set = utf8
```
for production:
```bash
rm phoenix2/secret_my_sql.cnf
echo "[client]">> phoenix/secret_my_sql.cnf
echo "database = your_database_name">> phoenix/secret_my_sql.cnf
echo "host = your_host_name">> phoenix/secret_my_sql.cnf
echo "user = your_user_name">> phoenix/secret_my_sql.cnf
echo "password = your_password">> phoenix/secret_my_sql.cnf
echo "default-character-set = utf8" >> phoenix/secret_my_sql.cnf
```



migrate : 
```python
python manage.py migrate
```

create superuser : 
```python
python manage.py createsuperuser
```

collectstatic : 
```python
python manage.py collectstatic
```


```bash
cp ./server/phoenix2.ini /etc/uwsgi/sites/phoenix2.ini
cp ./server/phoenix2 /etc/nginx/sites-available/phoenix2

```
