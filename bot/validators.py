def validate_side(side):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

def validate_order_type(order_type):
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")

def validate_quantity(quantity):
    try:
        q = float(quantity)
        if q <= 0:
            raise ValueError
    except:
        raise ValueError("Quantity must be a positive number")

def validate_price(price, order_type):
    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price required for LIMIT order")
        try:
            p = float(price)
            if p <= 0:
                raise ValueError
        except:
            raise ValueError("Price must be a positive number")
