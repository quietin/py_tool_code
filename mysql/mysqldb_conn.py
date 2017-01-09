# coding=utf-8
import MySQLdb

# example table `ship`
# +----------+---------+------+-----+---------+----------------+
# | Field    | Type    | Null | Key | Default | Extra          |
# +----------+---------+------+-----+---------+----------------+
# | id       | int(11) | NO   | PRI | NULL    | auto_increment |
# | cabin_id | int(11) | YES  | MUL | NULL    |                |
# | seattype | char(3) | YES  |     | NULL    |                |
# +----------+---------+------+-----+---------+----------------+


conn = MySQLdb.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='',
    db='faredb',
    charset="utf8"
)
cur = conn.cursor()
sql = "select * from ship where seattype = %s;"


def fetch_all():
    cur.execute(sql, 'B')
    columns = cur.description
    # fill into a list with `dict` elements
    result = [{columns[index][0]: column for index, column in enumerate(value)}
              for value in cur.fetchall()]
    # print result


def fetch_one():
    cur.execute(sql, 'G')
    # get columns with field name after `execute`
    columns = cur.description
    print columns
    one_tpl = cur.fetchone()
    mm = {columns[k][0]: one_tpl[k] for k in xrange(len(columns))}
    print mm


def insert():
    params = (99, 'M')
    # even the field is `int`, `%s` should be used in formatting
    insert_sql = "insert into ship(cabin_id, seattype) values (%s, %s);"
    try:
        cur.execute(insert_sql, params)
        conn.commit()
    except Exception as e:
        print 'commit fail:', e
        conn.rollback()


if __name__ == '__main__':
    fetch_one()
    insert()
    conn.close()
