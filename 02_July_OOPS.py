#!/usr/bin/env python
# coding: utf-8

#  #                                                        02_July_OOPS

# ### Q1. Explain what inheritance is in object-oriented programming and why it is used.
# 
# #### Sol.
# Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a new class to inherit the characteristics (fields and methods) of an existing class, known as the base or parent class. The new class is called the derived or child class. This concept is often referred to as "is-a" relationship, implying that a derived class is a type of the parent class. Inheritance enables code reuse, abstraction, and the creation of hierarchical relationships among classes.
# 
# ###### Here's why inheritance is used in object-oriented programming:
# 
# #### Code Reusability: 
# Inheritance promotes code reusability by allowing a derived class to reuse the properties and behaviors of the parent class. This helps in avoiding redundant code and making the codebase more modular and maintainable.
# 
# #### Abstraction: 
# Inheritance enables the creation of more abstract and general classes at higher levels of the hierarchy, while more specific details are defined in the derived classes. This abstraction simplifies the design and implementation of complex systems by focusing on high-level concepts.
# 
# #### Polymorphism: 
# Inheritance is closely related to the concept of polymorphism. Polymorphism allows objects of different classes to be treated as objects of a common base class, which makes it easier to write flexible and adaptable code. This is particularly useful for writing code that can work with different types of objects without knowing their specific types.
# 
# #### Extensibility: 
# Inheritance facilitates extending the functionality of existing classes without modifying their core implementation. You can create new classes that inherit from existing classes and add new methods or attributes specific to the new class's requirements.
# 
# #### Method Overriding: 
# Derived classes can override methods inherited from the base class. This means that a derived class can provide its own implementation of a method, which allows customization of behavior while still maintaining the common interface defined in the parent class.
# 
# #### Hierarchical Organization: 
# Inheritance allows classes to be organized in a hierarchical manner, forming a clear and logical structure that models real-world relationships. This organization makes it easier to understand and manage large codebases.
# 

# In[ ]:





# In[ ]:





# ### Q2. Discuss the concept of single inheritance and multiple inheritance, highlighting their differences and advantages.
# 
# #### Sol.
# 
# Single Inheritance and Multiple Inheritance are two different approaches to class inheritance in object-oriented programming. They determine how a class can inherit characteristics from other classes. Let's discuss each concept, highlight their differences, and explore their advantages.
# 
# #### Single Inheritance:
# In single inheritance, a class can inherit from only one parent class. This means that a derived class can extend the functionality of a single base class, incorporating its attributes and methods. Single inheritance leads to a linear hierarchy, where each class has a single parent, forming a tree-like structure.
# 
# ###### Advantages of Single Inheritance:
# 
# #### Simplicity: 
# Single inheritance is straightforward to understand and implement. The linear hierarchy makes it clear how classes are related and where functionality is derived from.
# Avoids Diamond Problem: The Diamond Problem is a complication that arises in multiple inheritance when two classes that are not directly related inherit from a common base class. Single inheritance avoids this problem entirely since each class has a single parent.
# Disadvantages of Single Inheritance:
# 
# 
# ###### Disadvantages of Single Inheritance:
# 
# #### Limited Reusability: 
# With single inheritance, a class can inherit from only one source, which can limit code reusability in situations where characteristics from multiple classes are needed.
# Lack of Flexibility: It might not adequately represent complex real-world relationships where an object may have attributes and behaviors from multiple different sources.
# Multiple Inheritance:
# In multiple inheritance, a class can inherit from more than one parent class. This allows a derived class to inherit attributes and methods from multiple sources. This approach can lead to complex class hierarchies, as each class may introduce its own set of characteristics.
# 
# 
# 
# 
# ##### Advantages of Multiple Inheritance:
# 
# ##### Enhanced Reusability: 
# Multiple inheritance allows a class to inherit functionality from multiple sources, facilitating code reuse and modularity.
# Real-world Modeling: In certain scenarios, real-world relationships can be accurately represented using multiple inheritance. For example, a class representing a "Flying Car" might inherit characteristics from both "Car" and "Aircraft" classes.
# Disadvantages of Multiple Inheritance:
# 
# 
# ##### Disadvantages of Multiple Inheritance:
# 
# ##### Diamond Problem: 
# The Diamond Problem is a significant challenge in multiple inheritance. It occurs when a derived class inherits from two classes that have a common base class. This can lead to ambiguity when calling methods or accessing attributes from the derived class.
# Complexity: Multiple inheritance can result in complex and hard-to-understand class hierarchies. Debugging and maintaining such hierarchies can become challenging.
# Potential for Conflicts: If the parent classes have methods with the same name but different implementations, it can lead to conflicts in the derived class.
# In some programming languages like Python, which support multiple inheritance, developers can use techniques like method resolution order (MRO) to address some of the challenges associated with the Diamond Problem and conflicts between methods with the same name.
# 

