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
    argv = (sys.argv[4], )
    cur.execute(arg, argv)
    query_rows = cur.fetchall()
    strings = []
    for item in query_rows:
        strings.append(item[0])
    print(", ".join(strings))
    cur.close()
    conn.close()
