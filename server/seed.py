from server.app import app
from server.config import db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

with app.app_context():
    print("Clearing existing data...")
    RestaurantPizza.query.delete()
    Restaurant.query.delete()
    Pizza.query.delete()
    db.session.commit()
    print("Data cleared.")

    print("Seeding restaurants...")
    r1 = Restaurant(name="Pizza Palace", address="123 Main St")
    r2 = Restaurant(name="Domino's Pizza", address="456 Oak Ave")
    r3 = Restaurant(name="Little Italy", address="789 Pine Ln")
    db.session.add_all([r1, r2, r3])
    db.session.commit()
    print("Restaurants seeded.")

    print("Seeding pizzas...")
    p1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")
    p2 = Pizza(name="Pepperoni", ingredients="Pepperoni, Cheese, Tomato Sauce")
    p3 = Pizza(name="Veggie Delight", ingredients="Bell Peppers, Onions, Mushrooms, Olives")
    db.session.add_all([p1, p2, p3])
    db.session.commit()
    print("Pizzas seeded.")

    print("Seeding restaurant pizzas...")
    rp1 = RestaurantPizza(restaurant=r1, pizza=p1, price=15)
    rp2 = RestaurantPizza(restaurant=r1, pizza=p2, price=18)
    rp3 = RestaurantPizza(restaurant=r2, pizza=p2, price=16)
    rp4 = RestaurantPizza(restaurant=r3, pizza=p1, price=14)
    rp5 = RestaurantPizza(restaurant=r3, pizza=p3, price=20)
    db.session.add_all([rp1, rp2, rp3, rp4, rp5])
    db.session.commit()
    print("Restaurant pizzas seeded.")

    print("Database seeding complete!")