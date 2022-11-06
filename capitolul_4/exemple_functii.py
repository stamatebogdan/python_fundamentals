def par_impar(x:int):
    if x % 2 == 0:
        print("Valoarea este para")
    else:
        print("Valoarea este impara")


# par_impar(102)
# par_impar(103)
# val=5
# print(par_impar(val))

# par_impar("abcd")

# def is_par(value: int) -> bool:
    # return value % 2 ==0
    # if value % 2 ==0:
    #     return True
    #     # print("Valoarea este para")
    # # else:
    #     return False

# print(is_par(100))
# res = is_par(101)
# print(res)

def suma_nr(x, y):
        return x+y

# print(suma_nr(10, 15))
# print(suma_nr(10.5, 12.7))
# print(suma_nr("HELLO", " WORLD"))
# print(suma_nr([1,2,3], [4,5,6]))

def patrat_cub(x):
    patrat = x ** 2
    cub = x ** 3
    return patrat, cub

# val = 5
# res = patrat_cub(5)
# print(res)
# print("Patratul este: " + str(res[0]))
# print("Cubul este: " + str(res[1]))
# print(type(res))

def suma_numerelor(*args):
    print(args)
    print(type(args))
    my_sum=0
    for i in args:
        my_sum += i
    return my_sum

# print(suma_numerelor(10, 20, 45, 101))
# print(suma_numerelor(1,2,3,4,5,6,7,8,9,10))
# print(suma_numerelor())

def my_function(**kwargs):
    print(kwargs)
    print(type(kwargs))
    print(kwargs.values())
    print(kwargs.keys())

# my_function(cheie1 = 10, cheie2 = 20, cheie3= 30)
# my_function(cheie_10=100)
# my_function()

def calculeaza_suma(a, b=50):
    return a+b

print(calculeaza_suma(10, 20))
print(calculeaza_suma(70))
print(calculeaza_suma(b=20, a=30))


