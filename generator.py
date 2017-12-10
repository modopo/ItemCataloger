from .app.db_setup import db_session, User, Categories, Items

user1 = User(name = 'Jon Smith', email = 'jonsmith@gmail.com')
db_session.add(user1)
db_session.commit()

user2 = User(name = 'Jane Dane', email = 'janedane@gmail.com')
db_session.add(user2)
db_session.commit()

category1 = Categories(name = 'Soccer', user = user1)
db_session.add(category1)
db_session.commit()

category2 = Categories(name = 'Badminton', user = user2)
db_session.add(category2)
db_session.commit()

category3 = Categories(name = 'Basketball', user = user1)
db_session.add(category3)
db_session.commit()

category4 = Categories(name = 'Tennis', user = user2)
db_session.add(category4)
db_session.commit()

item1 = Items(name = 'Soccer Ball',
              description = 'A ball to use for soccer. Typically black and '
                            'white hexagon patterns',
              category = category1, user = user1)
db_session.add(item1)
db_session.commit()

item2 = Items(name = 'Yonex Racket',
             description = 'A racket made for badminton by a racket company '
                           'called Yonex',
             category = category2, user = user2)
db_session.add(item2)
db_session.commit()

item3 = Items(name = 'Basketball',
              description = 'A typical brown-red bouncy ball used for a '
                            'basketball',
              category = category3, user = user1)
db_session.add(item3)
db_session.commit()

item4 = Items(name = 'Wilson racket',
              description = 'A racket made for tennis by a sport equipment '
                            'company Wilson',
              category = category4, user = user2)
db_session.add(item4)
db_session.commit()

