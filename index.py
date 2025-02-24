shopping_list = {
    "kolega_zakupy":["woda","pomidory","mydło"],
    "piekarnia":["chelb","pączek","bułki"],
    "warzywniak":["marchew","seler","rukola"]
}
total_items =0
for shop, products in shopping_list.items():
    shop = shop.capitalize()
    products = [product.capitalize() for product in products]
    print(f"Idę do {shop} i kupuję tam: {','.join(products)}")
    total_items += len(products)
    print(f"W sumie kupuję {total_items} produktów. ")

