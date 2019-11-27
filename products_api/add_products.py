from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import Base, products
 
engine = create_engine('postgresql+psycopg2://products:products@localhost/products')
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
001 = products(Product Code = "001", Name = "Lavender Heart", Price = "9.25")

session.add(001)
session.commit()

#Second product
002 = products(Product Code = "002", Name = "Personalized Cufflinks", Price = "45.00")

session.add(002)
session.commit()

#Third product
003 = products(Product Code = "003", Name = "Kids T-shirt", Price = "19.95")

session.add(003)
session.commit()


print "Added new products! Ready to get started"
