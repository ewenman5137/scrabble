from select import select
import tkinter as tk
import lettre as lt
from tkinter import ttk
#====================================================================
#création du background
#donner les tailles de la page 
#====================================================================
couleur_bg = "darkolivegreen"
couleur_interface = "#2c2f33"
root = tk.Tk()
root.title("fonction tri")
root.config(bg=couleur_bg)
fenetre = tk.LabelFrame(root)
fenetre.config(width=750,height=750,bg=couleur_bg,bd=0)
fenetre.pack()

lettre_alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

#cadre global ou l'on va entrer les 7 lettres 
cadre_entrer_ses_lettres = tk.LabelFrame(fenetre)
cadre_entrer_ses_lettres.config(width=600,height=500)
cadre_valeur = tk.LabelFrame(cadre_entrer_ses_lettres,text="Entrer vos lettres ici :",bd=0,fg="black")

# endroit ou les valeurs sont inscrites 
text_mot = tk.StringVar()
text_mot.set("")
mot_entrer = tk.Entry(cadre_entrer_ses_lettres,textvariable=text_mot)

# message d'erreur si le mot ne correspond pas totalement au condition ( pas de chiffre ni de caractère spécial et 7 lettres)
message_erreur = tk.StringVar()
message = "Le mot ne correspond pas au demande (7 lettres)"
message_erreur.set(message)
affiche_erreur = tk.Label(cadre_entrer_ses_lettres,bg="red",bd=0,textvariable=message_erreur)

#================================================================
# Logo scrabble
#================================================================
logo_scrabble = tk.PhotoImage(file='scrabble.png')
emplacement_logo_scrabble = tk.Label(fenetre,width=380,height=100,image=logo_scrabble)
emplacement_logo_scrabble.place(x=150,y=20)


#================================================================
# retourne faux si le mot ne correspond pas au condition ( pas de chiffre ni de caractère spécial et 7 lettres)
#================================================================

def verifie_mot(mot):
    mot = mot.upper()
    for lettre in mot:
        if not lettre in lettre_alphabet:
            print("votre mot a des caractère chiffré veuillez entrer un mot sans chiffre")
            return False
    if len(mot) != 7:
        print("le mot doit faire 7 lettre ni plus ni moins")
        return False
    else:
        return True


cadre_jeu = tk.LabelFrame(fenetre,width=600,height=400,bd=0)
message_entrer_mot_utilisateur = tk.LabelFrame(cadre_jeu,width=200,height=20,text="Proposez votre mot :",bd=0)

# endroit ou les valeurs sont inscrites 
text_mot_utilisateur = tk.StringVar()
text_mot_utilisateur.set("")
mot_entrer_par_utilisateur = tk.Entry(cadre_jeu,textvariable=text_mot_utilisateur)

