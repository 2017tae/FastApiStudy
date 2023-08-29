from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from starlette.config import Config

config = Config(".env")
# 데이터베이스 접속 주소
DB_URL = config('DATABASE_URL')

class engineconn:
    def __init__(self):
        self.engine = create_engine(DB_URL, pool_recycle=500)
    def sessionmaker(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session
    def connection(self):
        conn = self.engine.connect()
        return conn

Base = declarative_base()