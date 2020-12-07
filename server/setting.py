from decouple import config

database_url = config("DATABASE_URL", None)
debug = config("DEBUG")
secret_key = config("SECRET_KEY")
email = config("EMAIL")
password = config("password")

