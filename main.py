i = 0
while i < 21:
    print(i)
    i += 2

i = 1   
while i < 21:
    print(f"voici le carre de {i} : {i*i}")
    i += 1
print("job 3 fini")
#N = string int = nombre eniter 
N = int(input("Entrez le nombre a multiplier : ")) 
for i in range (1,11): # 1 = que ça commence a partir de 1 #11 = jusqu'a 10
    print(f"{N} x {i} = {N * i}")

print("job 4 fini")

# debut job 5 "Transformer cette boucle for en boucle while afin d’obtenir le même résultat

for N in range(1, 13):
    print(N)
N = 1
while N < 13:
    print(N)
    N += 1
print("job 5 fini")

#job 6

N = int(input("entrez un entier N : "))
i = 1
while i <= 10:
    result = N * i
    print(f"{N} * {i} = {result}")
    i += 1




