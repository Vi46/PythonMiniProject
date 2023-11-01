conversion_rate = [["EUR",0.85],["GBP",0.72],["JPY",109.35],["CAD",1.21]]
data_type =type(conversion_rate)
print(data_type)

laptopPrice = int(input("Enter laptop Price ="))
targetPrice = input("EUR,GBP,JPY,CAD")

convertedAmount = 0

for currency in conversion_rate:
    if currency[0] == targetPrice:
        convertedAmount = currency[1]*laptopPrice
        break

print(f"The laptop price in {targetPrice} is {convertedAmount} {targetPrice}")