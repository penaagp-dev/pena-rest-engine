def docker_template(name):
    docker_files = """FROM python:alpine3.10
    #CDC start from here

    WORKDIR /usr/src/app

    COPY . .

    RUN apk add gcc musl-dev \
        && pip3 install -r requirements.txt \
        && pip install .

    EXPOSE 3000

    EXPOSE 3000

    CMD ["sh", "-c", """+name+"""]
    """
    return docker_files

def make_template(name, mode):
    make_files = """.PHONY: build deploy
    build:
        pip install pyinstaller
        pyinstaller main.py --distpath=./ --name=

    install:
        pip install -e .
    run:
        pena http serve
    """
    return make_files

def make_main():
    main_files = """from src.app import create_app, app
    from src.config import config
    from sys import exit
    import os, traceback

    def main():
        config()
        try:
            httpServe = create_app(app)
            httpServe.run(host=os.environ.get('APP_HOST', 'localhost'),
                port=int(os.environ.get('APP_PORT', 8081)))
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            exit(1)
        
    if __name__ == '__main__':
        main()
    """
    return main_files

def make_environment(name, mode, debug):
    mode = {
        "dev": "development",
        "stg": "staging",
        "prd": "production"
    }
    env_files = """APP_NAME="""+name+"""
    APP_HOST=127.0.0.1
    APP_PORT=8081
    SECRET_KEY=asdsagdasgdasf@asfdasgvdasda@#!@#!%$#%@#@@##
    FLASK_ENV="""+name+"""
    FLASK_DEBUG = True
    FLASK_REDIS_URL = redis://:pass@127.0.0.1:6379/0

    JWT_SECRET_KEY = wqertyudfgfhjhkcxvbnmn@123$32213

    DB_HOST=localhost
    DB_PORT=3306
    DB_USER=oni-flag-service
    DB_PASSWORD=oni-flag-service
    DB_NAME=oni-flag-service

    SWAGGER_URL = '/api/docs'
    SWAGGER_API_URL = 'http://petstore.swagger.io/v2/swagger.json'
    """
    return env_files