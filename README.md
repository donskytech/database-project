# database-project
Creates a database project for IOT that uses SQLLITE as the database engine and using Python sqllite3 to create the database objects

Clone this project:

	git clone https://github.com/donskytech/database-project.git
	cd database-project
  
I have created a sample table in this database called Students:

https://github.com/donskytech/database-project/blob/master/StudentDB.sql

If you want to create your own then just delete the StudentDB.db and alter the code in https://github.com/donskytech/database-project/blob/master/student_db_utils.py and run it using commands suitable for your environment.

I have run this in a windows machine and the only requirement is a Python 3 installation.

Run:

	python --version
  
Requires Python 3 and the sqllite3 module is already pre-installed with the current Python 3 standard library.

then run
	python student_db_utils.py
  
This will create a new database with the file name StudentDB.db.

If you pass the file name as :memory: to the connect() function of the sqlite3 module, it will create a new database that resides in the memory (RAM) instead of a database file on disk.

		def db_connect():
			con = sqlite3.connect(':memory')
			return con
