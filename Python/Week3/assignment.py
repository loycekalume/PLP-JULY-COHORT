# Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying
#  a discount. The function should take the original price (price) and 
#  the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, 
#  apply the discount; otherwise, return the original price.


# Using the calculate_discount function, prompt the user to enter the original price of an item
#  and the discount percentage. Print the final price after applying the discount, 
#  or if no discount was applied, print the original price.


def calculate_discount():
    price = float(input("Enter the price: "))
    discount_rate = float(input("Enter the discount: "))
    discount_percent = discount_rate / 100

    if discount_percent >= 0.20 :
        discount = price * discount_percent
        final_price = price - discount
        print(f"Final price: {final_price}")
    else:
         print(f"Final price: {price}")

calculate_discount()



    


