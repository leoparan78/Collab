

class humain():

    def __init__():
        # executer l'action user_input
        user_input()

    def marcher():
        # marcher
        print("\n--- Combien souhaitez-vous que l'humain fasse de pas ?")
        marcher = ""
        while not marcher.isdigit():
            reponse = print("Rentrez un nombre valable.")
            marcher = (input("Nombre de pas : "))
        marcher = int(marcher)
        print("L'humain a fait", marcher, "pas.")

    def donner_un_ordre():
        # donner un ordre
        print("\n--- Quel ordre voulez-vous que l'humain donne au robot ? (faire le ménage, faire la vaisselle ou faire la cuisine) ")
        donner_un_ordre = ""
        if donner_un_ordre == "faire le ménage":
            print("L'humain a donné l'ordre au robot de faire le ménage.")
        elif donner_un_ordre == "faire la vaisselle":
            print("L'humain a donné l'ordre au robot de faire la vaisselle.")
        elif donner_un_ordre == "faire la cuisine":
            print("L'humain a donné l'ordre au robot de faire la cuisine.")
        else:
            print("Rentrez une action valide.")

    def superviser():
        # superviser
        print("\n--- Quel ordre voulez-vous que l'humain vérifie ? (faire le ménage, faire la vaisselle ou faire la cuisine)")
        superviser = ""
        if superviser == "faire le ménage":
            print("L'humain vérifie si le robot a bien fait le ménage.")
        elif superviser == "faire la vaisselle":
            print("L'humain vérifie si le robot a bien fait la vaisselle.")
        elif superviser == "faire la cuisine":
            print("L'humain vérifie si le robot a bien fait la cuisine.")
        else:
            print("Rentrez une action valide.")

    def user_input():
        user_input = (input("Saisissez 1 action (marcher, donner un ordre ou superviser) : "))
        if user_input == "marcher":
            marcher()
        elif user_input == "donner un ordre":
            donner_un_ordre()
        elif user_input == "superviser":
            superviser()
        else:
            print("Rentrez une action valide.")