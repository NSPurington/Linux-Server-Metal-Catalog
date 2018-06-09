# Metal-Catalog-App

Metal Catalog App on an AWS Lightsail Linux server using a PostgreSql database

# DESCRIPTION

The Metal Catalog App is a web app, coded using Python, using Flask, SQL Alchemy, and Psycopg2 to interact with the Apache2 WSGI protocol based on an Amazon Web Services Linux (Ubuntu distribution) server.  Postgresql is used for the database duties, and holds the 3 tables used in this app.  This apps purpose is to educate clients on basemetal and alloy relationships, as well as giving an opportunity to add a basemetal and alloy. 

# LOCATION

IP address = 52.32.17.248

SSH port = 22

URL = http://ec2-52-32-17-248.us-west-2.compute.amazonaws.com/

# SOFTWARE

--Python--
1. Python 2.7 (apt-get install python2.7)
2. Flask (pip install flask)
3. SQL Alchemy (pip install sqlalchemy)
4. Oauth2 Client (pip install oauth2client)
5. Requests (pip install requests)
6. Passlib (pip install passlib)
7. Its Dangerous (pip install itsdangerous)
8. Psycopg2 (pip install psycopg2) + (pip install psycopg2-binary)

--Web/WSGI--

9. Apache2 (apt-get apache2)
10. MOD - WSGI (apt-get libapache2-mod-wsgi)

--Database--

11. Postgresql (apt-get install postgresql) + (apt-get install postgresql-client)



