#suppose you have a dataframe or table in python from that table select the alternate rows 
values = input()
numbers = [x for x in values.split(",") if int(x)%2!=0]
print(",".join(numbers))