# In[ ]:





# In[ ]:





# ### Q3. Explain the terms "base class" and "derived class" in the context of inheritance.
# 
# #### Sol. 
# 
# In inheritance, a "base class" is the parent class that provides attributes and methods to be inherited. A "derived class" is the child class that inherits from the base class, gaining its properties. This hierarchy enables code reuse and specialization, making object-oriented programming more modular and efficient.

# In[ ]:





# In[ ]:





# ### Q4. What is the significance of the "protected" access modifier in inheritance? How does it differ from "private" and "public" modifiers?
# 
# #### Sol. 
# The "protected" access modifier in inheritance has a crucial role in controlling member visibility. Unlike "private," which restricts access to within the class, and "public," which allows access from anywhere, "protected" strikes a balance. It allows access within the class, derived classes, and even instances of those derived classes. This promotes encapsulation and supports the "is-a" relationship in OOP. 
# 
# While "private" provides strong encapsulation but no inheritance visibility, and "public" provides broad access but limited encapsulation, "protected" is an intermediary. It empowers derived classes with needed information while maintaining some encapsulation. Inheritance benefits from "protected" as it balances encapsulation and extension capabilities, making well-designed class hierarchies.

# In[ ]:





# In[ ]:





# ### Q5. What is the purpose of the "super" keyword in inheritance? Provide an example.
# 
# #### Sol. 
# The super keyword is used to refer to the parent class or superclass in the context of inheritance. It allows you to call methods and access attributes from the parent class within the derived class. The super keyword is particularly useful when a method in the derived class overrides a method in the parent class, but you still want to utilize the functionality of the overridden method in the parent class.
# 
# Here's an example to illustrate the purpose of the super keyword in Python:

# In[3]:


