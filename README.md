# flask-mysqlalchemy-tests
The goal of this test is to practice using MySql in SQLAlchemy 1.2
I was able to modify the connection string and then use the same code that I had written for a sqlite database in order to create a local MySql database and
update the information in the database. I added a graph component that graphs all information in the database. This enables me to test if the changes I pushed
to the databse went through properly. I also tested the nature of the specific database, and how SQLAlchemy handles removing data from the database. I created the
database in MySQL Workbench and then connected to it and dynamically updated it using a webpage running Flask with SQLAlchemy.