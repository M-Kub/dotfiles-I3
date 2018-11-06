import csv

bücher = {}


def buch_daten(bücher):
    while True:
        Autor = input("Bitte Namen des Autors eingeben! ")
        Titel = input("Bitte den Titel des Buches eingeben! ")
        bücher[Autor] = Titel
        
        weiter = input("Noch etwas hinzufügen? (y/n)")
        if weiter == "y":
            continue
        elif weiter == "n":
            print("Danke für die Eingabe:")
            break
        else:
            print("Falsche Eingabe, dass Programm wird beendet.")
            break

    outputFile = open("books.csv", "a", newline="")
    fieldnames = ["Autor", "Titel"]
    outputWriter = csv.DictWriter(outputFile, fieldnames=fieldnames, delimiter="\t")
    for key, val in bücher.items():
        #outputWriter.writeheader()
        outputWriter.writerow({"Autor" : key, "Titel" : val})

        #f.write(f"{key}, {val},\n")
        #w.writerow([key, val])
        #print(f"Der Autor {key} und der Titel {val} wurden der Datei hinzugefügt.")

buch_daten(bücher)
