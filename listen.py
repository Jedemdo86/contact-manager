strassen_liste = [
    "Hauptstraße", "Schulstraße", "Dorfstraße", "Bahnhofstraße", "Gartenstraße", "Bergstraße", "Schillerstraße", "Goethestraße", "Lindenstraße", "Kirchstraße",
    "Birkenweg", "Kirchweg", "Waldstraße", "Feldstraße", "Ringstraße", "Parkstraße", "Wiesenweg", "Poststraße", "Blumenstraße", "Erlenweg",
    "Buchenweg", "Dorfweg", "Sonnenstraße", "Jahnstraße", "Am Sportplatz", "Postweg", "Kuckucksweg", "Schloßstraße", "Uhlandstraße", "Lessingstraße",
    "Fichtenweg", "Ahornweg", "Sudetenstraße", "Brunnenstraße", "Kastanienweg", "Kiefernweg", "Heine Straße", "Fontanestraße", "Rathausstraße", "Mühlenstraße",
    "Talstraße", "Bahnhofsweg", "Mühlenweg", "Am Wald", "Kirchplatz", "Neugasse", "Mörikestraße", "Siedlungsstraße", "Waldweg", "Schulweg",
    "Sandweg", "Feldweg", "Industriestraße", "Gartenweg", "Eichenweg", "Hintergasse", "Rosenweg", "Kirchenstraße", "Querstraße", "Marktplatz",
    "Breite Straße", "Kurze Straße", "Neue Straße", "Vorstadt", "Am Berg", "Am Kirchpfad", "Schloßberg", "Weidenweg", "Hasenweg", "Flurstraße",
    "Mittelstraße", "Nordstraße", "Südstraße", "Oststraße", "Weststraße", "Zeppelinstraße", "Bismarckstraße", "Brahmsstraße", "Beethovenstraße", "Mozartstraße",
    "Körnerstraße", "Stormstraße", "Mörikeweg", "Eichendorffstraße", "Hebbelstraße", "Rilkestraße", "Wilhelmstraße", "Friedrichstraße", "Auguststraße", "Karlstraße",
    "Ludwigstraße", "Geibelstraße", "Claudiusstraße", "Kernerstraße", "Hauffstraße", "Wielandstraße", "Herderstraße", "Lentzeallee", "Ringweg", "Fasanenweg"
]

staedte_liste = [
    "Berlin", "Hamburg", "München", "Köln", "Frankfurt am Main", "Stuttgart", "Düsseldorf", "Leipzig", "Dortmund", "Essen",
    "Bremen", "Dresden", "Hannover", "Nürnberg", "Duisburg", "Bochum", "Wuppertal", "Bielefeld", "Bonn", "Münster",
    "Mannheim", "Karlsruhe", "Augsburg", "Wiesbaden", "Mönchengladbach", "Gelsenkirchen", "Aachen", "Braunschweig", "Chemnitz", "Kiel",
    "Halle (Saale)", "Magdeburg", "Freiburg im Breisgau", "Krefeld", "Mainz", "Lübeck", "Erfurt", "Oberhausen", "Rostock", "Kassel",
    "Hagen", "Potsdam", "Saarbrücken", "Hamm", "Ludwigshafen am Rhein", "Mülheim an der Ruhr", "Oldenburg", "Osnabrück", "Leverkusen", "Solingen",
    "Darmstadt", "Heidelberg", "Herne", "Neuss", "Regensburg", "Paderborn", "Ingolstadt", "Offenbach am Main", "Fürth", "Würzburg",
    "Ulm", "Heilbronn", "Pforzheim", "Wolfsburg", "Göttingen", "Bottrop", "Reutlingen", "Koblenz", "Recklinghausen", "Bremerhaven",
    "Bergisch Gladbach", "Remscheid", "Jena", "Trier", "Erlangen", "Moers", "Siegen", "Hildesheim", "Salzgitter", "Cottbus",
    "Kaiserslautern", "Gütersloh", "Schwerin", "Witten", "Gera", "Iserlohn", "Ludwigsburg", "Hanau", "Esslingen am Neckar", "Zwickau",
    "Düren", "Ratingen", "Tübingen", "Flensburg", "Lünen", "Villingen-Schwenningen", "Gießen", "Marl", "Dessau-Roßlau", "Worms"
]

