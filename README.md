#  Pizza Restaurant API

A RESTful API for managing a pizza restaurant. Built using Flask with MVC structure, SQLAlchemy models, and validated endpoints. Postman collection included for easy testing.

---

##  Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/pizza-api-challenge.git
cd pizza-api-challenge
```

### 2. Create and Activate a Virtual Environment
```bash
pipenv install flask flask_sqlalchemy flask_migrate
pipenv shell
```

### 3. Run Database Migrations
```bash
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 4. Seed the Database
```bash
python server/seed.py
```

---

##  Project Structure (MVC)
```
pizza-api-challenge/
├── server/
│   ├── app.py
│   ├── config.py
│   ├── seed.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── restaurant.py
│   │   ├── pizza.py
│   │   └── restaurant_pizza.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── restaurant_controller.py
│   │   ├── pizza_controller.py
│   │   └── restaurant_pizza_controller.py
├── migrations/
├── challenge-1-pizzas.postman_collection.json
└── README.md
```

---

## API Endpoints

###  GET /restaurants
Returns a list of all restaurants.
```json
[
  { "id": 1, "name": "Domino's", "address": "123 Street" },
  { "id": 2, "name": "Pizza Inn", "address": "456 Lane" }
]
```

###  GET /restaurants/<int:id>
Returns a restaurant with its pizzas.
```json
{
  "id": 1,
  "name": "Domino's",
  "address": "123 Street",
  "pizzas": [
    { "id": 1, "name": "Pepperoni", "ingredients": "Tomato, Cheese, Pepperoni" }
  ]
}
```
If not found:
```json
{ "error": "Restaurant not found" }
```

###  DELETE /restaurants/<int:id>
Deletes a restaurant and its related restaurant_pizzas.
- **Success:** 204 No Content
- **Not found:** 404
```json
{ "error": "Restaurant not found" }
```

###  GET /pizzas
Returns all pizzas.
```json
[
  { "id": 1, "name": "Veggie", "ingredients": "Tomato, Onion, Capsicum" },
  { "id": 2, "name": "Cheese", "ingredients": "Cheese, Tomato Sauce" }
]
```

###  POST /restaurant_pizzas
Creates a new restaurant-pizza relationship.

**Request:**
```json
{ "price": 10, "pizza_id": 1, "restaurant_id": 2 }
```

**Success Response:**
```json
{
  "id": 3,
  "price": 10,
  "pizza_id": 1,
  "restaurant_id": 2,
  "pizza": {
    "id": 1,
    "name": "Veggie",
    "ingredients": "Tomato, Onion, Capsicum"
  },
  "restaurant": {
    "id": 2,
    "name": "Pizza Inn",
    "address": "456 Lane"
  }
}
```

**Error Response:**
```json
{ "errors": ["Price must be between 1 and 30"] }
```

---

##  Validations
- `RestaurantPizza.price`: Must be an integer between 1 and 30
- Cascading delete: Deleting a Restaurant removes its related RestaurantPizzas

---

##  Postman Testing

1. Open [Postman](https://www.postman.com/)
2. Import the collection file:
   - `challenge-1-pizzas.postman_collection.json`
3. Test all routes using the included request templates.

---

##  Author

Built for Software Engineering Phase 4 Code Challenge  
[NIXON OCHIENG] | [GitHub Profile](https://github.com/Nick-Nyler)
                  [LinkedIn Profile](https://www.linkedin.com/in/nixon-ochieng-a9a623218)