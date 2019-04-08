from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Questions, Base, Choices

engine = create_engine('sqlite:///test.db')
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


# Menu for UrbanBurger
q = Questions(title="dummy 1?",answer="karim")

session.add(q)
session.commit()

q = Questions(title="dummy 2?",answer="voila this is karim")

session.add(q)
session.commit()
q = Questions(title="dummy 3?",answer="karim again")

session.add(q)
session.commit()



c= Choices(choice = "yes",question_id="1")

session.add(c)
session.commit()

c= Choices(choice = "maybe",question_id="1")

session.add(c)
session.commit()

c= Choices(choice = "no",question_id="1")

session.add(c)
session.commit()

c= Choices(choice = "yes",question_id="2")

session.add(c)
session.commit()

c= Choices(choice = "maybe",question_id="2")

session.add(c)
session.commit()

c= Choices(choice = "no",question_id="2")

session.add(c)
session.commit()

c= Choices(choice = "yes",question_id="3")

session.add(c)
session.commit()

c= Choices(choice = "maybe",question_id="3")

session.add(c)
session.commit()

c= Choices(choice = "no",question_id="3")

session.add(c)
session.commit()

q = Questions(title="dummy 4?",answer="karim")

session.add(q)
session.commit()

q = Questions(title="dummy 5?",answer="voila this is karim")

session.add(q)
session.commit()
q = Questions(title="dummy 6?",answer="karim again")

session.add(q)
session.commit()



c= Choices(choice = "yes",question_id="4")

session.add(c)
session.commit()

c= Choices(choice = "maybe",question_id="4")

session.add(c)
session.commit()

c= Choices(choice = "no",question_id="4")

session.add(c)
session.commit()

c= Choices(choice = "yes",question_id="5")

session.add(c)
session.commit()

c= Choices(choice = "maybe",question_id="5")

session.add(c)
session.commit()

c= Choices(choice = "no",question_id="5")

session.add(c)
session.commit()

c= Choices(choice = "yes",question_id="6")

session.add(c)
session.commit()

c= Choices(choice = "maybe",question_id="6")

session.add(c)
session.commit()

c= Choices(choice = "no",question_id="6")

session.add(c)
session.commit()

print "added menu items!"
