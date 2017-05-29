from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route("/")
def hello():
		return "Hello World!"

@app.route("/from-db")
def from_db():
	conn_string = "host='%s' dbname='%s' user='%s' password='%s'" % (
		os.environ['POSTGRES_HOST'],
		os.environ['POSTGRES_DB'],
		os.environ['POSTGRES_USER'],
		os.environ['POSTGRES_PWD']
	)
	conn = psycopg2.connect(conn_string)
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM pg_stats limit 1")
	records = cursor.fetchall()
	return str(records)

if __name__ == "__main__":
		app.run()

