from yoyo import get_backend

def mysql(config):
    url = "mysql://"+config["user"]+":"+config["password"]+"@"+config["host"]+":"+config["port"]+"/"+config["name"]
    backend = get_backend(url)
    return backend