import pymysql
import random

db1 = pymysql.connect('localhost', 'root', '010203')


def createdb():
    if db1:
        cursor = db1.cursor()

        # create database if not exists
        cursor.execute('create database if not exists db1;')

        db1.commit()

        # select database
        cursor.execute('use db1;')

        db1.commit()

        # create table if not exists
        cursor.execute('create table if not exists tbl1('
                       'id int unsigned auto_increment,'
                       'name varchar(32) not null,'
                       'sex char(1) not null,'
                       'pNumber varchar(32),'
                       'primary key(id));')

        db1.commit()

        # add
        # name
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        c = 0
        name = ''
        while c < 5:
            c += 1
            name += random.choice(alpha)

        # sex
        sex = random.randint(0, 1)
        if 1 == sex:
            sex = 'm'
        elif 0 == sex:
            sex = 'f'

        # phoneNubmer
        c = 0
        p_number = '1'
        while c < 10:
            c += 1
            p_number += str(random.randint(0, 9))

        cursor.execute('insert into tbl1 '
                       '(name, sex, pNumber) values'
                       '("%s", "%s", "%s");' % (name, sex, p_number))

        db1.commit()

        # # delete
        # cursor.execute('delete from tbl1 where id = 1')
        #
        # db1.commit()

        # update
        cursor.execute('update tbl1 set pNumber = "18001289144" where id = 1')

        db1.commit()

        # query
        cursor.execute('select * from tbl1;')

        for row in cursor.fetchall():
            print(row, end=' ')
            print()

        # close
        db1.close()


if __name__ == '__main__':
    createdb()
