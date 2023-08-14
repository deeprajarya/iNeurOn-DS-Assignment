#!/usr/bin/env python
# coding: utf-8

# ## Q (1) : What is the primary goal of Object-Oriented Programming (OOP)?

# ##### solution :
# The primary goal of Object-Oriented Programming (OOP) is to organize and model the complexities of real-world entities, 
# data, and interactions into self-contained units called objects. These objects encapsulate both data (attributes or 
# properties) and behavior (methods or functions) that operate on that data. Object-Oriented Programming promotes 
# maintainable, scalable, and organized code, reducing complexity and improving software development efficiency. 
# It's a widely used paradigm in modern programming languages like Java, C++, Python, and many others.
# 
# 

# ## Q (2) : What is an object in Python?

# ##### Solution :
# In Python, an object is a fundamental concept that represents a specific instance of a data structure or a user-defined 
# class. Everything in Python is an object, including numbers, strings, lists, functions, and even classes themselves.

# ## Q (3) : What is a class in Python?

# ##### Solution :
# In Python, a class is a blueprint or a template that defines a new data type. It is a way to create user-defined data 
# structures that encapsulate data (attributes) and the functions that operate on that data (methods). Classes provide a 
# mechanism for creating objects, and each object created from a class is an instance of that class.
# 
# A class is defined using the 'class' keyword, followed by the class name and a colon. The body of the class contains 
# attributes and methods that define the behavior and properties of objects created from that class.

# ## Q(4) : What are attributes and methods in a class?

# ##### Solution :
# Attributes are the characteristics or properties or data of an object, and methods are the actions or functions that the 
# object can perform. Together, they define what an object is and what it can do in a program.

# ## Q(5) : What is the difference between class variables and instance variables in Python?

# ##### Solution :
# In Python, class variables and instance variables are two types of variables used in classes, but they have distinct purposes and scopes within the class.
# 
# Class Variables:
# 
# 1) Class variables are variables that are shared among all instances (objects) of a class.
# 2) They are defined within the class, but outside any methods, using the class name directly.
# 3) Class variables have the same value for all objects of the class.
# 4) Any changes made to a class variable will affect all instances of the class.
# 5) Class variables are useful when you want to store data that is common to all instances of the class.
# 6) To access class variables, we can use the class name or the instance name, but it's generally better to access them using the class name to avoid any ambiguity.
# 
# 
# Instance Variables:
# 
# 1) Instance variables are variables that belong to individual instances (objects) of a class.
# 2) They are defined within the class's methods, typically within the __init__ method, using the self keyword.
# 3) Each object can have its own set of instance variables with different values.
# 4) Any changes made to an instance variable will only affect that specific instance, not other instances of the class.
# 5) Instance variables are useful for storing data that is unique to each object created from the class.

# ## Q(6) : What is the purpose of the self parameter in Python class methods?
# 
# ##### Solution :
# The self parameter refers to the instance of the class on which a method is called. When you create an object from a class, any method called on that object will automatically receive a reference to that specific instance as the first argument (i.e., self). This allows the method to access and modify the object's attributes and call other methods associated with the object.

# ## Q(7) : 
# For a library management system, you have to design the "Book" class with OOP principles in mind. The “Book” class will have following attributes:
# 
# 1. title: Represents the title of the book.
# 2. author: Represents the author(s) of the book.
# 3. isbn: Represents the ISBN (International Standard Book Number) of the book.
# 4. publication_year: Represents the year of publication of the book.
# 5. available_copies: Represents the number of copies available for checkout.
# 
# The class will also include the following methods:
# 1. check_out(self): Decrements the available copies by one if there are copiesavailable for checkout.
# 2. return_book(self): Increments the available copies by one when a book isreturned.
# 3. display_book_info(self): Displays the information about the book, including its attributes and the number of available copies.

# In[2]:


