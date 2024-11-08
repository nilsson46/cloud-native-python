import data.databas as db 

print(db.a)
# inga {} för kodblock utan indentering. 

# x = 12 

# y = 13 

# for i in range(0,5): #0 är inklusive men 5 är exklusive. 0,1,2,3,4
#     print(i)
# if x == 12: 
#     print("x är 12")
# else:
#     print("x är inte 12")



# namn = "Simon"

# print("Hej " + namn + "!") 
# namn = namn.upper()
#namn = 12 

# print( namn)



# myChildren = ["Emil", "Tobias", "Linus"] #lista med strängar 
# myChildren.append("Sara") #lägger till ett element i listan
# for barn in myChildren: # for each loop
#     print(barn)
# antal = len(myChildren)
# print(antal)


#function 

# def calculateTotalPrice(priceExMoms:int, moms:int) -> int : #type hinting 
#     total = priceExMoms + moms 
#     return total 

# calculateTotalPrice
# while True: 
#     price = int(input("Ange pris ex moms"))
#     moms = int(input("Ange moms")) 
#     total = calculateTotalPrice(price,moms)

#     print(f"Totala priset blev {total} kronor")
    
    
class Person: 
    def __init__(self, name, age): 
        self.name = name
        self.age = age
        self.phone = ""
        pass 
    
    
p = Person("Simon", 30)
p.City = "Stockholm"
print(p.name) 