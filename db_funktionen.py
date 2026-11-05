from db_verbindung import mydb, cursor

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

def person_anzeigen(person_id):
    sql="""
    SELECT p.person_id, p.vorname, p.nachname, p.geschlecht, p.geburtsdatum, p.groesse, k.typ, k.wert, a.typ, a.strasse, a.hausnummer, a.plz, a.stadt, a.land
    FROM person p 
    LEFT JOIN kommunikation k ON p.person_id = k.person_id
    LEFT JOIN person_adresse pa ON p.person_id = pa.person_id
    LEFT JOIN adresse a ON pa.person_id = a.adresse_id
    WHERE p.person_id = %s
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