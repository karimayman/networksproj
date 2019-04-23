from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Questions, Base, Choices

engine = create_engine('sqlite:///test.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()



q = Questions(title="Which cut flower is the most popular for purchase?",answer="Rose")

session.add(q)
session.commit()

q = Questions(title="Which flower has the smallest seeds?",answer="Orchid")

session.add(q)
session.commit()
q = Questions(title="Which flower symbolically means Beauty?",answer="Calla Lily")

session.add(q)
session.commit()



c= Choices(choice = "Rose",question_id="1")

session.add(c)
session.commit()

c= Choices(choice = "Lily",question_id="1")

session.add(c)
session.commit()

c= Choices(choice = "Tulip",question_id="1")

session.add(c)
session.commit()

c= Choices(choice = "Daffodil",question_id="2")

session.add(c)
session.commit()

c= Choices(choice = "Orchid",question_id="2")

session.add(c)
session.commit()

c= Choices(choice = "Sweet Pea",question_id="2")

session.add(c)
session.commit()

c= Choices(choice = "Honeysuckle",question_id="3")

session.add(c)
session.commit()

c= Choices(choice = "Gardenia",question_id="3")

session.add(c)
session.commit()

c= Choices(choice = "Calla Lily",question_id="3")

session.add(c)
session.commit()

q = Questions(title="What color rose would you send to someone to say: i am innocent and pure?",answer="White")

session.add(q)
session.commit()

q = Questions(title="The disc of this flower is made up of hundreds of tiny flowers:",answer="Daisy")

session.add(q)
session.commit()
q = Questions(title="What part of the flower is the corolla",answer="Petals")

session.add(q)
session.commit()
 

c= Choices(choice = "Pink",question_id="4")

session.add(c)
session.commit()

c= Choices(choice = "White",question_id="4")

session.add(c)
session.commit()

c= Choices(choice = "Yellow",question_id="4")

session.add(c)
session.commit()

c= Choices(choice = "Anemone",question_id="5")

session.add(c)
session.commit()

c= Choices(choice = "Gardenia",question_id="5")

session.add(c)
session.commit()

c= Choices(choice = "Daisy",question_id="5")

session.add(c)
session.commit()

c= Choices(choice = "Stamen",question_id="6")

session.add(c)
session.commit()

c= Choices(choice = "Petals",question_id="6")

session.add(c)
session.commit()

c= Choices(choice = "Pistil",question_id="6")

session.add(c)
session.commit()


q = Questions(title="What flower bulb can be used in place of onions in cooking?",answer="Tulip")

session.add(q)
session.commit()

q = Questions(title="Who said : where flowers bloom so does hope?",answer="Lady Bird Johnson")

session.add(q)
session.commit()
q = Questions(title="If a bride chooses pink roses for her wedding bouquet, what message is she conveying?",answer="Grace and Joy")

session.add(q)
session.commit()



c= Choices(choice = "Freesia",question_id="7")

session.add(c)
session.commit()

c= Choices(choice = "Tulip",question_id="7")

session.add(c)
session.commit()

c= Choices(choice = "Dahlia",question_id="7")

session.add(c)
session.commit()

c= Choices(choice = "Lady Bird Johnson",question_id="8")

session.add(c)
session.commit()

c= Choices(choice = "Shakespeare",question_id="8")

session.add(c)
session.commit()

c= Choices(choice = "Mother Teresa",question_id="8")

session.add(c)
session.commit()

c= Choices(choice = "Innocence and Purity",question_id="9")

session.add(c)
session.commit()

c= Choices(choice = "Modesty",question_id="9")

session.add(c)
session.commit()

c= Choices(choice = "Grace and Joy",question_id="9")

session.add(c)
session.commit()


q = Questions(title="Which is the biggest flower of the world?",answer="Rafflasia")

session.add(q)
session.commit()

q = Questions(title="There is a pretty little flower that shares its name with a musical instrument. Which is it?",answer="viola")

session.add(q)
session.commit()
q = Questions(title="Which of the following flowers changes colour from blue to pink according to the amount of acid in the soil?",answer="Hydrangea")

session.add(q)
session.commit()



c= Choices(choice = "Petunia",question_id="10")

session.add(c)
session.commit()

c= Choices(choice = "Lily",question_id="10")

session.add(c)
session.commit()

c= Choices(choice = "Rafflasia",question_id="10")

session.add(c)
session.commit()

c= Choices(choice = "Drumflower",question_id="11")

session.add(c)
session.commit()

c= Choices(choice = "Harp flower",question_id="11")

session.add(c)
session.commit()

c= Choices(choice = "Viola",question_id="11")

session.add(c)
session.commit()

c= Choices(choice = "Hydrangea",question_id="12")

session.add(c)
session.commit()

c= Choices(choice = "Daisies",question_id="12")

session.add(c)
session.commit()

c= Choices(choice = "Marigolds",question_id="12")

session.add(c)
session.commit()

q = Questions(title="There is a flower with a charming name that makes you think of Christmas. However, it doesn't bloom in December. What is it?",answer="Star Of Bethlehem")

session.add(q)
session.commit()

q = Questions(title="Which of the following flowers once caused a huge panic and made many people bankrupt?",answer="Tulip")

session.add(q)
session.commit()
q = Questions(title="Which flowers are the most popular spring flowers of all time?",answer="Tulips")

session.add(q)
session.commit()



c= Choices(choice = "Carolianthus",question_id="13")

session.add(c)
session.commit()

c= Choices(choice = "Star Of Bethlehem",question_id="13")

session.add(c)
session.commit()

c= Choices(choice = "Christmas Bush",question_id="13")

session.add(c)
session.commit()

c= Choices(choice = "Carnation",question_id="14")

session.add(c)
session.commit()

c= Choices(choice = "Tulip",question_id="14")

session.add(c)
session.commit()

c= Choices(choice = "Marygold",question_id="14")

session.add(c)
session.commit()

c= Choices(choice = "Tulips",question_id="15")

session.add(c)
session.commit()

c= Choices(choice = "Roses",question_id="15")

session.add(c)
session.commit()

c= Choices(choice = "SunFlowers",question_id="15")

session.add(c)
session.commit()

q = Questions(title="What is the genus name of sunflower?",answer="Helianthus")

session.add(q)
session.commit()

q = Questions(title="Which flowers are gifted to friends on Friendship Day?",answer="White Roses")

session.add(q)
session.commit()
q = Questions(title="Which of these flowers is the favorite of over 80 percent of people?",answer="Roses")

session.add(q)
session.commit()
 

c= Choices(choice = "Dianthus",question_id="13")

session.add(c)
session.commit()

c= Choices(choice = "Helianthus",question_id="13")

session.add(c)
session.commit()

c= Choices(choice = "Nelumbo",question_id="13")

session.add(c)
session.commit()

c= Choices(choice = "Yellow Roses",question_id="14")

session.add(c)
session.commit()

c= Choices(choice = "Pink Roses",question_id="14")

session.add(c)
session.commit()

c= Choices(choice = "White Roses",question_id="14")

session.add(c)
session.commit()

c= Choices(choice = "SunFlowers",question_id="15")

session.add(c)
session.commit()

c= Choices(choice = "Roses",question_id="15")

session.add(c)
session.commit()

c= Choices(choice = "Tulips",question_id="15")

session.add(c)
session.commit()

q = Questions(title="Saffron, the spice, comes from a type of which flower?",answer="Crocus")

session.add(q)
session.commit()

q = Questions(title="Which of these flowers does not need soil to grow?",answer="Orchids")

session.add(q)
session.commit()
q = Questions(title="Which flower was poisoned by the Wicked Witch in the Wizard of Oz?",answer="Poppy")

session.add(q)
session.commit()



c= Choices(choice = "Crocus",question_id="16")

session.add(c)
session.commit()

c= Choices(choice = "Magnolia",question_id="16")

session.add(c)
session.commit()

c= Choices(choice = "Iris",question_id="16")

session.add(c)
session.commit()

c= Choices(choice = "Lilies",question_id="17")

session.add(c)
session.commit()

c= Choices(choice = "Orchids",question_id="17")

session.add(c)
session.commit()

c= Choices(choice = "Lavender",question_id="17")

session.add(c)
session.commit()

c= Choices(choice = "Iris",question_id="18")

session.add(c)
session.commit()

c= Choices(choice = "Rose",question_id="18")

session.add(c)
session.commit()

c= Choices(choice = "Poppy",question_id="18")

session.add(c)
session.commit()


print "questions added successfully, ready, set , solve !"
