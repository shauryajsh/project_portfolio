"""
Name: Shaurya Joshi
Student ID: 34034897
Creation date: 17 Sept 2023
Last modified date: 24 Sept 2023

Description:
	Defines a Retailer class that represents retailers with an ID and name.
	Includes a constructor to initialize retailer attributes, a method to generate
	a unique retailer ID, and a string representation method. Ensures the uniqueness
	of retailer IDs by checking against a list of existing retailer IDs.
"""

# Import the 'random' module to generate random numbers
import random

# Define Retailer class
class Retailer:

	"""
	Methods:
		__init__(self, retailer_id = 12345678, retailer_name = "Chandler Bing"):
			Constructor method to initialize retailer attributes with default values.

		__str__(self):
			String representation of a retailer object.

		generate_retailer_id(self, list_retailer):
			Method to generate a unique 8-digit retailer ID.

		return_retailer_id(self, list_retailer):
			Method to return the retailer's ID if it exists in the list of retailer IDs,
			otherwise, returns None.
	"""

	def __init__(self, retailer_id = 12345678, retailer_name = "Chandler Bing"):
		"""
		Description:
			Constructor to initialize retailer attributes with default values.

		Arguments:
			self (Retailer): The Retailer object being created.
			retailer_id (int): Unique retailer ID (default: 12345678).
			retailer_name (str): Retailer's name (default: "Chandler Bing").
		
		Attributes:
			retailer_id (int): Unique retailer ID (default: 12345678).
			retailer_name (str): Retailer's name (default: "Chandler Bing").
		
		Return:
			None
		"""
		self.retailer_id = retailer_id
		self.retailer_name = retailer_name

	def __str__(self):

		"""
		Description:
			This method returns a formatted string representation of the retailer object.

		Arguments:
			self (Retailer): The Retailer object for which the string representation is generated.

		Return:
			str: A formatted string representing the retailer object, including its ID and name.
		"""

		return f"{self.retailer_id} {self.retailer_name}"
	
	def generate_retailer_id(self, list_retailer):

		"""
		Description:
			Generates a unique 8-digit retailer ID and checks it against the provided list of existing retailer IDs
			to ensure its uniqueness. If the generated ID is not unique, it keeps generating new IDs until a unique one is found.

		Arguments:
			self (Retailer): The Retailer object for which a unique ID is generated.
			list_retailer (list): The list of existing retailer IDs.

		Return:
			None
		"""

		retailer_id = random.randint(10000000, 99999999)
		# Check if the generated ID is already in the list of retailer IDs.
		if retailer_id in list_retailer:
			# If it is, generate a new ID until a unique one is found.
			while retailer_id in list_retailer:
				retailer_id = random.randint(10000000, 99999999)
		self.retailer_id = retailer_id
		# Add the generated unique ID to the list of retailer IDs.
		list_retailer.append(self.retailer_id)
		
	def return_retailer_id(self, list_retailer):
		
		"""
		Description:
			Returns the retailer's ID if it exists in the provided list of retailer IDs.
			If not found, it returns None.
		
		Arguments:
			self (Retailer): The Retailer object for which the retailer ID is retrieved.
			list_retailer (list): The list of existing retailer IDs.
		
		Return:
			int or None: The retailer's ID if found, otherwise None.
		"""

		for id in list_retailer:
			if id == self.retailer_id:
				return self.retailer_id
			else:
				return None