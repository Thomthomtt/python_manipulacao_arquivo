'''
#Testar erro de #NameError#
try:
    print(x)
except NameError:
    print("Erroooouuu")'''

'''
#Testar erro de #TypeError#

try:
    soma=1+"b"
    print(soma)
except TypeError:
    print("Errrrooouuuuuu!!!")'''

'''
#Testar erro de #IndexError#

try:
    lista=[0,1,2]
    print(lista[4])
except IndexError:
    print("TA ERRRADDOOO!!")'''

'''
#Testar error de #KeyError#

try:
    lista = {"Animal": "Gato",
         "Local": "fazenda"}
    print(lista["Semana"])
except KeyError:
    print("Burroooo ta errradddoo")'''

'''
#Testar error de #AttributeError#

try:
    frase="Suas Bolas Estão Murchas"
    print(frase.append)
except AttributeError:
    print("Muito burro filho kk")'''

'''
#Testar error de #ValueError#
try:
    valor=int("gatinha")
    print(valor)
except ValueError:
    print("Burro demaiiis")'''
