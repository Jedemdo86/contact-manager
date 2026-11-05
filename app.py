import mysql.connector
from db_funktionen import *
from db_verbindung import *


def create_person(vorname, nachname, geschlecht, geburtsdatum, groesse):
    sql="""
    INSERT INTO person (vorname, nachname, geschlecht, geburtsdatum, groesse)
    VALUES (%s, %s, %s, %s, %s)
    """
    werte= (vorname, nachname, geschlecht, geburtsdatum, groesse)
    cursor.execute(sql, werte)
    mydb.commit()

def create_kommunikation(person_id, typ, wert):
    sql="""
    INSERT INTO kommunikation (person_id, typ, wert)
    VALUES (%s, %s, %s)
    """
    werte= (person_id, typ, wert)
    cursor.execute(sql, werte)
    mydb.commit()

def update_person():
    sql= """
    UPDATE person_adresse
    SET gueltig_bis = "2077-12-31"
    WHERE adresse_id = 1
    """
    cursor.execute(sql)
    mydb.commit()

def create_adresse(person_id, typ, strasse, hausnummer, plz, stadt, land, ist_standard, adress_typ, gueltig_bis):
    sql_1="""
    INSERT INTO adresse (typ, strasse, hausnummer, plz, stadt, land)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    werte= (typ, strasse, hausnummer, plz, stadt, land)
    cursor.execute(sql_1, werte)

    adresse_id = cursor.lastrowid

    sql_2="""
    INSERT INTO person_adresse (person_id, adresse_id, ist_standard, adress_typ, gueltig_bis)
    VALUES (%s, %s, %s, %s, %s)
    """
    werte= (person_id, adresse_id, ist_standard, adress_typ, gueltig_bis)
    cursor.execute(sql_2, werte)
    print(f"Adresse für Person ID: {person_id} hinzugefügt")
    mydb.commit()

# create_database()
# create_table()
# drop_table("person")
# create_person("Thiemo", "Vetter", "M", "1986-11-24", 175)
# create_person("Sophia", "Madel", "W", "1990-08-11", 157)
create_person("Daniel", "Herkendell", "M", "1986-10-25", 176)
# create_kommunikation(1,"Telefon","01783470722")
# create_adresse("1","Wohnung", "Kirchbachstraße", "12a", "45476", "Mülheim an der Ruhr", "Deutschland", "1", "Privat", "2077-12-31")
# update_person()
person_anzeigen(1)
person_anzeigen(2)
person_anzeigen(3)

