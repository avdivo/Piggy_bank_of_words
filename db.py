from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

# Создание БД
engine = create_engine('sqlite:///pbw.db', echo=True)
meta = MetaData()

# Создание таблиц
texts = Table(
   'texts', meta,
   Column('id', Integer, primary_key = True),
   Column('theme', String),
   Column('description', String),
)
meta.create_all(engine)