"""A small shopping cart, for demonstrating the testing pipeline."""


def add_item(cart, name, price, quantity=1):
    """Add an item to a cart.

    Args:
        name: Product name.
        price: Unit price. Must be greater than 0.
        quantity: How many to add. Must be at least 1.

    Returns:
        The updated cart.
    """
    cart.append({"name": name, "price": price, "quantity": quantity})
    return cart


def calculate_total(cart):
    """Add up every line in the cart.

    Args:
        cart: A list of item dicts.

    Returns:
        The total price as a float.
    """
    total = 0
    for item in cart:
        total += item["price"] * item["quantity"]
    return total


def apply_discount(total, percent):
    """Take a percentage off a total.

    Args:
        total: The amount before discount. Must be greater than 0.
        percent: Discount percentage, 0 to 100.

    Returns:
        The discounted amount.

    Raises:
        ValueError: If percent is outside 0 to 100.
    """
    if percent < 0 or percent > 100:
        raise ValueError("percent must be between 0 and 100")
    return total - (total * percent)
