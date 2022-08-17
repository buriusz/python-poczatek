from online_shop.orders import create_new_order

print("To jest zaczątek wielkiego sklepu internetowego :)")

product_name = input("Podaj nazwę produktu, któy chcesz kupić: ")
quantity = int(input("Ile sztuk chcesz kupic: "))

result = create_new_order(product_name, quantity)
if result is not None:
    total_price = result
    print(f"Łączny koszt zamówienia to: {total_price}PLN")