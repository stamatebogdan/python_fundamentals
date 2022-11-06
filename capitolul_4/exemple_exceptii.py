# val=int(input("Introduceti o valoare numerica: "))
# print(10/val)

# def suma_numerelor(a, b):
#     return a+b
#
# suma_numerelor(10, "20")

# print(":)")
# try:
#     x = int(input("Introduceti o valoare numerica: "))
#     print(10/x)
#     print(":(")
# except:
#     print("A introdus o valoare invalida pentru impartire ")
# print(":D")

# my_list=["java","python","javascript"]
# try:
#     print(":)")
#     print(my_list[100])
#     print(":(")
# except:
#     print("Ai accesat un index inexistent din lista")
# finally:
#     print("Instructiuni executate indiferent daca am exceptie sau nu.")

# try:
#     x=1
#     y=10/x
#     print("A")
#     my_list=[100, 200, 300]
#     my_list[0] = 100
#     my_dict={"cheie_1":100}
#     print(my_dict['cheie_1'])
#     z = int("lala")
# except ZeroDivisionError:
#     print("Ai incercat sa imparti la 0! Nu este permis!")
# except (IndexError,KeyError) as e:
#     print("Te-ai folosit de un index inexistent!")
#     print(repr(e))
# except KeyError:
#     print("Ai incercat sa accesezi o cheie ce nu este prezenta in dicitonar")
# except Exception as e: #se pune la sfarsit in cadrul unui bloc care face tratarea exceptiilor in cadrul programului
#     print("Exceptie generala!")
#     print(repr(e))

def radical(x):
    if x<=0:
        raise ValueError("Radicalul se poate aplica doar pe valori numerice pozitive.")

radical(25)
radical(-25)


