# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 13:54:46 2019

@author: Maftuna
"""

class Store:
    def __init__(self, ID, Name, Address, Tel):
        self.__Name=Name
        self.__ID=ID
        self.__Address=Address
        self.__Tel=Tel
    
    @property
    def Name(self):
        return self.__Name
    
    @Name.setter
    def Name(self, name_value):
        self.__Name=name_value
    
    @property
    def ID(self):
        return self.__ID
    
    @ID.setter
    def ID(self, id_value):
        self.__ID=id_value
    
    @property
    def Address(self):
        return self.__Address
    
    @Address.setter
    def Address(self, address_value):
        self.__Address=address_value
    
    @property
    def Tel(self):
        return self.__Tel
    
    @Tel.setter
    def Name(self, tel_value):
        self.__Tel=tel_value
    
   
        
    def __str__(self):
        return ('\t Name: {} \t ID: {} \n \t Adress: {} \t Tel: +9989{}.'.format(self.__Name, self.__ID, self.__Address, self.__Tel))



class Staff:
    def __init__(self, ID, SSN, Name, Address, JobTitle, salary):
        self.__ID=ID
        self.__SSN=SSN
        self.__Name=Name
        self.__Address=Address
        self.__JobTitle=JobTitle
        self.__salary=salary
    
    @property
    def Name(self):
        return self.__Name
    
    @Name.setter
    def Name(self, name_value):
        self.__Name=name_value
    
    @property
    def ID(self):
        return self.__ID
    
    @ID.setter
    def ID(self, id_value):
        self.__ID=id_value
    
    @property
    def SSN(self):
        return self.__SSN
    
    @SSN.setter
    def SSN(self, ssn_value):
        self.__SSN=ssn_value
    
    @property
    def Address(self):
        return self.__Address
    
    @Address.setter
    def Address(self, address_value):
        self.__Address=address_value
    
    @property
    def JobTitle(self):
        return self.__JobTitle
    
    @JobTitle.setter
    def JobTitle(self, jobTitle_value):
        self.__JobTitle=jobTitle_value
    
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, salary_value):
        self.__salary=salary_value
        
        
          
    def __str__(self):
        return ('\t Name: {}, \t ID: {} \n \t Address: {} \t SSN: {} \n \t Jobtitle: {} \t Salary:  ${}'.format(self.__Name, self.__ID, 
                        self.__Address, self.__SSN, self.__JobTitle, self.__salary))


class Customer:
    def __init__(self, SSN, Name, Address, Purchasing_Points, Tel, Memberships=None):
        self.__SSN=SSN
        self.__Name=Name
        self.__Address=Address
        self.__Purchasing_Points=Purchasing_Points
        self.__Tel=Tel
        self.__Memberships=Memberships or []
    
    @property
    def SSN(self):
        return self.__SSN
    
    @SSN.setter
    def SSN(self, ssn_value):
        self.__SSN=ssn_value
    
    @property
    def Address(self):
        return self.__Address
    
    @Address.setter
    def Address(self, address_value):
        self.__Address=address_value
    
    @property
    def Purchasing_Points(self):
        return self.__Purchasing_Points
    
    @Purchasing_Points.setter
    def Purchasing_Points(self, purchasing_points_value):
        self.__Purchasing_Points=purchasing_points_value
    
    @property
    def Name(self):
        return self.__Name
    
    @Name.setter
    def Name(self, name_value):
        self.__Name=name_value
    
    @property
    def Memberships(self):
        return self.__Memberships
    
    @Memberships.setter
    def Memberships(self, memberships_value):
        self.__Memberships=memberships_value


    def __str__(self):
        return ('\t Name: {}, \t Address: {} \n \t Purchasing_Points: {} \t SSN: {} \n \t Memberships is {} '.format(self.__Name, self.__Address, 
                        self.__Purchasing_Points, self.__SSN, self.__Memberships))

class Product:
    def __init__(self, ProductCode, Name, Description, Price, Points):
        self.__ProductCode=ProductCode
        self.__Description=Description
        self.__Price=Price
        self.__Points=Points
        self.__Name=Name
    
    @property
    def ProductCode(self):
        return self.__ProductCode
    
    @ProductCode.setter
    def ProductCode(self, productCode_value):
        self.__ProductCode=productCode_value
        
    @property
    def Description(self):
        return self.__Description
    
    @Description.setter
    def Description(self, description_value):
        self.__ProductCode=description_value
    
    @property
    def Name(self):
        return self.__Name
    
    @Name.setter
    def Name(self, name_value):
        self.__Name=name_value
    
    @property
    def Price(self):
        return self.__Price
    
    @Price.setter
    def Price(self, price_value):
        self.__Price=price_value
    
    @property
    def Points(self):
        return self.__Points
    
    @Points.setter
    def Points(self, points_value):
        self.__Points=points_value
    def __str__(self):
        return ('\t ProductCode: {} \t Name: {} \n \t Description: {} \t Price: ${} \n \t Jobtitle: {} \t Salary: {}'.format(self.__ProductCode, self.__Name, 
                self.__Description, self.__Price, self.__Points))


class Order:
    def __init__(self, Store_object, Customer_Object, Staff_Object, Product_Objects, Quantity):
        self.__Store_object=Store_object
        self.__Customer_Object=Customer_Object
        self.__Staff_Object=Staff_Object
        self.__Product_Objects=Product_Objects or []
        self.__Quantity=Quantity
     
    @property
    def Quantity(self):
        return self.__Quantity
    
    @Quantity.setter
    def Quantity(self, quantity_value):
        self.__Quantity=quantity_value
    Product_Objects=Product(2345, 'Bread', 'Qoqon bread', 20, 3)       
    def addProduct(product_object):
        Product_Objects =[]
        for x in product_object:
            Product_Objects.append(x)


    def printReceipt(self):
        money=117 
        Store_object=Store(1238, 'Home_store', 'Xasanov street', 32145)
        Customer_Object=Customer(1458, 'Maftuna', 'Tashkent city', 2, 56565, ['regular customer', 'sister of staff'])
        Staff_Object=Staff(555, 458, 'Ahmadjon', 'Yunosob district', 'Seller', 2564)
        Product_Objects=Product(8787, 'Cola', 'US', 5, 1)  
        stock={
                'banana':6,
                'apple':0,
                'orange':32,
                'pear':15,}
        prices={
                'banana': 4,
                'apple':2,
                'orange':1.5,
                'pear':3}
        points={
                'banana': 2,
                'apple': 1,
                'orange': 1,
                'pear': 3}
        name=input('What is your name?')
        print('Hi, %s, welcome to home store. '%(name))
        print()
        
        def uppercase(x):
            return x[0].upper()+x[1:]   

        def menu():
            for fruit in prices:
                print(uppercase(fruit))
                print('Price: $%s'%(prices[fruit]))
                print('Stock: %s'%(stock[fruit]))
                print()
            print('You have: $%s'%(money))
            print()
        print("\t Info of staff and customer:")
        print("\t\t Staff member name: \t Customer Store ID: \t Customer name: \t \n")
        print("\t\t",Staff_Object.Name, " \t\t", Store_object.ID, " \t\t", Customer_Object.Name, " \t\t\n")
        print("\t\t Product code: \t Name: \t Price: \t product description: \t points \t Total Price  \t quantity")
        print("\t\t",Product_Objects.ProductCode, "\t\t", Product_Objects.Name, "\t\t $", Product_Objects.Price,
             "\t\t",Product_Objects.Description, "\t\t",Product_Objects.Points, "\t\t",self.Quantity)
        
        def ask_fruit(money):
            fruit=input('''What fruit do you want?
                        ''')
            print()
            if fruit in stock:
                if stock[fruit]>0:
                    ask_amount(fruit,money)
                else:
                    print('''Sorry, %ss are out of stock
                          '''%(fruit))
                    ask_fruit(money)
            else:
                print('''Sorry, we don\'t have that, look at the menu.
                      ''')
                ask_fruit(money)
        
        def ask_amount(fruit,money):
            amount=int(input('''How many %ss do you want?
                             '''%(fruit)))
            print()
            if amount<=0:
                print('''At least buy one.''')
                
                ask_amount(fruit,money)
            elif stock[fruit]>=amount:
                sell(fruit,amount,money)
            else:
                print('''Sorry, we don\'t have that many %ss.
                      '''%(fruit))
                ask_amount(fruit,money)
        
       
        
        def sell(fruit,amount,money):
            cost=prices[fruit]*amount
            confirmation=input('''Are you sure? That will be $%s.
        -Yes
        -No
        '''%(cost)).lower()
            print()
            if confirmation=='yes':
                money-=cost
                print('''Thank you for the business!
                      ''')
                stock[fruit]=stock[fruit]-amount
                ask_again()
            elif confirmation=='no':
                ask_fruit(money)
            else:
                print('''Answer me.
                      ''')
                sell(fruit,amount,money)
        
        
        def ask_again():
            answer=input('''Do you want anything else?
        -Yes
        -No
        ''').lower()
            print()
            if answer=='yes':
                menu()
                ask_fruit(money)
            elif answer=='no':
                print('Okay, bye.')
            else:
                print('Answer me.')
                ask_again()
        
        
        menu()
        ask_fruit(money)
        #sell('banana', 2, 125)
        #ask_amount("apple",1313)
        #sell()
        #ask_again()
print("\t\t\t *** Store info *** \n")       
storeObject=Store(456, "Home-Sore", "Tashkent city", 897)
print(storeObject)

print("\t\t\t *** Customer info *** \n")    
customer1=Customer(123, "Maftuna", "Yangiyul district", 3, 7894, "friend of staff")
print(customer1)

customer2=Customer(255, "Ahmadjon", "Andijon", 2, 45678, "brother of staff")
print(customer2)

print("\t\t\t *** Staff info *** \n")    
staff1=Staff(177, 565, "Yo'ldosh aka", "Navoiy district", "Seller", 456)
print(staff1)

staff2=Staff(789, 666, "Yulduz xola", "Buhoro city", "halper of seller", 564)
print(staff2)

order_object=Order(storeObject, customer1, staff1, ['banana', 'apple', 'orange', 'pear'], 58)
print(order_object.printReceipt())



        
        
    
