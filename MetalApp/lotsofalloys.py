from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import BaseMetal, Base, Alloy, ClientInfo

engine = create_engine('postgresql+psycopg2://catalog:catalog@localhost/metalcatalog')
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

#Add User
newUser1 = ClientInfo(id = "1", username = "Nick Purington", email = "nickpurington@gmail.com", picture = "https://lh4.googleusercontent.com/-fUhBCupxjJA/AAAAAAAAAAI/AAAAAAAAAAk/K60p8iirx6E/photo.jpg")

session.add(newUser1)
session.commit()

#Types for Aluminium
basemetal1 = BaseMetal(id = "1", name = "Aluminium")

session.add(basemetal1)
session.commit()

alloy1 = Alloy(name = "Magnalium", id = "1", description = "Magnalium is an aluminium alloy with magnesium and small amounts of nickel and tin.  Some alloys, intended for particular uses at the cost of poor corrosion resistance, may consist of up to 50% magnesium.", basemetal_id = "1")

session.add(alloy1)
session.commit()


#Types for Chromium
basemetal2 = BaseMetal(id = "2", name = "Chromium")

session.add(basemetal2)
session.commit()

alloy2 = Alloy(name = "Nichrome", id = "2", description = "Nichrome (NiCr, nickel-chrome, chrome-nickel, etc.) is any of various alloys of nickel, chromium, and often iron (and possibly other elements). The most common usage is as resistance wire, although in a few other applications.", basemetal_id = "2")

session.add(alloy2)
session.commit()


#Types for Cobalt
basemetal3 = BaseMetal(id = "3", name = "Cobalt")

session.add(basemetal3)
session.commit()

alloy3 = Alloy(name = "Stellite", id = "3", description = "Stellite alloy is a range of cobalt-chromium alloys designed for wear resistance. It may also contain tungsten or molybdenum and a small but important amount of carbon.", basemetal_id = "3")

session.add(alloy3)
session.commit()


#Types for Copper
basemetal4 = BaseMetal(id = "4", name = "Copper")

session.add(basemetal4)
session.commit()

alloy4 = Alloy(name = "Brass", id = "4", description = "Brass is a metallic alloy that is made of copper and zinc. The proportions of zinc and copper can vary to create different types of brass alloys. It is a substitutional alloy", basemetal_id = "4")

session.add(alloy4)
session.commit()

#Types for Gold
basemetal5 = BaseMetal(id = "5", name = "Gold")

session.add(basemetal5)
session.commit()

alloy5 = Alloy(name = "Rose Gold", id = "5", description = "Rose gold is a gold-copper alloy widely used for specialized jewelry. Rose gold, also known as pink gold and red gold, was popular in Russia at the beginning of the nineteenth century.", basemetal_id = "5")

session.add(alloy5)
session.commit()

#Types for Iron
basemetal6 = BaseMetal(id = "6", name = "Iron")

session.add(basemetal6)
session.commit()

alloy6 = Alloy(name = "Cast Iron", id = "6", description = "Cast iron is a group of iron-carbon alloys with a carbon content greater than 2%. Grey cast iron has graphite flakes which deflect a passing crack and initiate new cracks as the material breaks, stopping the crack from further progressing.", basemetal_id = "6")

session.add(alloy6)
session.commit()

#Types for Lead
basemetal7 = BaseMetal(id = "7", name = "Lead")

session.add(basemetal7)
session.commit()

alloy7 = Alloy(name = "Solder", id = "7", description = "Solder is a fusible metal alloy used to create a permanent bond between metal workpieces. Solder used in making electrical connections also needs to have favorable electrical characteristics.", basemetal_id = "7")

session.add(alloy7)
session.commit()


#Types for Nickel
basemetal8 = BaseMetal(id = "8", name = "Nickel")

session.add(basemetal8)
session.commit()

alloy8 = Alloy(name = "Alumel", id = "8", description = "Alumel is an alloy consisting of approximately 95% nickel, 2% aluminum, 2% manganese, and 1% silicon. This magnetic alloy is used for thermocouples and thermocouple extension wire.", basemetal_id = "8")

session.add(alloy8)
session.commit()


#Types for Silver
basemetal9 = BaseMetal(id = "9", name = "Silver")

session.add(basemetal9)
session.commit()

alloy9 = Alloy(name = "Platinum Sterling", id = "9", description = "Platinum Sterling is a registered trademark name of ABI Precious Metals.  The range of Platinum Sterling alloys was developed in 2003 by Marc Robinson, and its solder was created by Chuck Bennett.", basemetal_id = "9")

session.add(alloy9)
session.commit()


#Types for Tin
basemetal10 = BaseMetal(id = "10", name = "Tin")

session.add(basemetal10)
session.commit()

alloy10 = Alloy(name = "Pewter", id = "10", description = "Pewter is a malleable metal alloy. It is traditionally composed of 85-99 percent tin, mixed with copper, antimony, bismuth, and sometimes lead.  Pewter had a low melting point, depending on the exact mixture of metals.", basemetal_id = "10")

session.add(alloy10)
session.commit()


print "Added new alloys! Ready to get started"
