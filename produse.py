# dictionary
# remove(name) si pop(pozitie)
import os

os.system('cls')
produs = {
    1: ["lapte", 5, 10],
    2: ["paine", 3, 20],
}

def afiseaza_produs(produs):
    for key, value in produs.items():
        print(f"Produs #{key}: {value[0]} - Pret Total: {value[1]*value[2]}, Cantitate: {value[2]}")

def adauga_produs(n):
    global cheie
    cheie = len(produs) + 1
    for i in range(n):
        nume = input("Numele produsului: ")
        pret = float(input("Pretul produsului: "))
        cantitate = int(input("Cantitatea produsului: "))
        produs[cheie] = [nume, pret, cantitate]
        cheie += 1

n = int(input("Cate produse vrei sa adaugi? "))
adauga_produs(n)
afiseaza_produs(produs)
print(f"Numar Elemente: {cheie-1}")