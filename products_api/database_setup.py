from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine



Base = declarative_base()
    

class product(Base):
    __tablename__ = 'products'

    Product Code = Column(Integer, primary_key=True)
    Name = Column(String(250), nullable=False)
    Price = Column(Numeric (5, 2), nullable=False)
    

    @property
    def serialize(self):
        """Return object data in serializeable format"""
        return {
            'Product Code': self.Product Code,
            'Name': self.Name,
            'Price': self.Price,
        }


engine = create_engine('postgresql+psycopg2://products:products@localhost/products')


Base.metadata.create_all(engine)
