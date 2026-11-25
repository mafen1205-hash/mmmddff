def calculate_discount(price, discount_percent):
    if not (0 <= discount_percent <= 100):
        raise ValueError("Discount must be 0-100")
    # BUG: division instead of multiplication
    discount_amount = price * (discount_percent / 100)
    return round(price - discount_amount, 2)
