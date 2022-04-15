from src.app.repository import conn, curr


def insert(data):
    try:
        curr.execute("SELECT * FROM guest")
    except Exception as e:
        print("error:>", e)
        return e
    else:
        print(data)
        return data