import builtins

print(open is builtins.open)

open="Variabila open globala modulului, care face override unei variabile builtin"

print(open)

def func():
    print(open)

def func2():
    open = "Variabila open locala functiei"
    print(open)

func()
func2()

print(open is builtins.open)

