from configparser import ConfigParser

import psycopg2

connection = psycopg2.connect(host="localhost", dbname="pickle_db", user="pickle_user",password="mypassword123", port=5432)

curr = connection.cursor()
curr.execute("""ALTER TABLE players ADD COLUMN DECIMAL dupr_rating""")


connection.commit()
connection.close()
curr.close()