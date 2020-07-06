from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
ENGINE = create_engine("postgresql://zl:zlpw@localhost:5432/main", echo=True)


class People(Base):
    __tablename__ = "people"
    person_id = Column("id", Integer, primary_key=True)
    name = Column("name", String)


Base.metadata.create_all(bind=ENGINE)


