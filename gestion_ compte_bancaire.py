import random
import csv
### FONCTIONS

Client = {}
Compte = {}
ClientCompte = {}


def ajouterClient(numCl, MPC, numC, SoldeC):
    Client[numCl] = MPC
    Compte[numC] = SoldeC
    ClientCompte[numCl] = numC

def supprimerClient(numC):
    del Compte[ClientCompte[numC]]
    del ClientCompte[numC]
    del Client[numC]

def modifierMPClient (numCl,newMP,MPC):
    oldMP=input("entrer ancien mot de passe")
    if oldMP == MPC:
       Client[numCl]=newMP

def deposer(numCl,montant):
  Compte[ClientCompte[numCl]] += montant
  
def retirer(numCl ,montant):
    
      if  Compte[ClientCompte[numCl]] >= montant:
          Compte[ClientCompte[numCl]] -= montant

      else:  
          print('solde insuffisant.')

genererNumbercompte =lambda numCl:int(str(numCl)+ str(random.randint(0,100)))

def ecrirefichierCSV():
    with open("client.csv","w",newline="") as csvfile:
       fieldnames=["numero client","code secret"]
       writer =csv.DictWriter(csvfile, fieldnames=fieldnames)
       writer.writeheader()
       for numCl ,codeSecret in Client.items():
           writer.writerow({"numeroclient":numCl,"codeSecret":codeSecret})


def manipSTS ():
    list = list (ClientCompte.values())
    tuple = tuple(ClientCompte.values())
    set = set(ClientCompte.values())
    return list, tuple, set
### main program

while True:
    print("1. Agent ")
    print("2. Client ")
    choix = int(input("Entrez votre choix: "))

    if choix == 1:
        print("1. Ajouter un compte")
        print("2. Supprimer un compte")
        agent_choix = int(input("Entrez votre choix: "))

        if agent_choix == 1:
            numCl = int(input("Entrez le numéro du nouveau client: "))
            MPC = input("Entrez le code secret du nouveau client: ")
            numC = genererNumbercompte(numCl)
            SoldeC = float(input("Entrez le solde initial de son compte: "))
            ajouterClient(numCl, MPC, numC, SoldeC)
            print("Compte ajouté avec succès.")

        elif agent_choix == 2:
            numC = int(input("Entrez le numéro du compte à supprimer: "))
            supprimerClient(numC)
            print("Compte supprimé avec succès.")

    elif choix == 2:
        numCl = int(input("Entrez votre numéro de client: "))
        print("1. Modifier le mot de passe")
        print("2. Afficher le solde")
        print("3. Déposer de l'argent")
        print("4. Retirer de l'argent")
        client_choix = int(input("Entrez votre choix: "))

        if client_choix == 1:
            newMP = input("Entrez le nouveau mot de passe: ")
            modifierMPClient(numCl, newMP)
            print("Mot de passe modifié avec succès.")

        elif client_choix == 2:
            print("Solde actuel: ", Compte[ClientCompte[numCl]])

        elif client_choix == 3:
            montant = float(input("Entrez le montant à déposer: "))
            deposer(numCl, montant)
            print("Dépôt effectué avec succès.")

        elif client_choix == 4:
            montant = float(input("Entrez le montant à retirer: "))
            retirer(numCl, montant)
            print("Retrait effectué avec succès.")

      



 