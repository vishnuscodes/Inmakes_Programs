# def getprice(price_dic, item):
#
#     result = price_dic.get(item)
#
#     return result


PriceList = {"IPhone":"$1000", "Apple Watch":"$800", "Laptop" : "$1200", "Racket":"$55","Kayak":"$800"}
product = input("Enter the name of the item: ")
#price = getprice(PriceList,product)
print(PriceList.get(product))