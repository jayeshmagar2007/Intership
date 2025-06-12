'''task 1:
Create a "Shopping Bill" program:

Take input with proper data types: item name, quantity, price per item.

Calculate total = quantity × price.

finally,
Print a bill'''

item_name = input("Enter the item name:")
quantity = int (input("Enter the quantity :"))
price = float(input("Enter the price of item :"))
Total = quantity * price
discount=Total /10
gst =discount *0.18
total = Total-discount * 0.18
print("\n\t...Shopping Bill...")
print ("Item Name :",item_name)
print("Quantity of item :",quantity)
print("Price of item is : ",price)
print("Total is :",Total)
print("Discount :",discount)
print("GST :",gst)
print  ( "Discounted price with gst :",total)