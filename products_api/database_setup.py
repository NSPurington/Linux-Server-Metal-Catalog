from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_context
import random, string
from itsdangerous import(TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

Base = declarative_base()
secret_key = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(32), index=True)
    picture = Column(String)
    email = Column(String)
    

class BaseMetal(Base):
    __tablename__ = 'basemetal'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    users_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE', onupdate='CASCADE'))
    users = relationship(Users)

    @property
    def serialize(self):
        """Return object data in serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }


class Alloy(Base):
    __tablename__ = 'alloy'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    basemetal_id = Column(Integer, ForeignKey('basemetal.id', ondelete='CASCADE', onupdate='CASCADE'))
    basemetal = relationship(BaseMetal)
    users_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE', onupdate='CASCADE'))
    users = relationship(Users)

    @property
    def serialize(self):
        """Return object data in serializeable format"""
        return {
            'name': self.name,
            'description': self.description,
        }


engine = create_engine('postgresql+psycopg2://catalog:catalog@localhost/metalcatalog')


Base.metadata.create_all(engine)
