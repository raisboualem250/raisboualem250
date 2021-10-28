
chemin = r"C:\Users\kenzi\Documents\FORMATION_PYTHON\partie_02\fichier.txt"
with open(chemin,"r") as f: #for read
    #contenu = f.read() #get the content as it is 
    #contenu = repr(f.read()) #get the content and replace the new line by \n
    contenu = f.read().splitlines() #get the content and split it by lines
    #contenu = contenu.splitlines()
    print(contenu)

    #with open("fichier_txt", "r", encoding='utf-8') as f:
        #contenu = f.read()

with open(chemin,"w") as f:
    f.write("bonjour rais") # erase and write inside the file

with open(chemin,"r") as f:
    contenu = f.read()
    print(contenu)

with open(chemin,"a") as f: #a for append without erase
    f.write("\nby rais") # erase and write inside the file

with open(chemin,"r") as f:
    contenu = f.read()
    print(contenu)