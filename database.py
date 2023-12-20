import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(f"sqlite:///Shipments_DataBase.db", echo=True)
if engine:
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


    def get_db():
        """Get session for DB"""
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()
else:
    raise ConnectionError("Failed to connect")
