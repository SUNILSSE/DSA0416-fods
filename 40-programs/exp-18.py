item_prices = [10, 20, 30]
quantities = [2, 1, 3]
discount_rate = 10 
tax_rate = 5 


subtotal = sum(price * quantity for price, quantity in zip(item_prices, quantities))
print("Subtotal:", subtotal)

discount_amount = (discount_rate / 100) * subtotal
print("Discount amount:", discount_amount)

discounted_subtotal = subtotal - discount_amount
print("Discounted subtotal:", discounted_subtotal)

tax_amount = (tax_rate / 100) * discounted_subtotal
print("Tax amount:", tax_amount)

total_cost = discounted_subtotal + tax_amount
print("Total cost:", total_cost)
