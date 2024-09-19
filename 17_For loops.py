# for loops + execute a block of code a fixed number of times.
#         You can iterate over a range, string, sequence, etc.

# for x in range(1,11):       # 11 cause second value is excluded!
#     print(x)
#Print in reveerse:
# for x in reversed(range(1,11)):       # 11 cause second value is excluded!
#     print(x)
# print("Happy New Year")
# credit_card = "1234-5678-9012-3456"
# for x in credit_card:       # x will hold the card position
#     print(x)

for x in range(1,11):
    if x == 7:
        continue    #skipping the number 7. #if 'break' ->end the loop
    else:
        print(x)
