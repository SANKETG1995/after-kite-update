from kite_trade import *
import time

enctoken = input("Enter enc token \n\n")
kite = KiteApp(enctoken=enctoken)
while True:
    user_input = input("Enter a value (type 'q' to quit): ")
   
    def case1():
        print(kite.positions())
        print(kite.margins())
        print(kite.orders())

    def case2():
        while True:
            print(kite.ltp("NSE:RELIANCE"))
            time.sleep(2)

    def case3():
        print("TBD")
#        kite.modify_order(variety=kite.VARIETY_REGULAR,
 #                 order_id="order_id",
  #                parent_order_id=None,
   #               quantity=5,
    #              price=200,
     #             order_type=kite.ORDER_TYPE_LIMIT,
      #            trigger_price=None,
       #           validity=kite.VALIDITY_DAY,
        #          disclosed_quantity=None)

# Create a dictionary mapping cases to functions
case_dict = {
    1: case1,
    2: case2,
    3: case3
}

# Get the user's choice
choice = int(input("Enter a case (1-3): "))

# Use the dictionary to execute the chosen case
case_function = case_dict.get(choice, default_case)
case_function()    
    if user_input == 'q':
        break