typ_liste = [
    "Wohnung", "Haus"
]

land_liste = [
    "Deutschland"
]

nachnamen_liste = [
    "Dreier", "Valuski", "Müller", "Schmidt", "Schneider", "Fischer", "Weber", "Meyer", "Wagner", "Becker",
    "Schulz", "Hoffmann", "Schäfer", "Koch", "Bauer", "Richter", "Klein", "Wolf", "Schröder", "Neumann",
    "Schwarz", "Zimmermann", "Braun", "Krüger", "Hartmann", "Lange", "Werner", "Schmitz", "Krause", "Meier",
    "Lehmann", "Schmid", "Schulze", "Maier", "Köhler", "Herrmann", "König", "Walter", "Mayer", "Huber",
    "Kaiser", "Fuchs", "Peters", "Lang", "Scholz", "Möller", "Weiß", "Jung", "Hahn", "Schubert",
    "Vogel", "Friedrich", "Keller", "Günther", "Frank", "Berger", "Winkler", "Roth", "Beck", "Lorenz",
    "Baumann", "Franke", "Albrecht", "Schuster", "Gast", "Böhm", "Winter", "Kraus", "Martin", "Vogt",
    "Stein", "Jäger", "Otto", "Sommer", "Groß", "Seidel", "Heinrich", "Brandt", "Haas", "Schreiber",
    "Graf", "Dietrich", "Ziegler", "Kuhn", "Kühn", "Pohl", "Engel", "Horn", "Busch", "Bergmann",
    "Thomas", "Voigt", "Sauer", "Arnold", "Wolff", "Pfeiffer", "Timm", "Kramer", "Hansen", "Nagel"
]

m_vornamen_liste = [
    "Maximilian", "Alexander", "Lukas", "Leon", "Elias", "Paul", "Felix", "Jonas", "David", "Julian",
    "Ben", "Louis", "Henry", "Finn", "Liam", "Anton", "Emil", "Oskar", "Theodor", "Mats",
    "Leo", "Moritz", "Milan", "Noah", "Jan", "Tim", "Tobias", "Florian", "Niklas", "Simon",
    "Fabian", "Philipp", "Dominik", "Daniel", "Christian", "Michael", "Stefan", "Nico", "Kevin", "Justin",
    "Marvin", "Pascal", "Robin", "Timon", "Levin", "Mika", "Jannik", "Jonathan", "Samuel", "Clemens",
    "Benedikt", "Johannes", "Timo", "Sven", "Markus", "Lars", "Oliver", "Patrick", "Marcel", "Dennis",
    "Sean", "Thiemo", "Aaron", "Benjamin", "Dominic", "Erik", "Gabriel", "Hannes", "Kilian", "Linus",
    "Marlon", "Raphael", "Silas", "Valentin", "Vincent", "Hannes", "Toni", "Tom", "Janis", "Keno"
]

w_vornamen_liste = [
    "Anna", "Maria", "Lena", "Laura", "Hannah", "Sarah", "Lea", "Sofia", "Marie", "Mia",
    "Emilia", "Sophia", "Emma", "Clara", "Johanna", "Lina", "Mila", "Charlotte", "Amelie", "Luisa",
    "Leonie", "Greta", "Victoria", "Nina", "Julia", "Lisa", "Kim", "Melanie", "Sandra", "Jessica",
    "Zoe", "Elena", "Maya", "Pia", "Tina", "Katrin", "Nadine", "Stefanie", "Chiara", "Franziska",
    "Jasmin", "Katharina", "Lara", "Magdalena", "Miriam", "Paula", "Rabea", "Ronja", "Sabrina", "Saskia",
    "Selina", "Theresa", "Vanessa", "Vivienne", "Xenia", "Yvonne", "Amira", "Celine", "Eileen", "Emily",
    "Lilli", "Nele", "Sophie", "Stella", "Talea", "Alina", "Anja", "Carolin", "Denise", "Esther"
]

