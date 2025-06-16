from ..config import db 

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)

    restaurant_pizzas = db.relationship('RestaurantPizza', backref='restaurant', cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Restaurant {self.id}: {self.name}>'

    def to_dict(self, include_pizzas=False):
        data = {
            "id": self.id,
            "name": self.name,
            "address": self.address
        }
        if include_pizzas:
            data['pizzas'] = [rp.pizza.to_dict() for rp in self.restaurant_pizzas]
        return data