# default arguments = A default value for certain parameters 
#              default is used when that argument is omitted
# make your functions more felxible, reduces number of arguments
#  1. positioinal 2. DEFAULT 3. keyword 4. arbitary

# 2. DEFAULT :
 
# def net_price(list_price , discount , tax):
#     return list_price * (1 - discount) * (1 + tax)
# print(net_price(500,0,0.05))
# Instead of this we can set default value to discount and tax

# def net_price(list_price , discount=0, tax=0.05):
#      return list_price * (1 - discount) * (1 + tax)
# print(net_price(500)) #525
# # We can change the discount and tax though we set a default values
# print(net_price(500,0.1,0)) #450

#Ex:
import time

# def count(start,end): # here if i use start=0 ->error
     
#      for x in range(start, end+1):
#           print(x)
#           time.sleep(0.5)

#      print("Done!")

# count(0,10)
#instead of i should do this
def count(end,start=0):
      for x in range(start, end+1):
          print(x)
          time.sleep(0.5)

      print("Done!")

count(10)