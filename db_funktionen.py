from db_verbindung import mydb, cursor
import random
from datetime import datetime, timedelta
from listen import *


def person_anzeigen(person_id):
    sql="""
    SELECT p.person_id, p.vorname, p.nachname, p.geschlecht, p.geburtsdatum, p.groesse, k.typ, k.wert, a.typ, a.strasse, a.hausnummer, a.plz, a.stadt, a.land
    FROM person p 
    LEFT JOIN kommunikation k ON p.person_id = k.person_id
    LEFT JOIN person_adresse pa ON p.person_id = pa.person_id
    LEFT JOIN adresse a ON pa.person_id = a.adresse_id
    # WHERE p.person_id = %s
    """
    cursor.execute(sql, (person_id,))
    ergebnisse = cursor.fetchall()

    if not ergebnisse:
        print("Keine Person mit der ID: {person_id} gefunden")

    erste_zeile = ergebnisse[0]
    print("=" * 40)
    print(f"ID:          {erste_zeile[0]}")
    print(f"Name:        {erste_zeile[1]} {erste_zeile[2]}")
    print(f"Geschlecht:  {erste_zeile[3]}")
    print(f"Geburtstag:  {erste_zeile[4]}")
    print(f"Größe:       {erste_zeile[5]} cm")
    print("-" * 40)
    print("Kontaktdaten:")
    
    # Alle Kontaktdaten durchgehen
    hat_kontakte = False
    for zeile in ergebnisse:
        typ = zeile[6]
        wert = zeile[7]
        if typ and wert:
            print(f"  - {typ}: {wert}")
            hat_kontakte = True
            
    if not hat_kontakte:
        print("  (Keine Kontaktdaten hinterlegt)")
    print("=" * 40)

    hat_adresse = False

    typ = zeile[8]
    strasse = zeile[9]
    hausnummer = zeile[10]
    stadt = zeile[11]
    land = zeile[12]
    # ist_standard = zeile[13]
    # adress_typ = zeile[14]
    # gueltig_bis = zeile[15]
    if typ:
        print("Adressdaten:")
        print(f"ID  Typ         Straße              Hausnummer          Stadt        Land")
        print(f"    {typ}     {strasse}         {hausnummer}        {stadt}      {land}")
        hat_adresse = True

    if not hat_adresse:
        print("  (Keine Adressdaten hinterlegt)")
    print("=" * 40)
    
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

def update_geschlecht (person_id, geschlecht):
    sql= """
    UPDATE person
    SET geschlecht = %s
    WHERE person_id = %s
    """
    werte= (geschlecht, person_id)
    cursor.execute(sql,werte)
    mydb.commit()
    
    
def delete_adresse(person_id, adresse_id):
    sql="""
    DELETE FROM person_adresse
    WHERE person_id = "2" AND adresse_id = "1" AND gueltig_bis IS NULL
    """
    cursor.execute(sql)
    mydb.commit()
    print("Eintrag gelöscht")
    

def create_adresse(typ, strasse, hausnummer, plz, stadt, land):
    sql_1="""
    INSERT INTO adresse (typ, strasse, hausnummer, plz, stadt, land)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    werte= (typ, strasse, hausnummer, plz, stadt, land)
    cursor.execute(sql_1, werte)
    mydb.commit()
    return cursor.lastrowid
    
def assign_adresse(person_id, adresse_id, ist_standard, adress_typ, gueltig_bis):
    sql="""
    INSERT INTO person_adresse (person_id, adresse_id, ist_standard, adress_typ, gueltig_bis)
    VALUES (%s, %s, %s, %s, %s)
    """
    werte= (person_id, adresse_id, ist_standard, adress_typ, gueltig_bis)
    cursor.execute(sql, werte)
    print("Adresse zugewiesen")    
    mydb.commit()



def create_hobby(name, beschreibung):
    sql= """
    INSERT INTO hobby (name, beschreibung)
    VALUES (%s, %s)
    """
    werte= (name, beschreibung)
    cursor.execute(sql, werte)
    print("Hobby erstellt")
    mydb.commit()
    
def assign_hobby(person_id, hobby_id):
    print(f"person_id: {person_id} | hobby_id: {hobby_id}")
    sql="""
    INSERT INTO person_hobby (person_id, hobby_id)
    VALUES (%s, %s)
    """
    werte= (person_id, hobby_id)
    cursor.execute(sql, werte)
    print("Hobby zugewiesen")
    mydb.commit()

def person_generator(add_to_db):
    name = name_generator()
    vorname = name[0]
    nachname = name[1]
    geschlecht = name[2]
    geburtsdatum = generate_geburtsdatum()
    groesse = random.randint(150, 210)
    adresse = adress_generator()
    typ = adresse[0]
    strasse = adresse[1]
    hausnummer = adresse[2]
    stadt = adresse[3]
    land = adresse[4]
    print(vorname,nachname,geschlecht,geburtsdatum,groesse,typ,strasse,hausnummer,stadt,land)
    if add_to_db:
        sql="""
            INSERT INTO person (vorname,nachname,geschlecht,geburtsdatum,groesse)
            VALUES (%s, %s, %s, %s, %s)
        """
        werte = (vorname,nachname,geschlecht,geburtsdatum,groesse)
        cursor.execute(sql,werte)
        person_id = cursor.lastrowid
        sql="""
            INSERT INTO adresse (typ,strasse,hausnummer,stadt,land)
            VALUES (%s, %s, %s, %s, %s)
        """
        werte = (typ,strasse,hausnummer,stadt,land)
        cursor.execute(sql,werte)
        adresse_id = cursor.lastrowid
        ist_standard = 1
        adress_typ = "privat"
        gueltig_bis = "2077-12-31"
        sql="""
            INSERT INTO person_adresse (person_id, adresse_id, ist_standard, adress_typ, gueltig_bis)
            VALUES (%s, %s, %s, %s, %s)
        """
        werte = (person_id, adresse_id, ist_standard, adress_typ, gueltig_bis)
        cursor.execute(sql,werte)
        mydb.commit()
    else:
        return

def generate_geburtsdatum(min_alter=18, max_alter=85):
  heute = datetime.today()

  fruehestes_jahr = heute.year - max_alter
  spaetestes_jahr = heute.year - min_alter

  start_datum = datetime(fruehestes_jahr, 1, 1)
  end_datum = datetime(spaetestes_jahr, 12, 31)

  delta_tage = (end_datum - start_datum).days
  zufaehlige_tage = random.randint(0, delta_tage)

  geburtsdatum = start_datum + timedelta(days=zufaehlige_tage)

  return geburtsdatum.strftime("%Y-%m-%d")

def adress_generator():
    typ = random.choice(typ_liste)
    strasse = random.choice(strassen_liste)
    hausnummer = random.randint(1,100)
    stadt = random.choice(staedte_liste)
    land = random.choice(land_liste)
    return typ,strasse,hausnummer,stadt,land
    
    
def name_generator():
    random_geschlecht = random.choice(geschlecht_liste)
    if random_geschlecht == "M":
        random_vorname = random.choice(m_vornamen_liste)
    else:
        random_vorname = random.choice(w_vornamen_liste)
    random_nachname = random.choice(nachnamen_liste) 
    return random_vorname, random_nachname, random_geschlecht

def hobby_generator():
    kategorie = random.choice(hobbies_liste)
    hobby = random.choice(kategorie["hobbies"])    
    print("Hobby: ",hobby["name"])
    print("Kategorie: ",kategorie["kategorie"])
    print("Benötigte Ausrüstung: ",hobby["benoetigte_ausruestung"])
    print("\nGefährdungsgrad: ",hobby["gefaehrdungsgrad"])


    #TODO Function to fill SQL Hobby table with all from hobby list via nested loop. Create kategorie -> link hobbies to them. make it safely reusable
    for kategorie in hobbies_liste:
        print("- ",kategorie["kategorie"])
        sql_kategorie="""
        INSERT IGNORE INTO kategorie (kategorie_name)
        VALUES (%s)
        """
        werte = (kategorie["kategorie"])
        cursor.execute(sql_kategorie,(werte,))
        kategorie_id = cursor.lastrowid
        print(f"ID: {kategorie_id}")
        for hobby in kategorie["hobbies"]:
            print(hobby["name"])
        print("="*40)
        
hobby_generator()