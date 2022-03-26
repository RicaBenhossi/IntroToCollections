# The default parameter as bellow is not good beacuse var lista will be created only in the first call. Every subsequent
# call will reuse that same memory and will increase the list Lista
def processa_lista1(lista=[]):
    print('processa_lista1')
    print(len(lista))
    print(lista)
    lista.append(13)


# When you have mutable objects (list in this case) the best practice is always set the default as None. This way
# it will not reuse the same object
def processa_lista2(lista=None):
    print('processa_lista2')
    if lista is None:
        lista = list()
    print(len(lista))
    print(lista)
    lista.append(13)


idades = [30, 39, 27, 1, 15]
print(idades)
# shows the ammount of items in the list.
print(len(idades))
print(idades[1])
# add a value at the end of the list
idades.append(15)
print(idades)
# itrates in all item of the list
for idade in idades:
    print(idade)

# Remove the first apperance of 30 in the list
idades.remove(30)
# Error because there is no 30 in the list
# idades.remove(30)
# removes all items in the list
idades.clear()
print(idades)
# false because not exists
print(28 in idades)
# true
print(15 in idades)
if 15 in idades:
    idades.remove(15)

idades = [39, 18]
print(idades)
# Inster a new value in the position you pass
idades.insert(0, 20)
print(idades)
# add n elements to the list
idades.extend([27, 19])
print((idades))
# New list with idades + 1 using list comprehension
idades_no_ano_que_vem = [(idade + 1) for idade in idades]
print(idades)
print(idades_no_ano_que_vem)
print([(idade) for idade in idades if idade > 21])

processa_lista1()
processa_lista1()
processa_lista1()

processa_lista2()
processa_lista2()
processa_lista2()
