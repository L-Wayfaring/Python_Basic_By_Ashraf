# format specifires = {value:flags} format a value
# based on what flags are inserted

#1 .(number)f = round to that many decimal places (fixed point)
#2 :(number) = allocate that many spaces
#3 :03 = allocate and zero pad that many spaces
#4 :< = left justify
#5 :> = right justify
#6 :^ = center align
#7 :+ = use a plus sign to indicate positive value
#8 := = place sign to leftmost position
#9 :  = insert a space before positive numbers
#0 :, = comma separator

price1 = 3000.14159

print(f"Price 1 is :${price1}") # $3000.14159   # Normal

print(f"Price 2 is :${price2:.2f}") #$-9870.66  #1

print(f"Price 1 is :${price1:12}") # $  3000.14159 #2

print(f"Price 1 is :${price1:012}") # $003000.14159 #3

print(f"Price 1 is :${price1:<}") # $3000.14159 #4

print(f"Price 1 is :${price1:>}") # $3000.14159 #5

print(f"Price 1 is :${price1:^}") # $3000.14159 #6

print(f"Price 1 is :${price1:+}") # $+3000.14159 #7

print(f"Price 1 is :${price1:=}") # $3000.14159 #8

print(f"Price 1 is :${price1: }") #  3000.14159 #9

print(f"Price 1 is :${price1:,}") # $3,000.14159 #0