class Parent:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print(f"Name: {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Calling the parent class constructor
        self.age = age

    def show_info(self):
        super().show_info()  # Calling the parent class method
        print(f"Age: {self.age}")

child = Child("Arya", 20)
child.show_info()


# In[ ]:





# In[ ]:





# #### Q6. Create a base class called "Vehicle" with attributes like "make", "model", and "year". Then, create a derived class called "Car" that inherits from "Vehicle" and adds an attribute called "fuel_type". Implement appropriate methods in both classes.

# In[17]:


class vehicle:
    def __init__(self,make, model, year):
        self.make=make
        self.model=model
        self.year=year
        
    def show_info(self):
        print(f"make = {self.make}")
        print(f"model = {self.model}")
        print(f"year = {self.year}")
        
class Car(vehicle):
    def __init__(self,make, model, year,fuel_type):
        super().__init__(make, model, year)
        self.fuel_type=fuel_type
        
    def show_info(self):
        super().show_info()
        print(f"fuel_type = {self.fuel_type}")

v=vehicle("car","BMW","2023")
v.show_info()


# In[18]:


car1=Car("Car","BMW", 2023,"Petrol")
car1.show_info()


# In[ ]:





# In[ ]:





# #### Q7. Create a base class called "Employee" with attributes like "name" and "salary." Derive two classes, "Manager" and "Developer," from "Employee." Add an additional attribute called "department" for the "Manager" class and "programming_language" for the "Developer" class.

# In[47]:


class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
    def show_info(self):
        print(f"Name : {self.name} ")
        print(f"Salary : {self.salary}")


# In[48]:


class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
        
    def show_info(self):
        super().show_info()
        print(f"Department : {self.department}")


# In[59]:


class Developer(Manager):
    def __init__(self,name,salary,department,programming_language):
        super().__init__(name,salary,department)
        self.programming_language=programming_language
        
    def show_info(self):
        super().show_info()
        print(f"Programming Language : {self.programming_language}")


# In[50]:


emp1=Employee("Arya", "50k")
emp1.show_info()


# In[51]:


mgr=Manager("Arya","50k","Data Science Team")
mgr.show_info()


# In[60]:


dev=Developer("Deepraj", "80k", "DataScience", "Python")
dev.show_info()


# In[ ]:





# In[ ]:





# #### Q8. Design a base class called "Shape" with attributes like "colour" and "border_width." Create derived classes, "Rectangle" and "Circle," that inherit from "Shape" and add specific attributes like "length" and "width" for the "Rectangle" class and "radius" for the "Circle" class.
# 

# In[62]:


class shape:
    def __init__(self,colour,border_width):
        self.colour=colour
        self.border_width=border_width
        
    def show_info(self):
        print(f"colour : {self.colour}")
        print(f"border_width : {self.border_width}")


# In[75]:


class rectangle(shape):
    def __init__(self,colour,border_width,length,width):
        self.length=length
        self.width=width
        super().__init__(colour,border_width)
    
    def show_info(self):
        super().show_info()
        print(f"length : {self.length}")
        print(f"width : {self.width}")


# In[78]:


class circle(shape):
    def __init__(self,colour,border_width,radius):
        super().__init__(colour,border_width)
        self.radius=radius
        
    def show_info(self):
        super().show_info()
        print(f"radius : {self.radius}")
        


# In[70]:


shape1=shape("Red", 10)
shape1.show_info()


# In[77]:


r1=rectangle("Blue",10,4,5)
r1.show_info()


# In[80]:


c1=circle("Green",10,5)
c1.show_info()


# In[ ]:





# In[ ]:





# #### Q9. Create a base class called "Device" with attributes like "brand" and "model." Derive two classes, "Phone" and "Tablet," from "Device." Add specific attributes like "screen_size" for the "Phone" class and "battery_capacity" for the "Tablet" class.

# In[81]:


class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")

class Phone(Device):
    def __init__(self, brand, model, screen_size):
        super().__init__(brand, model)
        self.screen_size = screen_size

    def display_info(self):
        super().display_info()
        print(f"Screen Size: {self.screen_size}")

class Tablet(Device):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def display_info(self):
        super().display_info()
        print(f"Battery Capacity: {self.battery_capacity}")

# Creating objects of derived classes
phone = Phone("Apple", "iPhone 13", "6.1 inches")
tablet = Tablet("Samsung", "Galaxy Tab S7", "8000 mAh")

# Displaying information about the devices
print("Phone:")
phone.display_info()

print("\nTablet:")
tablet.display_info()


# In[ ]:





# In[ ]:





# #### Q10. Create a base class called "BankAccount" with attributes like "account_number" and "balance." Derive two classes, "SavingsAccount" and "CheckingAccount," from "BankAccount."  Add specific methods like "calculate_interest" for the "SavingsAccount" class and "deduct_fees" for the "CheckingAccount" class.

# In[99]:


class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance
        
    def show_info(self):
        print(f"Account_Number : {self.account_number}")
        print(f"Balance : {self.balance}")

class SavaingsAccount(BankAccount):
    def __init__(self,account_number,balance):
        super().__init__(account_number,balance)
    
    def calculate_intrest(self):
        super().show_info()
        balance=self.balance
        intrest_rate = int(input("Intrest rate : "))
        intrest_amount = (self.balance * intrest_rate)/100
        new_balance= balance + intrest_amount
        print(f"Updated Balance :{new_balance}")


# In[92]:


bank_acc1=BankAccount(12345, 15000)
bank_acc1.show_info()


# In[100]:


saving_acc1=SavaingsAccount(12345,15000)
saving_acc1.calculate_intrest()


# In[ ]:




