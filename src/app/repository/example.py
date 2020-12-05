from src.app.repository import __cursor__ as curr


def insert(data):
    try:
        curr.execute("")
    except Exception as e:
        print("error:>", e)
        return e
    else:
        print(data)
        return data