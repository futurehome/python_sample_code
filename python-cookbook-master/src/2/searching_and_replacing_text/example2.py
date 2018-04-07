import re
template = "Hello [first_name] [last_name], Thank you for purchasing \
[product_name] from [store_name]. The total cost of your purchase was \
[product_price] plus [ship_price] for shipping. You can expect your product \
to arrive in [ship_days_min] to [ship_days_max] business days. Sincerely, \
[store_manager_name]"

# assume dic has all the replacement data
# such as dic['first_name'] dic['product_price'] etc...
dic = {
    "first_name": "John",
    "last_name": "Doe",
    "product_name": "iphone",
    "store_name": "Walkers",
    "product_price": "$500",
    "ship_price": "$10",
    "ship_days_min": "1",
    "ship_days_max": "5",
    "store_manager_name": "DoeJohn"
}
result = re.compile(r'\[(.*?)\]')


def replace(m):
    return dic[m.group(1)]


print(result.sub(replace, template))
