import sqlite3


def createTable(db, table, attrTypes):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    sql_query = "CREATE TABLE IF NOT EXISTS {} {}".format(table, attrTypes)
    cur.execute(sql_query)
    conn.commit()
    conn.close()

def insertData(db,table, attrValues):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    sql_query = "INSERT INTO {} VALUES {}".format(table, attrValues)
    cur.execute(sql_query)
    conn.commit()
    conn.close()

def view(db,table):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    sql_query = "SELECT * FROM {}".format(table)
    cur.execute(sql_query)
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(db, table, attr, value):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    sql_query = "DELETE FROM {} WHERE {} = {}".format(table, attr, value)
    cur.execute(sql_query)
    conn.commit()
    conn.close()

def update(db, table, attrType, attrVal, refType, refVal):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    sql_query = "UPDATE {} SET {} = {} WHERE {} = {}".format(table, attrType, attrVal, refType, refVal)
    cur.execute(sql_query)
    conn.commit()
    conn.close()
