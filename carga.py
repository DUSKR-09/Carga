import pymysql
import xlrd

book = xlrd.open_workbook('C:\carga\DataPrueba.xlsx')
sheet = book.sheet_by_index(0)

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='carga')

cursor = connection.cursor()
query = """INSERT INTO movimientos (codigo, nombre, apellido1, apellido2, tc, fch_con, monto, saldo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""

print(sheet.cell_value(1, 1))
