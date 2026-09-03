def apply_discount(price, discount):
    # 1. Verify price type
    if not isinstance(price, (int, float)):
        return "The price should be a number"
    
    # 2. Verify discount type
    if not isinstance(discount, (int, float)):
        return "The discount should be a number"
    
    # 3. Check for price boundaries
    if price <= 0:
        return "The price should be greater than 0"

    # 4. Check for discount boundaries
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"
    
    # 5. Calculate and return the final discounted price
    final_price = price * (1 - discount / 100)
    return final_price
