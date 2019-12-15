#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    """
    filter name
    """
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           charset="utf8")
    cur = conn.cursor()

    arg = '''SELECT cities.name, states.id
        FROM cities, states
        WHERE cities.state_id=states.id
        AND states.name = %s
        ORDER BY id ASC;
        '''
    if len(sys.argv) > 5:
        x = sys.argv[4] + ' ' + sys.argv[5]
        argv = (x, )
    else:
        argv = (sys.argv[4], )
    cur.execute(arg, argv)
    query_rows = cur.fetchall()
    x = len(query_rows)
    flag = 0

    for row in query_rows:
        flag = 1
        if row != query_rows[x - 1]:
            print(row[0], end=", ")
        else:
            print(row[0], end="")
    if flag == 1:
        print()
    cur.close()
    conn.close()
