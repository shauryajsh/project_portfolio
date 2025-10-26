"""
Name: Shaurya Joshi
Student ID: 34034897
Creation date: 20 Sept 2023
Last modified date: 24 Sept 2023

Description:
	Defines an Order class that represents orders with unique IDs based on specified steps.
	Each order is associated with a car and retailer.
"""

# Import necessary classes and modules
from car import Car
from retailer import Retailer
# Import the 'random' module to generate random numbers
import random

# Define the order class
class Order:

	"""
	Methods:
		__init__(self, order_id = "1234", order_car = "Mazda", order_retailer = "Kandet", 
			  order_creation_time = 1672491601):
			Constructor for the Order class to initialize order attributes with default values.

		__str__(self):
			String representation of the order object.

		generate_order_id(self, car_code):
			Generate and return a unique order ID based on specified steps, incorporating car code and creation time.
	"""

	def __init__(self, order_id = "1234", order_car = "Mazda", order_retailer = "Kandet", 
			  order_creation_time = 1672491601):
		
		"""
		Description:
			Constructor to initialize order attributes with default values.

		Arguments:
			self (Order): The Order object being created.
			order_id (str): Unique order ID (default: "1234").
			order_car (Car): Car associated with the order (default: "Mazda").
			order_retailer (Retailer): Retailer associated with the order (default: "Kandet").
			order_creation_time (int): Timestamp when the order was created (default: 1672491601).
		
		Attributes:
			order_id (str): Unique identifier for the order.
			order_car (Car): The car associated with the order.
			order_retailer (Retailer): The retailer associated with the order.
			order_creation_time (int): The timestamp when the order was created.
		"""

		self.order_id = order_id
		self.order_car = order_car
		self.order_retailer = order_retailer
		self.order_creation_time = order_creation_time

	def __str__(self):

		"""
		Description:
			This method returns a formatted string representation of the order object.

		Arguments:
			self (Order): The Order object for which the string representation is generated.

		Return:
			str: A formatted string representing the order object, including its ID, car details, retailer details, and creation time.
		"""

		return f"{self.order_id}{self.order_car.car_code}{self.order_retailer.retailer_id}{self.order_creation_time}"
	
	# Generate and return a unique order ID based on the specified steps
	def generate_order_id(self, car_code):

		"""
		Description:
			This method generates and returns a unique order ID based on specified steps, incorporating car code and creation time.

		Arguments:
			self (Order): The Order object for which the order ID is generated.
			car_code (str): The car code associated with the order.

		Return:
			str: A unique order ID combining random alphabets, car code, and creation time.
		"""

		random_string = ''
		str_1 = "~!@#$%^&*"
		order_id = ''
		# Step 1: Generate a random lowercase alphabet character 6 times
		for i in range(10):
			# random_alphabet = (random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
			# Step 2: If the current iteration is odd, convert the character to uppercase
			if i == 0 or i == 9:
				random_alphabet = (random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')).lower()
			else:
				random_alphabet = (random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
			# Storing the final string from step 1 and step 2
			random_string = random_string + random_alphabet
			# Step 3: Calculate the ASCII value of the current character
			ascii_value = ord(random_alphabet)
			# Step 4: Calculate the remainder when the ASCII value is squared and divided by the length of 'str_1'
			remainder = (ascii_value ** 2) % len(str_1)
			# Step 5 and step 6 combined: Append str_1[remainder] multiplied by i to 'order_id'
			order_id = order_id + (str_1[remainder] * i)
		# Step 6: Append car_code and order creation time to 'order_id'
		order_id = random_string + order_id + car_code + str(self.order_creation_time)
		# Return the generated order id
		return order_id

order = Order()
print(order.generate_order_id("AB123456"))