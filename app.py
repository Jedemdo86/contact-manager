import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mycontactdb"
)
cursor = mydb.cursor()

def create_database():
    sql = """CREATE DATABASE mycontactdb"""
    cursor.execute(sql)
    mydb.commit()

def create_table():
    sql1= """CREATE TABLE IF NOT EXISTS person (
                person_id INT AUTO_INCREMENT PRIMARY KEY,
                vorname VARCHAR(30),
                nachname VARCHAR(30),
                geschlecht VARCHAR(30),
                geburtsdatum DATE,
                groesse INT
            );"""
            
    sql2= """CREATE TABLE IF NOT EXISTS kommunikation (
                kommunikation_id INT AUTO_INCREMENT PRIMARY KEY,
                person_id INT,
                typ VARCHAR(30),
                wert VARCHAR(100),
                FOREIGN KEY (person_id) REFERENCES person(person_id)
                    ON DELETE CASCADE
            );"""
            
    sql3= """CREATE TABLE IF NOT EXISTS adresse (
                adresse_id INT AUTO_INCREMENT PRIMARY KEY,
                typ VARCHAR(50),
                strasse VARCHAR(100),
                hausnummer VARCHAR(5),
                plz VARCHAR(5),
                stadt VARCHAR(100),
                land VARCHAR(100)    
            );"""
    sql4= """CREATE TABLE IF NOT EXISTS person_adresse (
                person_id INT,
                adresse_id INT,
                ist_standard BOOLEAN,
                adress_typ VARCHAR(50),
                gueltig_bis DATE,
                FOREIGN KEY (person_id) REFERENCES person(person_id),
                FOREIGN KEY (adresse_id) REFERENCES adresse(adresse_id)
            );"""
    sql5= """CREATE TABLE IF NOT EXISTS hobby (
                hobby_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR (100),
                beschreibung VARCHAR (1000)
            );"""
    
    sql6= """CREATE TABLE IF NOT EXISTS person_hobby (
                person_id INT,
                hobby_id INT,
                FOREIGN KEY (person_id) REFERENCES person (person_id),
                FOREIGN KEY (hobby_id) REFERENCES hobby (hobby_id)
            );"""
            
    sql7= """CREATE TABLE IF NOT EXISTS notiz (
                notiz_id INT AUTO_INCREMENT PRIMARY KEY,
                person_id INT,
                typ VARCHAR(100),
                inhalt VARCHAR(1000),
                datum DATE,
                FOREIGN KEY (person_id) REFERENCES person (person_id)
            );"""
            
    sql8= """CREATE TABLE IF NOT EXISTS job (
                job_id INT AUTO_INCREMENT PRIMARY KEY,
                person_id INT,
                titel VARCHAR(50),
                beschreibung VARCHAR(500),
                firma VARCHAR(100),
                gehalt INT,
                FOREIGN KEY (person_id) REFERENCES person (person_id)
            );"""
            
    sql9= """CREATE TABLE IF NOT EXISTS inventar (
                inventar_id INT AUTO_INCREMENT PRIMARY KEY,
                person_id INT,
                kopf VARCHAR(50),
                brust VARCHAR(50),
                bein VARCHAR(50),
                fuss VARCHAR(50),
                geld INT,
                FOREIGN KEY (person_id) REFERENCES person (person_id)
            );"""
            
    cursor.execute(sql1)
    cursor.execute(sql2)
    cursor.execute(sql3)
    cursor.execute(sql4)
    cursor.execute(sql5)
    cursor.execute(sql6)
    cursor.execute(sql7)
    cursor.execute(sql8)
    cursor.execute(sql9)
    mydb.commit()

def drop_table(tablename):
    sql= f"DROP TABLE {tablename}"
    print(f"Die Tabelle {tablename} wird gelöscht..")
    cursor.execute(sql)
    mydb.commit()


# create_database()
# create_table()
# drop_table("person")
