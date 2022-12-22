import sqlite3

pointeur = sqlite3.connect("base_donner.db")
curseur = pointeur.cursor()



def cree_la_base():
    try:
        curseur.execute("CREATE TABLE base_donne_utilisateur(id_utilisateur integer primary key autoincrement,nom_utilisateur TEXT,prenom_utilisateur TEXT,adresse_mail TEXT,mot_de_passe TEXT)")
        pointeur.commit()
    except:
        pass

def inscrit_des_infos_dans_la_base(liste):
    nom = "'"+liste[0]+"'"
    prenom = "'"+liste[1]+"'"
    adresse_mail = "'"+ liste[2]+"'"
    mot_de_passe = "'"+liste[3]+"'"
    existe_deja = curseur.execute(f"""SELECT prenom_utilisateur FROM base_donne_utilisateur Where adresse_mail={adresse_mail}""")
    pointeur.commit()
    test = []
    for valeur in existe_deja:
        for prenom in valeur:
            test.append(prenom)
    if len(test)>=1:
        print("l'adresse :",liste[2],"est déjà utilisé")
    else:
        code = curseur.execute("SELECT COUNT(*) FROM base_donne_utilisateur")
        for valeur in code:
            for nb in valeur:
                code = nb + 1
        
        curseur.execute(f"""INSERT INTO base_donne_utilisateur VALUES({code},{nom},{prenom},{adresse_mail},{mot_de_passe})""")
        pointeur.commit()
    
def verifie_connection(liste):
    mot_de_passe = "'"+liste[1]+"'"
    adresse_mise_en_petit = liste[0]
    test_adresse = "'"+adresse_mise_en_petit.lower()+"'"
    print(test_adresse)
    try:    
        valeur_adresse_et_mot_de_passe = curseur.execute(f"""SELECT mot_de_passe FROM base_donne_utilisateur WHERE adresse_mail={test_adresse}""")
        pointeur.commit()
        liste_mot_passe = []
        for valeur in valeur_adresse_et_mot_de_passe:
            for indice in valeur:
                liste_mot_passe.append(indice)
        mot_de_passe_a_tester = "'"+liste_mot_passe[0]+"'"
        return mot_de_passe==mot_de_passe_a_tester
    except:
        return False
    
def donne_les_infos(mail):
    mail = "'"+mail+"'"
    info_utilisateur = curseur.execute(f"""SELECT prenom_utilisateur, nom_utilisateur, adresse_mail FROM base_donne_utilisateur WHERE adresse_mail={mail}""")
    pointeur.commit()
    liste=[]
    for valeur in info_utilisateur:
        for indice in valeur:
            liste.append(indice)
    return liste


cree_la_base()