# message erreur utilisateur 
affiche_erreur_utilisateur = tk.Label(cadre_jeu,bg="red",bd=0,textvariable=message_erreur)
lettre_dispo = {"\n":0,"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0,"H":0,"I":0,"J":0,"K":0,"L":0,"M":0,"N":0,"O":0,"P":0,"Q":0,"R":0,"S":0,"T":0,"U":0,"V":0,"W":0,"X":0,"Y":0,"Z":0}

#============================================================
# verifie si le mot entrer possède tout les bonnes lettres 
#============================================================
def lettre_du_mot_correspond(mot):
    copy_dico_lettre_dispo = lettre_dispo
    mot = mot.upper()
    for lettre in mot:
        if copy_dico_lettre_dispo[lettre]>0:
            copy_dico_lettre_dispo[lettre] -=1
        else:
            print("il n'y a pas les bonnes lettres")
            return False
    validation()
    return True

#=======================================================================================================
#  récupère la proposition de l'utilisateur verifie la taille puis s'il y a bien le bon nombre de lettre
#=======================================================================================================
liens_bravo = 'bravo.png'
photo_bravo = tk.PhotoImage

def validation_utilisateur():
    lettre_a_utiliser = ""
    for lettre in lettre_alphabet:
        if lettre_dispo[lettre] >= 1:
            for _ in range(lettre_dispo[lettre]):
                lettre_a_utiliser = lettre_a_utiliser + lettre
    proposition = mot_entrer_par_utilisateur.get()
    proposition = proposition.upper()
    if verifie_mot(proposition):
        if lettre_du_mot_correspond(proposition):
            affiche_erreur.place_forget()
            print("la proposition est : ",proposition)
            affiche_les_lettres(proposition)
            if lt.cherche_un_mot(proposition):
                print("bravo votre mot existe")

            else:
                print("le mot n'existe pas")
    else:
        affiche_erreur_utilisateur.place(x=100,y=150)
    for lettre in lettre_alphabet:
        lettre_dispo[lettre] = 0
    rempli_les_lettres_dispo(lettre_a_utiliser)
        
# bouton de validation
bouton_validation_mot_utilisateur = tk.Button(cadre_jeu,command=validation_utilisateur,width=15,height=2,text="Valider la proposition")

#================================================================
# affiche le message d'erreur
#================================================================
def validation():
    mot = mot_entrer.get().upper()
    if not verifie_mot(mot):
        affiche_erreur.place(x=20,y=150)
    else:
        affiche_erreur.place_forget()
        rempli_les_lettres_dispo(mot)
        jeu(mot)

    

bouton_validation = tk.Button(cadre_entrer_ses_lettres,text="Valider les lettres",command=validation)

cadre_lettre = tk.LabelFrame(cadre_jeu,bg="black")

image_a = tk.PhotoImage(file=lt.A)
image_b = tk.PhotoImage(file=lt.B)
image_c = tk.PhotoImage(file=lt.C)
image_d = tk.PhotoImage(file=lt.D)
image_e = tk.PhotoImage(file=lt.E)
image_f = tk.PhotoImage(file=lt.F)
image_g = tk.PhotoImage(file=lt.G)
image_h = tk.PhotoImage(file=lt.H)
image_i = tk.PhotoImage(file=lt.I)
image_j = tk.PhotoImage(file=lt.J)
image_k = tk.PhotoImage(file=lt.K)
image_l = tk.PhotoImage(file=lt.L)
image_m = tk.PhotoImage(file=lt.M)
image_n = tk.PhotoImage(file=lt.N)
image_o = tk.PhotoImage(file=lt.O)
image_p = tk.PhotoImage(file=lt.P)
image_q = tk.PhotoImage(file=lt.Q)
image_r = tk.PhotoImage(file=lt.R)
image_s = tk.PhotoImage(file=lt.S)
image_t = tk.PhotoImage(file=lt.T)
image_u = tk.PhotoImage(file=lt.U)
image_v = tk.PhotoImage(file=lt.V)
image_w = tk.PhotoImage(file=lt.W)
image_x = tk.PhotoImage(file=lt.X)
image_y = tk.PhotoImage(file=lt.Y)
image_z = tk.PhotoImage(file=lt.Z)

lettre_1 = tk.Label(fenetre,image=image_b)
lettre_2 = tk.Label(fenetre,image=image_b)
lettre_3 = tk.Label(fenetre,image=image_b)
lettre_4 = tk.Label(fenetre,image=image_b)
lettre_5 = tk.Label(fenetre,image=image_b)
lettre_6 = tk.Label(fenetre,image=image_b)
lettre_7 = tk.Label(fenetre,image=image_b)

liste_emplacement_lettre = [lettre_1,lettre_2,lettre_3,lettre_4,lettre_5,lettre_6,lettre_7]
dico_image = {"A":image_a,"B":image_b,"C":image_c,"D":image_d,"E":image_e,"F":image_f,
"G":image_g,"H":image_h,"I":image_i,"J":image_j,"K":image_k,"L":image_l,"M":image_m,
"N":image_n,"O":image_o,"P":image_p,"Q":image_q,"R":image_r,"S":image_s,
"T":image_t,"U":image_u,"V":image_v,"W":image_w,"X":image_x,"Y":image_y,"Z":image_z}


#==================================================================
# place les 7 lettres sous l'encart cadre_jeu
#==================================================================

def affiche_les_lettres(liste_lettre):
    emplacement_lettre = 10
    x=0
    cadre_lettre.place(x=20,y=250)
    for lettre_a_afficher in liste_lettre:
        liste_emplacement_lettre[x].config(image=dico_image[lettre_a_afficher])
        liste_emplacement_lettre[x].place(x=emplacement_lettre,y=620)
        emplacement_lettre = emplacement_lettre + 106
        x = x +1


#========================================================================================
# remplie le dico avec les lettres dispo
#========================================================================================

def rempli_les_lettres_dispo(mot):
    print(mot)
    for lettre in mot:
        lettre_dispo[lettre] += 1

def affiche_les_mot():
    print("d'accord nous allons chercher les mots correspondant")
    lettre_a_utiliser = ""
    for lettre in lettre_alphabet:
        if lettre_dispo[lettre] >= 1:
            for _ in range(lettre_dispo[lettre]):
                lettre_a_utiliser = lettre_a_utiliser + lettre
    liste_mot = lt.trouver_toute_les_valeurs_possibles(lettre_a_utiliser)
    bouton_affiche_les_mots.place_forget()
    affiche_les_mot_possible(liste_mot)
    
    

bouton_affiche_les_mots = tk.Button(cadre_jeu,command=affiche_les_mot,text="affiche les résultat possible")


#================================================================
# fonction qui renvoie une liste de 7 lettre
#================================================================

def donne_les_lettres():
    for lettre in lettre_alphabet:
        lettre_dispo[lettre]=0
    lettre_donner = ""
    bouton_donne_les_lettres.place_forget()
    bouton_entrer_ses_lettres.place_forget()
    lettre_donner = lt.donne_combinaison_possible()
    rempli_les_lettres_dispo(lettre_donner)
    jeu(lettre_donner)
#bouton qui active donne les lettres
bouton_donne_les_lettres = tk.Button(fenetre,command=donne_les_lettres,text="Donne les lettres")
bouton_donne_les_lettres.config(width=15,height=2)
bouton_donne_les_lettres.place(x=200,y=150)

#========================================================================================
# lance le programme principale pour afficher et executer les différents programme du jeu
#========================================================================================


def jeu(liste_lettre_dispo):
    cadre_entrer_ses_lettres.place_forget()
    bouton_donne_les_lettres.place_forget()
    bouton_entrer_ses_lettres.place_forget()
    cadre_jeu.place(x=50,y=200)
    message_entrer_mot_utilisateur.place(x=20,y=20)
    mot_entrer_par_utilisateur.place(x=20,y=50)
    bouton_validation_mot_utilisateur.place(x=250,y=350)
    bouton_affiche_les_mots.place(x=20,y=200)
    bouton_donne_les_lettres_2.place(x=20,y=250)
    affiche_les_lettres(liste_lettre_dispo)


bouton_donne_les_lettres_2 = tk.Button(cadre_jeu,command=donne_les_lettres,text="Donne de nouvelle lettres")

#================================================================
# active l'entrer pour l'utilisateur 
#================================================================

def entrer_ses_lettres():
    bouton_donne_les_lettres.place_forget()
    bouton_entrer_ses_lettres.place_forget()
    cadre_entrer_ses_lettres.place(x=50,y=200)
    cadre_valeur.place(x=50,y=50,width=200,height=20)
    mot_entrer.place(x=50,y=80)
    bouton_validation.place(x=200,y=200,width=200,height=20)

bouton_entrer_ses_lettres = tk.Button(fenetre,command=entrer_ses_lettres,text="Donnez vos lettres")
bouton_entrer_ses_lettres.config(width=15,height=2)
bouton_entrer_ses_lettres.place(x=350,y=150)


cadre_mot_possible = tk.LabelFrame(fenetre,width=700,height=400,bd=0)
liens_correction = 'correction.png'
image_correction = tk.PhotoImage(file=liens_correction)
cadre_image_correction = tk.Label(cadre_mot_possible,image=image_correction,width=220,height=45)

#================================================================
# relance le jeu en effacent les réponses et réaffiche les boutons
#================================================================

def relance_le_jeu():
    cadre_mot_possible.place_forget()
    for lettre_a_effacer in liste_emplacement_lettre:
        lettre_a_effacer.place_forget()
    bouton_entrer_ses_lettres.place(x=350,y=150)
    bouton_donne_les_lettres.place(x=200,y=150)
bouton_relance_le_jeu = tk.Button(cadre_mot_possible,text="relance une nouvelle partie",command=relance_le_jeu)

#========================================================================================
# crée la liste pour la listes déroulante
#========================================================================================

def affiche_les_mot_possible(liste_mot):
    cadre_jeu.place_forget()
    cadre_mot_possible.place(x=25,y=140)
    cadre_image_correction.place(x=250,y=0)
    bouton_relance_le_jeu.place(x=250,y=350)
    liste_mot_a_afficher = []
    vrai_mot = ""
    for mot in liste_mot:
        vrai_mot = ""
        for lettre in mot:
            if lettre in lettre_alphabet:
                vrai_mot = vrai_mot + lettre
        liste_mot_a_afficher.append(vrai_mot)
    creer_la_liste_deroulante(liste_mot_a_afficher)
    


listeCombo = ttk.Combobox(cadre_mot_possible,values=["VALEURS"])


#================================================================
# crée une liste déroulante avec les mots disponible elle va ensuite les affichers en bas 
#================================================================

def creer_la_liste_deroulante(liste):
    listeCombo = ttk.Combobox(cadre_mot_possible,values=liste)
    listeCombo.current(0)
    listeCombo.bind("<<ComboboxSelected>>", action)
    listeCombo.place(x=20,y=50)

def action(event,listeCombo):
    select = listeCombo.get()
    print("vous avez sélectionné",select)
    affiche_les_lettres(select)



root.mainloop()