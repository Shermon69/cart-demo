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
    total = 0.0
    for item in cart:
        total += item["price"] * item["quantity"]
    return total


def apply_discount(total, percent):
    """Take a percentage off a total.

    Args:
        total: The amount before discount. Must be >= 0.
        percent: Discount percentage, 0 to 100.

    Returns:
        The discounted amount.

    Raises:
        ValueError: If percent is outside 0 to 100.
    """
    if percent < 0 or percent > 100:
        raise ValueError("percent must be between 0 and 100")
    if total <= 0:
        raise ValueError("total must be positive")
    return total - (total * percent)


def refund(amount, paid):
    """Refund part of a payment.

    Args:
        amount: How much to refund. Must not exceed what was paid.
        paid: The original payment.

    Returns:
        The amount still held after the refund.

    Raises:
        ValueError: If amount is greater than paid.
    """
    return paid - amount
