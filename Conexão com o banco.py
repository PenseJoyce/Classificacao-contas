
"""
@author: Joyce
"""

import sqlite3

try :

# criação do banco 
    banco = sqlite3.connect("database.db")

# conectanto ao banco 
    cur = banco.cursor()

    print("conexão realizada com sucesso")

# salvar resultado em um dataframe 
    res = cur.execute("select * from levels")
    res.fetchall()

    df = cur.execute("select * from levels").to_dataframe()


   # banco.close()

except sqlite3.Error as erro:
    print("Erro ao conectar com o banco: ", erro)
