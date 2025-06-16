from flask import Blueprint, request, jsonify, make_response
from ..models.restaurant_pizza import RestaurantPizza
from ..models.restaurant import Restaurant
from ..models.pizza import Pizza
from ..config import db
from sqlalchemy.exc import IntegrityError

restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    try:
        new_restaurant_pizza = RestaurantPizza(
            price=price,
            pizza_id=pizza_id,
            restaurant_id=restaurant_id
        )
        db.session.add(new_restaurant_pizza)
        db.session.commit()

        created_rp = RestaurantPizza.query.get(new_restaurant_pizza.id)

        return make_response(jsonify(created_rp.to_dict()), 201)
    except ValueError as e:
        db.session.rollback()
        return make_response(jsonify({"errors": [str(e)]}), 400)
    except IntegrityError:
        db.session.rollback()
        return make_response(jsonify({"errors": ["Invalid pizza_id or restaurant_id"]}), 400)
    except Exception as e:
        db.session.rollback()
        return make_response(jsonify({"errors": [f"An unexpected error occurred: {str(e)}"]}), 500)