import pymysql
import xlrd

book = xlrd.open_workbook('C:\carga\DataPrueba.xlsx')
sheet = book.sheet_by_index(0)

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='carga')

cursor = connection.cursor()
query = """INSERT INTO movimientos (codigo, nombre, apellido1, apellido2, tcNum, fchCon, monto, saldo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""


for r in range(1, sheet.nrows):
    codigo   = sheet.cell(r,0).value
    nombre   = sheet.cell(r,1).value
    apellido1 = sheet.cell(r,2).value
    apellido2 = sheet.cell(r,3).value
    numTarjeta = sheet.cell(r,4).value
    fchCon = xlrd.xldate_as_datetime(sheet.cell(r,5).value, book.datemode)
    monto = sheet.cell(r,6).value
    saldo = sheet.cell(r,7).value
    values = codigo, nombre, apellido1, apellido2, numTarjeta, fchCon, monto, saldo
    cursor.execute(query, values)

connection.commit()
cursor.close()
connection.close()