class Book:
    def __init__(self, title, author, isbn, publication_year, available_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year
        self.available_copies = available_copies
    
    def check_out(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            print(f"Checked out '{self.title}'. {self.available_copies} copy(s) available.")
        else:
            print(f"'{self.title}' is not available for checkout.")
    
    def return_book(self):
        self.available_copies += 1
        print(f"Returned '{self.title}'. {self.available_copies} copy(s) available.")
    
    def display_book_info(self):
        print("Book Information:")
        print(f"Title: {self.title}")
        print(f"Author(s): {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Publication Year: {self.publication_year}")
        print(f"Available Copies: {self.available_copies}")


book1 = Book("New Ramayana", "New Valimiki", "978-3-16-148410-0", 1925, 5)
book1.check_out()
book1.return_book()
book1.display_book_info()


# ## Q(8) : 
# For a ticket booking system, you have to design the "Ticket" class with OOP principles in mind. The “Ticket” class should have the following attributes:
# 1. ticket_id: Represents the unique identifier for the ticket.
# 2. event_name: Represents the name of the event.
# 3. event_date: Represents the date of the event.
# 4. venue: Represents the venue of the event.
# 5. seat_number: Represents the seat number associated with the ticket.
# 6. price: Represents the price of the ticket.
# 7. is_reserved: Represents the reservation status of the ticket.
# 
# The class also includes the following methods:
# 1. reserve_ticket(self): Marks the ticket as reserved if it is not already reserved.
# 2. cancel_reservation(self): Cancels the reservation of the ticket if it is already reserved.
# 3. display_ticket_info(self): Displays the information about the ticket, including its attributes and reservation status.

# In[3]:


class Ticket:
    def __init__(self, ticket_id, event_name, event_date, venue, seat_number, price, is_reserved=False):
        self.ticket_id = ticket_id
        self.event_name = event_name
        self.event_date = event_date
        self.venue = venue
        self.seat_number = seat_number
        self.price = price
        self.is_reserved = is_reserved
    
    def reserve_ticket(self):
        if not self.is_reserved:
            self.is_reserved = True
            print(f"Ticket {self.ticket_id} has been reserved.")
        else:
            print(f"Ticket {self.ticket_id} is already reserved.")
    
    def cancel_reservation(self):
        if self.is_reserved:
            self.is_reserved = False
            print(f"Reservation for ticket {self.ticket_id} has been canceled.")
        else:
            print(f"Ticket {self.ticket_id} is not currently reserved.")
    
    def display_ticket_info(self):
        print("Ticket Information:")
        print(f"Ticket ID: {self.ticket_id}")
        print(f"Event Name: {self.event_name}")
        print(f"Event Date: {self.event_date}")
        print(f"Venue: {self.venue}")
        print(f"Seat Number: {self.seat_number}")
        print(f"Price: {self.price}")
        print(f"Reservation Status: {'Reserved' if self.is_reserved else 'Not Reserved'}")

# Example usage
ticket1 = Ticket("T101", "brithday Night", "2023-08-20", "Grand Arena", "A12", 50.0)
ticket1.reserve_ticket()
ticket1.display_ticket_info()
ticket1.cancel_reservation()
ticket1.display_ticket_info()


# ## Q(9) : 
# You are creating a shopping cart for an e-commerce website. Using OOP to model the "ShoppingCart" functionality the class 
# should contain following attributes and methods:
# 1. items: Represents the list of items in the shopping cart.
# 
# The class also includes the following methods:
# 1. add_item(self, item): Adds an item to the shopping cart by appending it to the list of items.
# 2. remove_item(self, item): Removes an item from the shopping cart if it exists in the list.
# 3. view_cart(self): Displays the items currently present in the shopping cart.
# 4. clear_cart(self): Clears all items from the shopping cart by reassigning an empty list to the items attribute.

# In[4]:


class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
        print(f"Item '{item}' has been added to the shopping cart.")
    
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Item '{item}' has been removed from the shopping cart.")
        else:
            print(f"Item '{item}' is not in the shopping cart.")
    
    def view_cart(self):
        print("Items in the Shopping Cart:")
        for item in self.items:
            print(f"- {item}")
    
    def clear_cart(self):
        self.items = []
        print("Shopping cart has been cleared.")

# Example usage
cart = ShoppingCart()
cart.add_item("Shoes")
cart.add_item("T-shirt")
cart.add_item("Hat")
cart.view_cart()

cart.remove_item("T-shirt")
cart.view_cart()

cart.clear_cart()
cart.view_cart()


# ## Q(10) : 
# Imagine a school management system. You have to design the "Student" class using OOP concepts.The “Student” class has the following attributes:
# 1. name: Represents the name of the student.
# 2. age: Represents the age of the student.
# 3. grade: Represents the grade or class of the student.
# 4. student_id: Represents the unique identifier for the student.
# 5. attendance: Represents the attendance record of the student.
# 
# The class should also include the following methods:
# 1. update_attendance(self, date, status): Updates the attendance record of the student for a given date with the provided status (e.g., present or absent).
# 2. get_attendance(self): Returns the attendance record of the student.
# 3. get_average_attendance(self): Calculates and returns the average attendance percentage of the student based on their attendance record.

# In[6]:


class Student:
    def __init__(self, name, age, grade, student_id):
        self.name = name
        self.age = age
        self.grade = grade
        self.student_id = student_id
        self.attendance = {}  # Using a dictionary to store attendance records
    
    def update_attendance(self, date, status):
        self.attendance[date] = status
        print(f"Attendance for {date}: {status}")
    
    def get_attendance(self):
        return self.attendance
    
    def get_average_attendance(self):
        total_days = len(self.attendance)
        if total_days == 0:
            return 0.0
        present_days = sum(1 for status in self.attendance.values() if status == "present")
        average_attendance = (present_days / total_days) * 100
        return average_attendance

# Example usage
student1 = Student("Arya", 16, "12th Grade", "S100")
student1.update_attendance("2023-08-01", "present")
student1.update_attendance("2023-08-02", "absent")
student1.update_attendance("2023-08-03", "present")
attendance_record = student1.get_attendance()
print("Attendance Record:", attendance_record)
average_attendance = student1.get_average_attendance()
print("Average Attendance:", average_attendance, "%")


# In[ ]:





# In[ ]:




