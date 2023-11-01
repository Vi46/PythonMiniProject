#listOflistToDictonary
# Multiple inner lists
laptop_product = ["Laptop", 899.00, "USD", 2, 3.34, "Hardware"]
keyboard_product = ["Keyboard", 29.50, "USD", 6, 4.80, "Peripherals"]
mouse_product = ["Mouse", 13.99, "USD", 14, 2.45, "Peripherals"]
hdmi_cable_product = ["HDMI Cable", 9.50, "USD", 58, 5.0, "Accessories"]
printer_product = ["Printer", 58.20, "USD", 21, 3.75, "Peripherals"]
headphones_product = ["Headphones", 26.99, "USD", 5, 4.77, "Accessories"]
docking_station_product = ["Docking Station", 65.41, "USD", 1, 4.9, "Hardware"]

# A list of lists
inventory_products = [laptop_product, keyboard_product, mouse_product, hdmi_cable_product, printer_product, headphones_product, docking_station_product]
#print(inventory_products)

dict = []
for product in inventory_products:
    #print('product',product)
    product_dict={
        'Name': product[0],
        'price': product[1],
        'currency': product[2],
        'quantity': product[3],
        'user_rating': product[4],
        'category': product[5]
    }
    #print('product_dict',product_dict)
    dict.append(product_dict)
#print('dict',dict)

for final_dict in dict:
 #print(final_dict)

book1 = ["The Great Gatsby", "F. Scott Fitzgerald", 1925, "978-0-7432-7356-5"]
book2 = ["To Kill a Mockingbird", "Harper Lee", 1960, "978-0-06-112008-4"]
book3 = ["1984", "George Orwell", 1949, "978-0-452-28423-4"]
book4 = ["Pride and Prejudice", "Jane Austen", 1813, "978-0-14-143951-8"]

# A list of lists representing books
books_data = [book1, book2, book3, book4]


emptyList =[]
for book in books_data:
    book_dictionary = {
        'Name' : book[0],
        'Author Name' : book[1],
        'Published Year' : book[2],
        'Book Id' : book[3]
    }
    print(book[0])
    emptyList.append(book_dictionary)
    #print(emptyList)

    #for finalBook in emptyList:
