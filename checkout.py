def calculate_total(price, tax_rate):
    """Calculates the total price including tax."""
    total = price + (price * tax_rate)
    return total + 10