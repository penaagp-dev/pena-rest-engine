from src.app.repository import conn


def insert(data):
    try:
        conn.execute("")
    except Exception as e:
        print("error:>", e)
        return e
    else:
        print(data)
        return data