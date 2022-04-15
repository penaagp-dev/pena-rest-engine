from src.app.repository import conn

cur = conn.cursor()
def insert():
    try:
        cur.execute("SELECT * FROM guest")
    except Exception as e:
        raise e
    else:
        return cur.fetchall()