geschlecht_liste = ["M","W"]

hobbies_liste = [
    {
        "kategorie": "Wassersport",
        "hobbies": [
            {
                "name": "Apnoetauchen",
                "beschreibung": "Tauchen ohne Sauerstoffgerät mit nur einem Atemzug.",
                "gefaehrdungsgrad": "Hoch",
                "benoetigte_ausruestung": [
                    "Neoprenanzug",
                    "Taucherbrille",
                    "Flossen",
                ],
            },
            {
                "name": "Stand-Up-Paddling",
                "beschreibung": (
                    "Fortbewegung auf einem aufblasbaren Board stehend mit einem"
                    " Stechpaddel."
                ),
                "gefaehrdungsgrad": "Niedrig",
                "benoetigte_ausruestung": [
                    "SUP-Board",
                    "Paddel",
                    "Schwimmweste",
                ],
            },
            {
                "name": "Kitesurfen",
                "beschreibung": (
                    "Sich mit einem großen Lenkdrachen über das Wasser ziehen"
                    " lassen."
                ),
                "gefaehrdungsgrad": "Hoch",
                "benoetigte_ausruestung": ["Kite", "Board", "Trapez", "Helm"],
            },
            {
                "name": "Schwimmen",
                "beschreibung": (
                    "Fortbewegung im Wasser durch eigene Muskelkraft."
                ),
                "gefaehrdungsgrad": "Sehr gering",
                "benoetigte_ausruestung": [
                    "Badekleidung",
                    "Badebrille",
                    "Handtuch",
                ],
            },
        ],
    },
    {
        "kategorie": "Bergsport & Outdoor",
        "hobbies": [
            {
                "name": "Bouldern",
                "beschreibung": (
                    "Klettern ohne Seil an Felsblöcken oder Kletterwänden bis"
                    " zur Absprunghöhe."
                ),
                "gefaehrdungsgrad": "Mittel",
                "benoetigte_ausruestung": [
                    "Kletterschuhe",
                    "Magnesiumbeutel",
                    "Crashpad",
                ],
            },
            {
                "name": "Wingsuit-Fliegen",
                "beschreibung": (
                    "Extremsportart, bei der man im Spezialanzug aus großer"
                    " Höhe abspringt."
                ),
                "gefaehrdungsgrad": "Extrem",
                "benoetigte_ausruestung": [
                    "Wingsuit",
                    "Fallschirm",
                    "Höhenmesser",
                ],
            },
            {
                "name": "Wandern",
                "beschreibung": (
                    "Längeres zu Fuß gehen in der Natur, meist auf markierten"
                    " Wegen."
                ),
                "gefaehrdungsgrad": "Gering",
                "benoetigte_ausruestung": [
                    "Wanderschuhe",
                    "Rucksack",
                    "Trinkflasche",
                ],
            },
            {
                "name": "Mountainbiken",
                "beschreibung": (
                    "Radfahren abseits befestigter Straßen im unwegsamen"
                    " Gelände."
                ),
                "gefaehrdungsgrad": "Hoch",
                "benoetigte_ausruestung": [
                    "Mountainbike",
                    "Helm",
                    "Protektoren",
                    "Fahrradhandschuhe",
                ],
            },
        ],
    },
    {
        "kategorie": "Indoor & Kreativ",
        "hobbies": [
            {
                "name": "Schach",
                "beschreibung": (
                    "Strategisches Brettspiel für zwei Personen."
                ),
                "gefaehrdungsgrad": "Keine",
                "benoetigte_ausruestung": ["Schachbrett", "Schachfiguren"],
            },
            {
                "name": "Töpfern",
                "beschreibung": (
                    "Formen von Gegenständen aus Ton auf der Drehscheibe oder per"
                    " Hand."
                ),
                "gefaehrdungsgrad": "Gering",
                "benoetigte_ausruestung": [
                    "Töpferton",
                    "Töpferscheibe",
                    "Brennofen",
                ],
            },
            {
                "name": "Malen & Zeichnen",
                "beschreibung": (
                    "Erstellen von Bildern mit Farben, Stiften oder Kohle."
                ),
                "gefaehrdungsgrad": "Keine",
                "benoetigte_ausruestung": [
                    "Leinwand",
                    "Pinsel",
                    "Farben",
                    "Bleistifte",
                ],
            },
            {
                "name": "Kochen & Backen",
                "beschreibung": (
                    "Zubereiten von Speisen und Lebensmitteln nach Rezept oder"
                    " kreativ."
                ),
                "gefaehrdungsgrad": "Gering (Verbrennungsgefahr)",
                "benoetigte_ausruestung": [
                    "Pfannen",
                    "Töpfe",
                    "Messer",
                    "Küchenwaage",
                ],
            },
        ],
    },
    {
        "kategorie": "Motorsport & Technik",
        "hobbies": [
            {
                "name": "Kartfahren",
                "beschreibung": (
                    "Motorsport mit kleinen, rahmenlosen Rennfahrzeugen auf"
                    " Kartbahnen."
                ),
                "gefaehrdungsgrad": "Mittel",
                "benoetigte_ausruestung": ["Helm", "Rennkombi", "Rippenschutz"],
            },
            {
                "name": "Drohnen-Fliegen",
                "beschreibung": (
                    "Steuern von unbemannten Fluggeräten per Fernbedienung und"
                    " Kamera."
                ),
                "gefaehrdungsgrad": "Gering",
                "benoetigte_ausruestung": [
                    "Drohne",
                    "Fernsteuerung",
                    "Ersatzakkus",
                ],
            },
            {
                "name": "Modellbau",
                "beschreibung": (
                    "Detailgetreue Nachbildung von Autos, Flugzeugen oder"
                    " Schiffen im Kleinformat."
                ),
                "gefaehrdungsgrad": "Keine",
                "benoetigte_ausruestung": [
                    "Bausatz",
                    "Modellbaukleber",
                    "Pinzette",
                    "Farben",
                ],
            },
            {
                "name": "3D-Druck",
                "beschreibung": (
                    "Erstellen physischer dreidimensionaler Objekte aus"
                    " digitalen Vorlagen."
                ),
                "gefaehrdungsgrad": "Gering",
                "benoetigte_ausruestung": [
                    "3D-Drucker",
                    "Filament",
                    "Spachtel",
                ],
            },
        ],
    },
    {
        "kategorie": "Sammeln & Geist",
        "hobbies": [
            {
                "name": "Briefmarkensammeln",
                "beschreibung": (
                    "Zusammentragen und archivieren von postfrischen oder"
                    " gestempelten Briefmarken."
                ),
                "gefaehrdungsgrad": "Keine",
                "benoetigte_ausruestung": [
                    "Briefmarkenalbum",
                    "Pinzette",
                    "Lupe",
                ],
            },
            {
                "name": "Gärtnern",
                "beschreibung": (
                    "Anbauen und Pflegen von Blumen, Gemüse oder Zimmerpflanzen."
                ),
                "gefaehrdungsgrad": "Sehr gering",
                "benoetigte_ausruestung": [
                    "Blumenerde",
                    "Gartenschere",
                    "Blumentöpfe",
                ],
            },
            {
                "name": "Astronomie",
                "beschreibung": (
                    "Beobachten des Sternenhimmels, der Planeten und Himmelskörper."
                ),
                "gefaehrdungsgrad": "Keine",
                "benoetigte_ausruestung": [
                    "Teleskop",
                    "Sternenkarte",
                    "Fernglas",
                ],
            },
            {
                "name": "Fotografie",
                "beschreibung": (
                    "Festhalten von Momenten, Landschaften oder Personen mit"
                    " einer Kamera."
                ),
                "gefaehrdungsgrad": "Keine",
                "benoetigte_ausruestung": [
                    "Kamera",
                    "Objektiv",
                    "Stativ",
                    "Speicherkarte",
                ],
            },
        ],
    },
]