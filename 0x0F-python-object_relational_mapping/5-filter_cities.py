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
    cur.execute(arg, (sys.argv[4], ))
    query_rows = cur.fetchall()
    x = len(query_rows) - 1
    for row in query_rows:
        if x != 0:
            if row != query_rows[x]:
                print(row[0], end=", ")
        else:
            print(row[0])
    cur.close()
    conn.close()
