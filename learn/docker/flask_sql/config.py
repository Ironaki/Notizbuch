import os


user = os.environ["POSTGRES_USER"]
password = os.environ["POSTGRES_PASSWORD"]
host = os.environ["POSTGRES_HOST"]
database = os.environ["POSTGRES_DB"]
port = os.environ["POSTGRES_PORT"]

DATABASE_CONNECTION_URI = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"

# POSTGRES_USER="admin"
# POSTGRES_PASSWORD="pw"
# POSTGRES_HOST="localhost"
# POSTGRES_PORT=5432
# POSTGRES_DB="example"

# DATABASE_CONNECTION_URI = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
