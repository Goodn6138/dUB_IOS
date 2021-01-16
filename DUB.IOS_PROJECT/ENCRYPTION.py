import sqlite3
key = '12345'

KEY_DB = 'config.db'
LOCK_DB = 'config_j_trx1.db'

DB = 'credential.db'

key = '1234'

def CRYPTION()
    try:
        conn = sqlite3.connect(KEY_DB)
        c = conn.cursor()
        c.execute('SELECT lock FROM entries WHERE null 1 = ?', (key,))
        data = c.fetchall()
        lock = data[0][0]
        conn.commit()
        conn.close()
        print('HUU HAA')
        error = True#si virgin
        8
    except sqlite3.OperationalError:
        error  = False #NI VIRGIN
        print("VIRGO")
        pass
    


