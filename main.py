from fastapi import FastAPI

app = FastAPI()

inventory = {
  1: {
    "name": "Goat Cheese",
    "price": "£12.00 per Kilogram",
    "discount": "No",
  },
  2: {
    "name": "Sausage Roll",
    "price": "£1.99",
    "discount": "No",
  },
  3: {
    "name": "Hotdog",
    "price": "99p",
    "discount": "No",
  },
  4: {
    "name": "Lucozade Sport Orange",
    "price": "£2.00",
    "discount": "No",
  },
  5: {
    "name": "Lucozade Sport Raspberry",
    "price": "£2.00",
    "discount": "No",
  },
  6: {
    "name": "Coca Cola Can",
    "price": "£1.50",
    "discount": "No",
  },
  7: {
    "name": "Pepsi Max Can",
    "price": "£1.50",
    "discount": "No",
  },
  8: {
    "MEAL": "DEAL",
    "food_name": "Sausage Roll",
    "food_price": "£1.00",
    "food_discount": "Yes",
    "----": "----",
    "drink_name": "Any Drink of Choice",
    "drink_price": "£1.00",
    "drink_discount": "Yes",
    "---": "---",
    "Total Price": "£2.00",
  },
}

@app.get("/get-info/{item_id}")
def get_info(item_id: int):
  return inventory[item_id]
