from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine



Base = declarative_base()
    

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    price = Column(Integer, nullable=False)
    name = Column(String(250), nullable=False)
    

    @property
    def serialize(self):
        """Return object data in serializeable format"""
        return {
            'id': self.id,
            'price': self.price,
            'name': self.name
        }


engine = create_engine('postgresql+psycopg2://products_user:U$er@localhost/postgres')


Base.metadata.create_all(engine)
