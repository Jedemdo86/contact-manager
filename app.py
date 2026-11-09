import mysql.connector
from db_funktionen import *
from db_verbindung import *




# create_database()
# create_table()
# drop_table("person")
# create_person("Thiemo", "Vetter", "M", "1986-11-24", 175)
# create_person("Sophia", "Madel", "W", "1990-08-11", 157)
# create_person("Daniel", "Herkendell", "M", "1986-10-25", 176)
# create_kommunikation(1,"Telefon","01783470722")
# create_adresse("1","Wohnung", "Kirchbachstraße", "12a", "45476", "Mülheim an der Ruhr", "Deutschland", "1", "Privat", "2077-12-31")
# update_person()
# person_anzeigen(1)
# person_anzeigen(2)
# person_anzeigen(3)
# delete_adresse(2,1)

print(f"{name_generator()} \n{name_generator()} \n{name_generator()} \n{name_generator()} \n{name_generator()} \n{name_generator()} \n")
person_1 = name_generator()
vorname = person_1[0]
nachname = person_1[1]
geschlecht = person_1[2]
print(f"Zusammengesetzter Name: {vorname} {nachname}, {geschlecht}")


while True:
    print("="*40)
    print("Kontakt-Datenbank")
    print("1 - Kontakt anzeigen lassen")
    print("2 - Neuen Kontakt erstellen")
    print("3 - Kommunikationsmittel erstellen")
    print("4 - Hobby erstellen")
    print("5 - Hobby zuweisen")
    print("6 - Adresse erstellen")
    print("7 - Adresse zuweisen")
    print("9 - Beenden")
    print("Auswahl:")
    auswahl = input()
    match auswahl:
        case "1":
            print("1 - Alle Kontakte anzeigen")
            print("2 - Kontakt nach ID filtern")
            auswahl = input()
            match auswahl:
                case "1":
                    print("DEBUG: Zeige ALLE Kontakte an")
                case "2":
                    print("Nach welcher ID filtern?")
                    auswahl = input()
                    print(f"ID {auswahl} wird angezeigt")
                    person_anzeigen(auswahl)
                    
            print("Erfolg")
        case "2":
            print("Neuen Kontakt erstellen")
            print("Vorname")
            vorname = input()
            print("Nachname")
            nachname = input()
            print("Geschlecht (M oder W)")
            geschlecht = input()
            print("Geburtsdatum (JAHR-MONAT-TAG)")
            geb = input()
            print("Größe (in cm)")
            groesse = input()
            print(f"Soll der Kontakt: {vorname} {nachname}, {geschlecht}, geboren am {geb} und {groesse} cm größe erstellt werden")
            print("Bestätige mit '1'")
            auswahl = input()
            if auswahl == "1":
                create_person(vorname,nachname,geschlecht,geb,groesse)
            else:
                print("Vorgang abgebrochen..")
        case "3":
            print("Welcher ID soll es hinzugefügt werden?")
            auswahl_id = input()
            print("Um welche Art handelt es sich?")
            print("1 - Telefon")
            print("2 - E-Mail")
            auswahl_device = input()
            match auswahl_device:
                case "1":
                    auswahl_device = "Telefon"
                    print("Wie lautet die Telefonnummer?")
                    auswahl_nummer = input()
                    create_kommunikation(auswahl_id, auswahl_device, auswahl_nummer)
                case "2":
                    auswahl_device = "E-Mail"
                    print("Wie lautet die E-Mail Adresse?")
                    auswahl_nummer = input()
                    create_kommunikation(auswahl_id, auswahl_device, auswahl_nummer)
                case _:
                    print("keine gültige Auswahl..")
        case "4":
            print("Erstellung eines Hobbies")
            print("Hobby-Name:")
            name = input()
            print("Beschreibung:")
            beschreibung = input()
            print(f"Soll dieses Hobby erstellt werden?")
            print(f"Name:           {name}")
            print(f"Beschreibung:   {beschreibung}")
            print("Tippe '1' zum bestätigen")
            auswahl = input()
            if auswahl == "1":
                create_hobby(name, beschreibung)
        case "5":
            print("Welcher Person soll ein Hobby zugewiesen werden?")
            print("Gib die ID der Person ein:")
            person_id = input()
            print("Gib die ID des Hobbies ein:")
            hobby_id = input()
            print("Tippe '1' zum bestätigen")
            auswahl = input()
            if auswahl == "1":
                assign_hobby(person_id, hobby_id)     
        case "7":
            print("Welcher Personen ID soll die Adress_id zugeordnet werden?")    
            print("person_id:")
            person_id = input()
            print("adresse_id:")
            adresse_id = input()
            print("Hauptwohnsitz der Person? (j / n)")
            ist_standard = input()
            if ist_standard == "j":
                ist_standard = "1"
            else:
                ist_standard = "0"    
            print("Privat oder Geschäftsadresse? (p / g)")
            adress_typ = input()
            if adress_typ == "p":
                adress_typ = "Privat"
            elif adress_typ == "g":
                adress_typ = "Geschäftlich"
            else:
                print("Keine gültige Angabe")
                quit()
            print("Bis wann ist die Adresse gültig? (JAHR,MONAT,TAG (1970-12-24) )")
            gueltig_bis = input()
            
            assign_adresse(person_id, adresse_id, ist_standard, adress_typ, gueltig_bis)
        case "9":
            print("Beende Terminal-App..")
            quit()
        case _:
            print("keine gültige Auswahl..")

            