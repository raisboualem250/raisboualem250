
liste = []

choix = 1
liste_choix = ["1","2","3","4","5"]

while choix != 5:

    #menu des choix
    print("1. Ajouter un élément à la liste de courses")
    print("2. Retirer un élément de la liste de courses")
    print("3. Afficher les éléments de la liste de courses")
    print("4. Vider la liste de courses")
    print("5. Quitter le programme")
    choix = input("votre choix : ")

    if ( choix not in liste_choix ):
        print("on accepte que les choix 1.2.3.4.5")  

    if choix == "1" :
        element = input("entrer votre nouveau element : ")
        liste.append(element)
        print(f"l'element {element} a bien été ajouté ")

    if choix == "2" :
        element = input("entrer l'element a supprimer : ")
        if(element in liste):
            liste.remove(element)
            print(f"l'element {element} a été bien supprimé ")
        else :
            print(f"l'element {element} n'est pas dans la liste")

    if choix == "3" :
        if(len(liste) > 0):
            for i, element in enumerate(liste):
                print(i+1, element)
        else:
            print("laliste est vide...!!")

    if choix == "4" :
        liste.clear()
        print("la liste a bien été vidé")
    
    if choix == "5" :
        print("au revoir")
        print("___________________________________________")
        break


    print("___________________________________________")
    #for i, element in enumerate(liste):
    #    print(i+1, element)
    
