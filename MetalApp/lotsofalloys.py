from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import BaseMetal, Base, Alloy, Users
 
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


#Types for Aluminium
basemetal1 = BaseMetal(id = "100", name = "Aluminium")

session.add(basemetal1)
session.commit()

alloy1 = Alloy(name = "Magnalium", id = "100", description = "Magnalium is an aluminium alloy with magnesium and small amounts of nickel and tin.[1] Some alloys, intended for particular uses at the cost of poor corrosion resistance, may consist of up to 50% magnesium.")

session.add(alloy1)
session.commit()


#Types for Chromium
basemetal2 = BaseMetal(id = "200", name = "Chromium")

session.add(basemetal2)
session.commit()

alloy2 = Alloy(name = "Nichrome", id = "200", description = "Nichrome (NiCr, nickel-chrome, chrome-nickel, etc.) is any of various alloys of nickel, chromium, and often iron (and possibly other elements).")

session.add(alloy2)
session.commit()


#Types for Cobalt
basemetal3 = BaseMetal(id = "300", name = "Cobalt")

session.add(basemetal3)
session.commit()

alloy3 = Alloy(name = "Stellite", id = "300", description = "Stellite alloy is a range of cobalt-chromium alloys designed for wear resistance. It may also contain tungsten or molybdenum and a small but important amount of carbon.")

session.add(alloy3)
session.commit()


#Types for Copper
basemetal4 = BaseMetal(id = "400", name = "Copper")

session.add(basemetal4)
session.commit()

alloy4 = Alloy(name = "Brass", id = "400", description = "Brass is a metallic alloy that is made of copper and zinc. The proportions of zinc and copper can vary to create different types of brass alloys with varying mechanical and electrical properties.")

session.add(alloy4)
session.commit()

#Types for Gold
basemetal5 = BaseMetal(id = "500", name = "Gold")

session.add(basemetal5)
session.commit()

alloy5 = Alloy(name = "Rose Gold", id = "500", description = "Rose gold, also known as pink gold and red gold, was popular in Russia at the beginning of the nineteenth century, and was also known as Russian gold, although this term is now obsolete.")

session.add(alloy5)
session.commit()

#Types for Iron
basemetal6 = BaseMetal(id = "600", name = "Iron")

session.add(basemetal6)
session.commit()

alloy6 = Alloy(name = "Cast Iron", id = "600", description = "Cast iron is a group of iron-carbon alloys with a carbon content greater than 2%. Its usefulness derives from its relatively low melting temperature.")

session.add(alloy6)
session.commit()

#Types for Lead
basemetal7 = BaseMetal(id = "700", name = "Lead")

session.add(basemetal7)
session.commit()

alloy7 = Alloy(name = "Solder", id = "700", description = "Solder is a fusible metal alloy used to create a permanent bond between metal workpieces.  Solder used in making electrical connections also needs to have favorable electrical characteristics.")

session.add(alloy7)
session.commit()


#Types for Nickel
basemetal8 = BaseMetal(id = "800", name = "Nickel")

session.add(basemetal8)
session.commit()

alloy8 = Alloy(name = "Alumel", id = "800", description = "Alumel is an alloy consisting of approximately 95% nickel, 2% aluminum, 2% manganese, and 1% silicon. This magnetic alloy is used for thermocouples and thermocouple extension wire.")

session.add(alloy8)
session.commit()


#Types for Silver
basemetal9 = BaseMetal(id = "900", name = "Silver")

session.add(basemetal9)
session.commit()

alloy9 = Alloy(name = "Platinum Sterling", id = "900", description = "Platinum Sterling is a registered trademark name of ABI Precious Metals, Inc. The range of Platinum Sterling alloys was developed in 2003 by Marc Robinson, and its solder was created by Chuck Bennett.")

session.add(alloy9)
session.commit()


#Types for Tin
basemetal10 = BaseMetal(id = "1000", name = "Tin")

session.add(basemetal10)
session.commit()

alloy10 = Alloy(name = "Pewter", id = "1000", description = "Pewter is a malleable metal alloy. It is traditionally composed of 85-99 percent tin, mixed with copper, antimony, bismuth, and sometimes lead, although the use of lead is less common today.")

session.add(alloy10)
session.commit()


print "Added new alloys! Ready to get started"
