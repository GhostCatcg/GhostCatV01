import sqlite3
import os

con = sqlite3.connect('DB\\message.db')
cur = con.cursor()

def write():

    cur.execute('CREATE TABLE message (id integer primary key ,name varchar(20),age integer)')

    cur.executemany('INSERT INTO message VALUES (?,?,?)', [(3,'GhostCat',19), (4,'GhostDog',26)])

    # 提交
    con.commit()

def read():
    cur.execute('SELECT * FROM message')
    res = cur.fetchall()
    for line in res:
        print("循环fetchall的值>>>", line)


def delete():
    cur.execute('UPDATE message SET name=? WHERE id=? ', ('GhostCat', 19))
    cur.execute('DELETE FROM message WHERE id=3')
    con.commit()



if __name__ == '__main__':

    write()
    # delete()
    read()


    con.close()
