from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import Base, Product
 
engine = create_engine('postgresql+psycopg2://products_user:U$er@localhost/postgres')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


#First product
product1 = Product(name = "Lavender heart", price = "9.25")

session.add(product1)
session.commit()

#Second product
product2 = Product(name = "Personalized cufflinks", price = "45.00")

session.add(product2)
session.commit()

#Third product
product3 = Product(name = "Kids T-shirt", price = "19.95")

session.add(product3)
session.commit()


print "Added new products! Ready to get started"
