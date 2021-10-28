import operator
ops = {
    "+" : operator.add,
    "-" : operator.sub,
    "*" : operator.mul,
    "/" : operator.truediv,  # use operator.div for Python 2
    "%" : operator.mod,
}
dec_continue = "o"
liste_operations = ["*","+","/","%","-"]
while dec_continue == "o":
    #operand 01
    chiffre_1 = input("entrez le chiffre 1 : ")
    while(not chiffre_1.isdigit()):
        chiffre_1 = input("on accepte que les chiffres :")

    #operation
    operation = input("entrez l operation * / + - % :")
    while(operation not in liste_operations):
        operation = input("entrez une operation valide * / + - % :")

    #operand 02
    chiffre_2 = input("entrez le chiffre 2 : ")
    while(not chiffre_2.isdigit()):
        chiffre_2 = input("on accepte que les chiffres :")

    #tt va bien
    resultat = ops["+"](int(chiffre_1),int(chiffre_2))
    print(f"le resulte de {chiffre_1} {operation} {chiffre_2} est de : {resultat}")

    dec_continue = input("voulez vous continuer : ")
