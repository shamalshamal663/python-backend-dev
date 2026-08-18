def calculate_order(cart_price,promo_code):
    sub_total = sum(cart_price)
    promo = promo_code.strip().upper()
    if promo == "SAVE10":
     discount_total = sub_total*0.90
    elif promo == "FLAT20" and sub_total > 50: 
       discount_total = sub_total - 20
    else:
       discount_total = sub_total


    if discount_total < 30 :
       discount_total += 5.0

    return(f"Sub Total:{sub_total:.2f} | Final Total :{discount_total:.2f}") 


print(calculate_order([15.0,20.0,10],"save10"))
print(calculate_order([10.0, 12.0], "FLAT20"))       
print(calculate_order([30.0, 30.0], "FLAT20"))
          
    