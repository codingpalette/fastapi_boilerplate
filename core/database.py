from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from config import conf
from typing_extensions import Annotated
from sqlalchemy.orm import Session, sessionmaker

config = conf()
# 디비종류//유저이름:비밀번호@호스트:포트/디비이름
DATABASE_URL = f"mysql+pymysql://{config['DB_USER']}:{config['DB_PASS']}@{config['DB_HOST']}:{config['DB_PORT']}/{config['DB_NAME']}"  # 또는 다른 데이터베이스 URL

engine = create_engine(DATABASE_URL, echo=False)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Annotated를 사용하여 의존성 주입
db_session = Annotated[Session, Depends(get_db)]
