 1) 
nome = input("Inserisci il tuo nome: ")
print (nome)

2)
nome = input("Inserisci il tuo nome: ")
cognome = input("Inserisci il tuo cognome: ")
print (nome , cognome)

3)
nome = input("Inserisci il tuo nome: ")
cognome = input("Inserisci il tuo cognome: ")
print (len(nome), len(cognome))

4)
x = input("Inserisci il primo numero: ")
y = input("Inserisci il secondo numero: ")

if x > y: print (x , y)
else: print (y, x)

5)
colore = input("Inserisci il tuo colore preferito: ")
if colore == "blu" or colore == "BLU" or colore == "Blu": print("Buono")
else: print("Non mi piace")

6)
nome = input("Inserisci il tuo nome: ")
c=0
while(c<3): 
  print(nome)
  c+=1

7)
nome = input("Inserisci il tuo nome: ")

for x in nome:
  print(x)

8)
frutta = ("Pera", "Banana", "Mela", "Mango")
print(frutta[2])

9)
frutta = ("Pera", "Banana", "Mela", "Mango")
print(frutta)
scelta = input("Scegli uno di questi quattro: ")
if scelta == "Pera": 
  print(frutta.index("Pera"))

if scelta == "Banana": 
  print(frutta.index("Banana"))

if scelta == "Mela": 
  print(frutta.index("Mela"))

if scelta == "Mango": 
  print(frutta.index("Mango"))

10)
list = ["Antonio", "Giuseppe" , "Francesco" , "Paolo", "Marco"]

c = 0
while c < len(list):
  print(list[c])
  c += 1

11)
list = ["Antonio", "Giuseppe" , "Francesco" , "Paolo", "Marco", "Andrea", "Stefano", "Diego", "Giovanna", "Filomena"]
list.sort()
c = 0
while c < len(list):
  print(list[c])
  c += 1