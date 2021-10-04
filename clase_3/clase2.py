# String

salto = "aay \nmarikito"

tab = '\t ta tabuladoy y ta tartamudo'

slash = '\\ slash invertido'

comilla = "\' comilla con slash, y ' comilla comun"

otra_comilla = '\" igual y " otra xd'

print(salto)
print(tab)
print(slash)
print(comilla)
print(otra_comilla)

prueba = 'epale'
print(prueba,len (prueba))


prueba = format(prueba,">10s")
print(prueba, len(prueba))


print( f'si te saludo te digo: {prueba}')
print( 'si te saludo te digo: {}'.format(prueba))
print( 'si te saludo te digo: {varibale}'.format(varibale = prueba))

# IF ELSE
num = input('número: ')

num = int(num)

if not num:
    print('y el número papá?')
else: #Chacer comentario sobre el elif
    if num >= 10:
        print('crack')
    else:
        print('efe por ti')


# OPERADOR TERNARIO
#  https://converter.website-dev.eu/

var = 0
#varibale = (condicion) ? resultado si se cumple : resultado sino se cumple
# resultado = (var == True) ? 'verdadero' : 'falso'

result = 'verdadero' if var == True else 'falso'
print(result)

# ejemplo de num
#impresion = !num ? ' y el num papá?' : num >=10 ? 'crack' : 'efe por ti' 

# $play = !empty($timeshift) ? $timeshift['pqt_tipo'] == 'TIMESHIFT' ? '0' : '1' : '1';
timeshift = ''
# play = 1 if bool(timeshift) == True else 0 if timeshift['pqt_tipo'] else 1
"""
if (isset($timeshift['pqt_tipo']) && $timeshift['pqt_tipo'] == 'TIMESHIFT') {
   $play = 0;
} else {
   $play = 1;
}
"""


# Revisar pagina 4 diapositivas
res = 's'

while res == 's':
    res = input('\nDesea continuar: [s/n]')

print('fin del while')

dicho = 'guerra avisada es porque el rio suena'

for letra in dicho :
    print(letra)

mi_lista = [0,1,2,3,4,5]
mi_tupla = ('si tu me ama', 'y yo te amo', 'vamo a amarno')
mi_dic = {
    'tu': 'mami gabi',
    'yo': 'el mas culino',
    'ambos': 'irrespetandonos'
} 



for valor in mi_lista:
    print('el valor es {0} pero si le sumo 2 entonces es {1}'.format(valor, valor+1))







for frase in mi_tupla:
    print(f'la frase del poema es {frase}')







for numero in range(1,20):
    if numero == 10 or numero == 15:
        continue
    print(numero)
print( 'fuera del continue')







for numero in range(1,20):
    if numero == 10 :
        break
    print(numero)
print('fuera del break')





# for no sirve para los dic
for lo_que_sea in mi_dic:
    print(f'la frase del poema es es {lo_que_sea}')