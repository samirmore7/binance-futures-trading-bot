import argparse
from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)
from bot.logging_config import setup_logger

setup_logger()

parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True)
parser.add_argument("--price")

args = parser.parse_args()

try:
    validate_side(args.side)
    validate_order_type(args.type)
    validate_quantity(args.quantity)
    validate_price(args.price, args.type)

    print("\nOrder Request Summary")
    print("---------------------")
    print(f"Symbol: {args.symbol}")
    print(f"Side: {args.side}")
    print(f"Type: {args.type}")
    print(f"Quantity: {args.quantity}")
    print(f"Price: {args.price}")

    response = place_order(
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    print("\nOrder Response")
    print("---------------------")
    print(f"Order ID: {response.get('orderId')}")
    print(f"Status: {response.get('status')}")
    print(f"Executed Qty: {response.get('executedQty')}")
    print(f"Avg Price: {response.get('avgPrice')}")

    print("\nOrder placed successfully!")

except Exception as e:
    print(f"\nError: {str(e)}")
