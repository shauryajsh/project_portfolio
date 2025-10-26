"""
Name: Shaurya Joshi
Student ID: 34034897
Creation date: 17 Sept 2023
Last modified date: 24 Sept 2023

Description:
	The Car class represents a car object and provides various attributes and 
	methods to work with car information. It allows you to create car objects with 
	default or custom attributes, check if a car is restricted for a probationary 
	license based on its power-to-weight ratio, find a car with a specific code, 
	and retrieve the car's type.
"""

# Define Car class
class Car:

	"""
	Methods:
		__init__(self, car_code = "AB123456", car_name = "Audi", car_capacity = 5, car_horsepower = 240, 
			  car_weight = 2100, car_type = "FWD"):
			Constructor to initialize car attributes with default values.
		
		__str__(self):
			This method returns a string representation of the car object, containing its attributes.
		
		probationary_license_prohibited_vehicle(self):
			This method calculates the power-to-weight ratio of the car and checks if it exceeds the threshold for
            prohibiting a probationary license based on this ratio.
		
		found_matching_car(self, car_code):
			This method checks if a car with a specific car code exists in the car_details list of the Car object.
		
		get_car_type(self):
			This method retrieves the type of the car as a string from the Car object.
	"""
	
	def __init__(self, car_code = "AB123456", car_name = "Audi", car_capacity = 5, car_horsepower = 240, 
			  car_weight = 2100, car_type = "FWD"):
		
		"""
		Description:
			Constructor to initialize car attributes with default values.
		
		Arguments:
			self (Car): The Car object being created.
			car_code (str): Unique car code (default: "AB123456").
			car_name (str): Car name (default: "Audi").
			car_capacity (int): Seating capacity of the car (default: 5).
			car_horsepower (int): Horsepower of the car in Kilo Watts (default: 240).
			car_weight (float): Weight of the car in Kg (default: 2100).
			car_type (str): Type of the car ('FWD', 'RWD', 'AWD') (default: "FWD").
		
		Attributes:
			car_code (str): Unique car code
			car_name (str): Car name
			car_capacity (int): Seating capacity of the car
			car_horsepower (int): Horsepower of the car in Kilo Watts
			car_weight (float): Weight of the car in Kg
			car_type (str): Type of the car ('FWD', 'RWD', 'AWD')
			car_details (list): List of all car attributes

		Return:
			None
		"""

		self.car_code = car_code
		self.car_name = car_name
		self.car_capacity = car_capacity
		self.car_horsepower = car_horsepower
		self.car_weight = car_weight
		self.car_type = car_type
		self.car_details = [car_code, car_name, car_capacity, car_horsepower, car_weight, car_type]

	def __str__(self):

		"""
		Description:
			This method returns a string representation of the car object, containing its attributes.
		
		Arguments:
			self (Car): The Car object for which the string representation is generated.
		
		Return:
			str: A formatted string representing the car object, including its code, name, capacity, horsepower, weight, and type.
		"""

		return f"{self.car_code} {self.car_name} {self.car_capacity} {self.car_horsepower} {self.car_weight} {self.car_type}"
	
	def probationary_license_prohibited_vehicle(self):

		"""
		Description:
			This method calculates the power-to-weight ratio of the car and checks if it exceeds the threshold for
			prohibiting a probationary license based on this ratio.
		
		Arguments:
			self (Car): The Car object for which the probationary license restriction is determined.
		
		Return:
			bool: True if the calculated power-to-weight ratio exceeds 130, indicating a prohibited probationary license;
		      False otherwise.
		"""

		# Compute the power to weight ratio of the car, scaled for precision by multiplying it by 1000
		ratio = round((self.car_horsepower/self.car_weight) * 1000)
		# Determine whether the calculated ratio surpasses the threshold for restricting a probationary license
		if ratio > 130:
			return True
		else:
			return False
		
	def found_matching_car(self, car_code):

		"""
		Description:
			This method checks if a car with a specific car code exists in the car_details list of the Car object.
		
		Arguments:
			self (Car): The Car object in which the presence of a car with a specific code is verified.
			car_code (str): The car code to be checked for existence.
		
		Return:
			bool: True if a car with the provided car code is found in the car_details list; False otherwise.
		"""

		if car_code in self.car_details:
			return True
		else:
			return False
		
	def get_car_type(self):

		"""
		Description:
			This method retrieves the type of the car as a string from the Car object.
		
		Arguments:
			self (Car): The Car object from which the car type is retrieved.
		
		Return:
			str: A string representing the type of the car.
		"""

		return str(self.car_type)