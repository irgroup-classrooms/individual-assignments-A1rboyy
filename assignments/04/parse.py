import re 


def main():
    
    # Read the CSV file with the product orders
    with open('04/csv/orders.csv') as f_in:
        text = f_in.read()

    # Define the regular expression to extract all order numbers
    regex = r'\d+'
    regex_order_numbers = r"Order #(\d+)"
    regex_product_names = r"Product: ([\w\s]+),"
    regex_prices = r"Price: \$(\d+\.\d{2})"
    regex_order_dates = r"Date: (\d{4}-\d{2}-\d{2})"

    # Match the regex with the text
    orders = re.findall(regex, text)
    order_numbers = re.findall(regex_order_numbers,text)
    product_names = re.findall(regex_product_names,text)
    prices = re.findall(regex_prices,text)
    order_dates = re.findall(regex_order_dates,text)

    updated_dates = re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3/\2/\1", text)

    # Print the results
    print(orders)
    print("Order Nummern") 
    print(order_numbers)
    print("Produktname")
    print(product_names)
    print("preise") 
    print(prices)
    print("Datum der Orders") 
    print(order_dates)

    products_over_500 = []
    counter = 0
    for preis in prices:
        if float(preis) >= 500:
            products_over_500.append([product_names[counter]])
        counter +=1

    print(products_over_500)
    print("Neues Datum")
    print(updated_dates)

    lange_namen = []
    for produkt in product_names:
        if len(produkt) >6:
            lange_namen.append(produkt)

    print("neue Produkte")
    print(lange_namen)

    set_von_produkten = set(product_names)
    print("Es gibt " + str(len(set_von_produkten)) + " Produkte")

    Order_preis_vergleich = dict(zip(orders,prices))
    print(Order_preis_vergleich)
    orders_to_delete = []

    for order,preis in Order_preis_vergleich.items():
        print(float(preis))
        if (float(preis)+0.01) % 1 == 0:
            orders_to_delete.append(order)
            
    for order in orders_to_delete:
        del Order_preis_vergleich[order]

    print(Order_preis_vergleich)

    print("günstigstes Produkt")
    guenstigstes = 0
    counter = 0
    for preis in prices:
        if float(preis) < float(prices[guenstigstes]):
            guenstigstes = counter
        counter += 1
    print(prices[guenstigstes])



if __name__ == '__main__':
    main()
