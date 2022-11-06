list=[0,1]

try:
    print(list[10])
except IndexError:
    print("Am ajuns in exceptia de index dorita")

try:
    raise IndexError
    print("Aici am ajuns")
except:
    print("Am ajuns in exceptia de index provocata de noi")

class TelacadException (Exception):
    pass

try:
    raise TelacadException
except TelacadException:
    print("Am ajuns in exceptia definita de noi")

try:
    raise IndexError
    print("Aici nu ajungem")
except:
    raise IndexError
    print("Aici nu am ajuns")
finally:
    print("Am ajuns aici chiar daca va fi aruncata exceptia IndexError")

