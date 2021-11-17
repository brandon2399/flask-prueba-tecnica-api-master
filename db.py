from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#from config import connection_db

# Local host
#connection_db = "sqlite:///basedatos.db"
# user:password@host:port/database
connection_db = "postgresql://cqocmrzsxlmnrg:2c592f3a044258bc81352ae886c711a533aa733e7e05fc165021bb51a18e883d@ec2-44-198-236-169.compute-1.amazonaws.com:5432/d7r14pm8sff829"

Base = declarative_base()

engine = create_engine(connection_db)

Session = sessionmaker(bind=engine)

