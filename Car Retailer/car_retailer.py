"""
Name: Shaurya Joshi
Student ID: 34034897
Creation date: 18 Sept 2023
Last modified date: 24 Sept 2023

Description:
	Contains all the operations related to the CarRetailer Class. This class inherits from the Retailer class.
"""

# Import necessary classes and modules
from retailer import Retailer
from car import Car
from order import Order
# Import the 'random' module to generate random numbers
import random

class CarRetailer(Retailer):
	def __init__(self, retailer_id = 12345678, retailer_name = "Jackie Chan", carretailer_address = "Center Road Clayton, VIC 3168", 
			  carretailer_business_hours = (9.5, 18.0), carretailer_stock = []):
		
		"""
        Description:
        	Constructs a CarRetailer object.

        Arguments:
			retailer_id (int, default: 12345678):Must be a unique integer of 8 digits.
			retailer_name (str, default: "Jackie Chan"): Can only consist of letters and whitespace.
			carretailer_address (str, default: "Center Road Clayton, VIC 3168"): The address format should be 
			street address followed by the state and postcode.
			carretailer_business_hours (tuple of floats, default: (9.5, 18.0)):Represents start and end hours in 24hr format.
			Business hours are from 9:30 AM inclusive to 6:00 PM inclusive.
			The business hours should be within the range of 6:00 AM inclusive to 11:00 PM inclusive.
			carretailer_stock (list of str, default: None): A list of car_codes indicating the available cars from the retailer.
			The default value should be an empty list.

        Returns:
        	None
        """
		
		# Calls the constructor of the base class 'Retailer' to initialize retailer_id retailer_name attributes
		super().__init__(retailer_id, retailer_name)
		self.carretailer_address = carretailer_address
		self.carretailer_business_hours = carretailer_business_hours
		self.carretailer_stock = carretailer_stock
		
	def __str__(self):

		"""
        Description:
        	Return the car retailer information as a formatted string.

        Arguments:
			self (CarRetailer): The Car Retailer object for which the string representation is generated.

        Returns:
        str: A string in the following format: "retailer_id, retailer_name, carretailer_address
        carretailer_business_hours, carretailer_stock"
        """

		return f"{self.retailer_id} {self.retailer_name} {self.carretailer_address} {self.carretailer_business_hours} {self.carretailer_stock}"
	
	def load_current_stock(self, file_path):

		"""
        Description:
			Retrieve the car retailer's current stock by matching the retailer_id with the 
			data in the "stock.txt" file. Subsequently, collect the car codes of the available 
			cars and store them in the carretailer_stock list attribute.

        Arguments:
			self (CarRetailer): The Car Retailer object.
        	file_path (str): The path to the stock file.

        Returns:
        	None
        """

		try:
			with open(file_path, 'r') as read_file:
				for line in read_file:
					# Split the line by comma into a list
					car_data = line.split(',')
					# Check if the list has at least 6 elements
					if len(car_data) >= 6:
						# Get the car code from the 8th element and remove leading/trailing whitespace
						car_code = car_data[7].strip()
						# Add the car code to the stock list
						self.carretailer_stock.append(car_code)
					elif len(car_code) == 8 and car_code[:2].isalpha() and car_code[2:].isdigit():
							# Add the car code to the stock list if it matches the specified format
						self.carretailer_stock.append(car_code)
		except FileNotFoundError:
			print("File not found: ", file_path)
		except Exception as e:
			print("An error occurred while loading current stock: ", e)

	def is_operating(self, cur_hour):

		"""
        Description:
			Return a boolean value to indicate whether the car retailer is currently
			operating (i.e., within working hours)

        Arguments:
			self (CarRetailer): The Car Retailer object.
			cur_hour (float): A float value indicating the current hour in
			24H format, e.g., 12.5 - 12:30 PM.

        Returns:
        	bool: True (is operating) / False (is not operating)
        """

		return self.carretailer_business_hours[0] <= cur_hour <= self.carretailer_business_hours
	
	def get_all_stock(self):

		"""
        Description:
			Retrieve a list of Car objects representing all available cars in the car retailer's current stock.

        Arguments:
        	self (CarRetailer): The Car Retailer object

        Returns:
        	list: A list of Car objects
        """

		car_code_list = []
		print(self.carretailer_stock)
		for car_code in self.carretailer_stock:
			car = Car(car_code)
			car_code_list.append(car)
		return car_code_list
	
	def get_postcode_distance(self, postcode):

		"""
        Description:
			Calculate the distance between the car retailer's postcode and the given postcode.

        Arguments:
			self (CarRetailer): The Car Retailer object.
            postcode (int): The postcode to calculate the distance from.

        Returns:
            distance (int): The distance between the postcodes.
        """

		print("Address: ", self.carretailer_address)
		index = self.carretailer_address.find(',')
		post_code = self.carretailer_address[index:].strip()
		post_code = post_code[-4:]
		distance = abs(postcode - int(post_code))
		return distance
	
	def remove_from_stock(self, car_code):

		"""
        Description:
			Remove a car from the car retailer's stock.

        Arguments:
			self (CarRetailer): The Car Retailer object.
            car_code (str): The car code of the car to be removed.

        Returns:
            bool: True if the car was successfully removed, False otherwise.
        """

		if car_code in self.carretailer_stock:
			self.carretailer_address.remove(car_code)
			return True
		else:
			return False
		
	def add_to_stock(self, car = Car):

		"""
        Description:
			Add a car to the car retailer's stock.

        Arguments:
			self (CarRetailer): The Car Retailer object.
            car (Car): The car object to be added.

        Returns:
            bool: True if the car was successfully added, False otherwise.
        """

		if car in self.carretailer_stock(Car):
			return False
		else:
			self.carretailer_stock.append(Car)
			return True
		
	def get_stock_by_car_type(self, car_types):

		"""
        Description:
			Get the stock of cars based on the given car types.

        Arguments:
			self (CarRetailer): The Car Retailer object.
            car_types (list of str): The car types to filter the stock by.

        Returns:
            car_type_stock (list): A list of Car objects matching the given car types.
        """

		car_type_stock = []
		for car_code in self.carretailer_stock:
			car = Car(car_code)
			if car.car_type in car_types:
				car_type_stock.append(car)
		return car_type_stock
	
	def get_stock_by_licence_type(self, licence_type):

		"""
        Description:
			Get the stock of cars based on the given licence type.

        Arguments:
			self (CarRetailer): The Car Retailer object.
            licence_type (str): The licence type to filter the stock by.

        Returns:
            available_cars (list): A list of Car objects matching the given licence type.
        """

		available_cars = []
		for car_code in self.carretailer_stock:
			car = Car(car_code)
			if licence_type == 'L' or (licence_type == 'P' and not Car.probationary_license_prohibited_vehicle) or licence_type == 'Full':
				available_cars.append(car)
		return available_cars

	def car_recommendation(self):

		"""
        Description:
			Get a random car recommendation from the car retailer's stock.

		Arguments:
			self (CarRetailer): The Car Retailer object.
			
        Returns:
            Car: A randomly selected Car object from the stock.
        """

		if self.carretailer_stock:
			select_car_code = random.choice(self.carretailer_stock)
			selected_car = Car(select_car_code)
			return selected_car
		else:
			return None
		
	def create_order(self, car_code):

		"""
        Description:
			Create an order for a car with the given car code.

        Arguments:
			self (CarRetailer): The Car Retailer object.
            car_code (str): The car code of the car to create an order for.

        Returns:
            Order: The created Order object if the car is available in the stock, None otherwise.
        """

		if car_code in self.carretailer_stock:
			self.carretailer_stock.remove(car_code)
			new_order = Order(Order.order_id, car_code, self.retailer_id, Order.order_creation_time)
			return new_order
		else:
			return None