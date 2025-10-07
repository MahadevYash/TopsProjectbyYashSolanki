name=input("Enter Your Name=")
age=int(input("Enter your age="))
gender=input("Enter M for male and F for female=")

product=input("Enter your product=")
weight=int(input("Enter weight in gram="))
print("------------------------")
price=11635
print(f"Current Gold Price 1 gm={price}")
amount=price*weight
print("  ")
print("TOTAL GOLD RATE= ",amount)

print("------------------------")
making=845
print("Making charge=",making)
tmaking=weight*making
print("TOTAL MAKING CHARGE:",tmaking)
print("------------------------")
total=amount+tmaking
print("Total amount:",total)

discount = 0

if gender=="M":
    if age>65:
      if amount>510000:
         discount=35
      elif amount<510000 and amount>310000:
          discount=30
      elif amount<310000 and amount>210000:
          discount=20
    if age<65:
      if amount>510000:
          discount=25
      elif amount<510000 and amount>310000:
          discount=20
      elif amount<310000 and amount>210000:
          discount=10

elif gender=="F":
    if age>65:
      if amount>510000:
          discount=40
      elif amount<510000 and amount>310000:
          discount=35
      elif amount<310000 and amount>210000:
          discount=25
    if age<65:
      if amount>510000:
          discount=30
      elif amount<510000 and amount>310000:
          discount=25
      elif amount<310000 and amount>210000:
          discount=15
else:
    print("invalid input")

print("-------------------")

print("Discount Percentage =",discount)
Damount=(amount/100)*discount
print("Total Discount =",Damount)


print("-------------------")
pay=total-Damount
print("Total amount after discount)",pay)
      
    

