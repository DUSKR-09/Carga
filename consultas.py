import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='carga')

cursor = connection.cursor()
codigo = """"""

print("Filtro:\n")
print("1. Codigo de Asociado\n")
print("2. Nombres\n")
print("3. Numero de Tarjeta\n") 
choice = input()

if choice == '1':
    print("Ingrese codigo de asociado")
    choice = input()
    codigo = """SELECT codigo, nombre, apellido1, apellido2, tcNum FROM movimientos WHERE codigo = '%s'""" % choice
    
if choice == '2':
    print('Ingrese un nombre')
    choice = input()
    codigo = """SELECT codigo, nombre, apellido1, apellido2, tcNum FROM movimientos WHERE nombre LIKE '%s'""" % choice
    

if choice == '3':
    print('Ingrese un numero de tarjeta')
    choice = input()
    codigo = """Select codigo, nombre, apellido1, apellido2, tcNum FROM movimientos WHERE tcNum = '%s'""" % choice
    
# mostrar
if len(codigo) > 0:
    cursor.execute(codigo)
    resultados = cursor.fetchall()

    if resultados:
        for resultado in resultados : 
            print(resultado)
    else:
        print("Sin Resultados")
else:
    print("Consulta Vacia")

cursor.close()
connection.close()