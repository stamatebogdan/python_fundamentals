import random

# print(random.random())
# print(random.random())

# print(random.uniform(5,15.5))

# print(random.randint(-100, 100))

# print(random.randrange(0, 100, 7))

# cumparaturi=["televizor", "masina de calcat", "calculator", "aspirator"]
# print(random.choice(cumparaturi))

# valori_posibile = list(range(1,50))
# valori_extrase = random.sample(valori_posibile, 6)
# print(valori_extrase)

valori = [2,10,12,100,-50,24,123]
random.shuffle(valori)
print(valori)
