def est_premier(nombre):
    if nombre <= 1:
        return False
    for i in range(2, int(nombre**0.5) + 1):
        if nombre % i == 0:
            return False
    return True

def afficher_premiers_inferieurs_a(n):
    for i in range(2, n):
        if est_premier(i):
            print(i)

# Programme principal
if __name__ == "__main__":
    try:
        n = int(input("Entrez un entier n : "))
        afficher_premiers_inferieurs_a(n)
    except ValueError:
        print("Veuillez entrer un entier valide.")