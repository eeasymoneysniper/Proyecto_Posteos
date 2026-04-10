from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy import create_engine


SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:Easymoney4605444.@localhost/usuarios"


Base = declarative_base()

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
