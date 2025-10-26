"""
Name: Shaurya Joshi
Student ID: 34034897
Creation date: 20 Sept 2023
Last modified date: 24 Sept 2023

Description:
	This is the main file containing different functions
"""

# Import necessary classes and modules
from car import Car
from car_retailer import CarRetailer
# Import the 'random' module to generate random numbers
import random

def main_menu():

	"""
    Description:
    	Function to display the main menu options.

    Arguments:
    	None

    Returns:
    	None
    """

	print()
	print("==========================================")
	print("||     CAR PURCHASE ADVISORY SYSTEM     ||")
	print("==========================================")
	print()
	print("=================MENU=================")
	print("a) Look for the nearest car retailer")
	print("b) Get car purchase advice")
	print("c) Place a car order")
	print("d) Exit")

def generate_test_data():

	"""
    Description:
    	Function to generate test data for car retailers and cars.

    Arguments:
    	None

    Returns:
    	None
    """

	try:
		retailer_names = ['Jeff Hardy', 'Pepe', 'Wayne Rooney', 'Luka Modric', 'Richarlison', 'Toni Kroos', 
					'Ronaldo', 'Sergio Ramos', 'Harry Kane', 'David Alaba', 'Alison', 'Ben White', 'Valverde', 
					'Aaron Ramsdale', 'Oliver Kahn']
		address = ['Center Road Clayton, VIC3168', 'Harry Road Burwood, VIC3291', 'Clayton Road Mulgrave, VIC3255', 
				'Wellington Road Springvale, VIC3165', 'Wall Street Southland, VIC3000', 'Broad Steet Oakleigh, VIC3482', 
				'Scotsburn Avenue Keysborough, VIC3200', 'Kyle Street Carlington, VIC3050', 'Donald Road Melton, VIC3120', 
				'End Road Ashwood, VIC3442', 'Dale Avenue Carlton, VIC3370']
		car_companies = ['Audi', 'Mercedes', 'BMW', 'Porche', 'Lexus', 'Honda', 'Hyundai', 'Jeep', 
				   'Toyota', 'Nissan', 'Skoda', 'Ford', 'Jaguar', 'MG', 'Volvo', 'Kia', 'Bentley', 'Fiat', 'Mazda']
		retailer_data = ''
		file_data = ''
		for _ in range(3):
			car_retailer = CarRetailer()
			retailer_number = []
			car_retailer.generate_retailer_id(retailer_number)
			car_retailer.retailer_name = random.choice(retailer_names)
			car_retailer.carretailer_address = random.choice(address)
			start_hour = round(random.uniform(6.00, 23.00), 2)
			end_hour = round(random.uniform(6.00, 23.00), 2)
			while end_hour <= start_hour:
				start_hour = round(random.uniform(6.00, 23.00), 2)
				end_hour = round(random.uniform(6.00, 23.00), 2)
			car_retailer.carretailer_business_hours = (start_hour, end_hour)
			retailer_data = str(car_retailer.retailer_id) + ", " + car_retailer.retailer_name + ", " + str(car_retailer.carretailer_address) + ", " + str(car_retailer.carretailer_business_hours)
			car_data = ''
			car_stock_data = []
			for _ in range(4):
				car = Car()
				car.car_code = ''
				for i in range(8):
					if i == 0 or i == 1:
						car.car_code = car.car_code + random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
					else:
						car.car_code = car.car_code + str(random.randint(0, 9))
				car.car_name = random.choice(car_companies)
				car.car_capacity = random.randint(2, 8)
				car.car_horsepower = random.randint(50, 2500)
				car.car_weight = round(random.uniform(700, 3000), 2)
				car.car_type = random.choice(['FWD', 'RWD', 'AWD'])
				car_data = str(car.car_code) + ", " + car.car_name + ", " + str(car.car_capacity) + ", " + str(car.car_horsepower) + ", " + str(car.car_weight) + ", " + car.car_type
				car_stock_data.append(car_data)
			file_data = file_data + f"{retailer_data}{', '}{car_stock_data}\n"
		file_path = 'stock.txt'
		with open(file_path, 'w') as new_file:
			new_file.write(file_data)
	except FileNotFoundError:
			print("File not found: ", file_path)
	except Exception as e:
		print("Error encountered while generating test data: ", e)

def retrieve_carretailer_data():

	"""
    Description:
    	Function to retrieve car retailer data from a file.

    Arguments:
    	None

    Returns:
    	retailer_object: A list of CarRetailer objects.
    """

	try:
		# Define the path to the data file
		file_path = 'stock.txt'
		# Open the file for reading
		with open(file_path, 'r') as file:
			# Read all lines from the file into a list
			single_line = file.readlines()
			# Initialize variables to store data
			car_retailer_data = []
			carretailer_stock = []
			car_retailer = CarRetailer()
			# Iterate through each line in the file
			for data in single_line:
				# Find the start position of the car retailer data
				start_position = data.find("[")
				# Extract the car retailer data as a string
				car_retailer_data = data[:start_position].strip()
				car_retailer_data = car_retailer_data[:-1]
				# Split the car retailer data into individual fields
				retailer_id, retailer_name, retailer_street_address, retailer_postal_code, retailer_start_hour, retailer_end_hour = car_retailer_data.split(', ')
				# Create the full address and business hours strings
				carretailer_address = retailer_street_address + ", " + retailer_postal_code
				carretailer_business_hours = retailer_start_hour + ", " + retailer_end_hour
				# Create a CarRetailer object with the extracted data
				car_retailer = CarRetailer(retailer_id, retailer_name, carretailer_address, carretailer_business_hours)
				# Append the CarRetailer object to the list
				carretailer_stock.append(car_retailer)
			# Return the list of CarRetailer objects
			retailer_object = carretailer_stock
			return retailer_object
	except FileNotFoundError:
		# Handle the case where the file is not found
		print("File not found: ", file_path)
	except Exception as e:
		# Handle any other exceptions
		print("An error occurred while retrieving stock data: ", e)

def retrieve_car_data():
	
	"""
	Description:
    	Function to retrieve car data from a file.

    Arguments:
    	None
	
	Returns:
		car_object: A list of car object
	"""

	try:
		# Define the path to the data file
		file_path = 'stock.txt'
		# Open the file for reading
		with open(file_path, 'r') as file:
			# Read all lines from the file into a list
			single_line = file.readlines()
			# Create empty Car objects
			car_object1 = Car()
			car_object2 = Car()
			car_object3 = Car()
			# Initialize variables to store data
			car_data_str = []
			car_data_list = []
			car_list = []
			# Iterate through each line in the file
			for data in single_line:
				# Find the start position of the car data
				start_position = data.find("[")
				# Extract the car data as a string
				car_data_str = data[start_position+2:-3].strip()
				car_data_str = car_data_str
				# Split the car data into a list
				car_data_list = car_data_str.split(', ')
				car_data_list = car_data_list
				 # Append the car data list to the car_list
				car_list.append(car_data_list)
			# Initialize variables to store individual car data
			carcode = ''
			carcodes_line1 = []
			carcodes_line2 = []
			carcodes_line3 = []
			carname = ''
			carnames_line1 = []
			carnames_line2 = []
			carnames_line3 = []
			carcapacity = ''
			carcapacity_line1 = []
			carcapacity_line2 = []
			carcapacity_line3 = []
			carhorsepower = ''
			carhorsepower_line1 = []
			carhorsepower_line2 = []
			carhorsepower_line3 = []
			carweight = ''
			carweight_line1 = []
			carweight_line2 = []
			carweight_line3 = []
			cartype = ''
			cartype_line1 = []
			cartype_line2 = []
			cartype_line3 = []
			
			# Loop through the car data and store it in respective variables and objects
			for i in range(0, len(car_list[0]), 6):
				# Storing data in every index in respective variables
				carcode = car_list[0][i]
				carcode = carcode.strip("'")
				carname = car_list[0][i+1]
				carcapacity = car_list[0][i+2]
				carhorsepower = car_list[0][i+3]
				carweight = car_list[0][i+4]
				cartype = car_list[0][i+5]
				cartype = cartype.strip("'")
				# Create a Car object with the extracted data
				car_object1 = Car(carcode, carname, carcapacity, carhorsepower, carweight, cartype)
				# Appending all data into respective lists
				carcodes_line1.append(car_list[0][i])
				carcodes_line1 = [code.strip("'") for code in carcodes_line1]
				carnames_line1.append(car_list[0][i+1])
				carcapacity_line1.append(car_list[0][i+2])
				carhorsepower_line1.append(car_list[0][i+3])
				carweight_line1.append(car_list[0][i+4])
				cartype_line1.append(car_list[0][i+5])
				cartype_line1 = [code.strip("'") for code in cartype_line1]

			# Loop through the car data and store it in respective variables and objects
			for i in range(0, len(car_list[1]), 6):
				# Storing data in every index in respective variables
				carcode = car_list[1][i]
				carcode = carcode.strip("'")
				carname = car_list[1][i+1]
				carcapacity = car_list[1][i+2]
				carhorsepower = car_list[1][i+3]
				carweight = car_list[1][i+4]
				cartype = car_list[1][i+5]
				cartype = cartype.strip("'")
				# Create a Car object with the extracted data
				car_object2 = Car(carcode, carname, carcapacity, carhorsepower, carweight, cartype)
				# Appending all data into respective lists
				carcodes_line2.append(car_list[1][i])
				carcodes_line2 = [code.strip("'") for code in carcodes_line2]
				carnames_line2.append(car_list[1][i+1])
				carcapacity_line2.append(car_list[1][i+2])
				carhorsepower_line2.append(car_list[1][i+3])
				carweight_line2.append(car_list[1][i+4])
				cartype_line2.append(car_list[1][i+5])
				cartype_line2 = [code.strip("'") for code in cartype_line2]

			# Loop through the car data and store it in respective variables and objects
			for i in range(0, len(car_list[2]), 6):
				# Storing data in every index in respective variables
				carcode = car_list[2][i]
				carcode = carcode.strip("'")
				carname = car_list[2][i+1]
				carcapacity = car_list[2][i+2]
				carhorsepower = car_list[2][i+3]
				carweight = car_list[2][i+4]
				cartype = car_list[2][i+5]
				cartype = cartype.strip("'")
				# Create a Car object with the extracted data
				car_object3 = Car(carcode, carname, carcapacity, carhorsepower, carweight, cartype)
				# Appending all data into respective lists
				carcodes_line3.append(car_list[2][i])
				carcodes_line3 = [code.strip("'") for code in carcodes_line3]
				carnames_line3.append(car_list[2][i+1])
				carcapacity_line3.append(car_list[2][i+2])
				carhorsepower_line3.append(car_list[2][i+3])
				carweight_line3.append(car_list[2][i+4])
				cartype_line3.append(car_list[2][i+5])
				cartype_line3 = [code.strip("'") for code in cartype_line3]

			# Return the Car object
			return car_object1
		#car_object2, car_object3
	except FileNotFoundError:
		# Handle the case where the file is not found
		print("File not found: ", file_path)
	except Exception as e:
		# Handle any other exceptions
		print("An error occurred while retrieving stock data: ", e)

def main():

	"""
    Description:
		This is the main function of the program.
    
    Arguments:
        None
        
    Returns:
        None
	"""
		
	# Generate test data
	generate_test_data()
	# Retrieve car retailer data
	retailer_list = retrieve_carretailer_data()
	# Retrieve car data
	car_list = retrieve_car_data()
	while True:
		# Display the main menu
		main_menu()
		# Valid choices for the menu
		choices = ['a','b','c','d']
		print()
		choice = input("ENTER YOUR CHOICE: ").lower()
		print()
		while choice not in choices:
			# Prompt for a valid choice if input is invalid
			choice = input("INVALID INPUT! PLEASE ENTER A VALID CHOICE (a/b/c/d): ").lower()
			print()

		if choice == 'a':
			# Option A: Find the closest car retailer based on postcode
			postcode = None
			while True:
				try:
					# Prompt for a valid 4-digit postcode
					postcode = input("Enter a valid 4 digit post code: ")
					postcode = int(postcode)
					if len(str(postcode)) != 4:
						raise ValueError("Post Code must be exactly 4 digits")
					break
				except ValueError as e:
					print("Invalid Input: ", e)
			# Calculate the postcode differences for each retailer
			postcode_difference1 = retailer_list[0].get_postcode_distance(postcode)
			print("Postal difference 1: ", postcode_difference1)
			postcode_difference2 = retailer_list[1].get_postcode_distance(postcode)
			print("Postal difference 2: ", postcode_difference2)
			postcode_difference3 = retailer_list[2].get_postcode_distance(postcode)
			print("Postal difference 3: ", postcode_difference3)
			# Find the minimum difference and display the closest retailer
			minimun = min(postcode_difference1, postcode_difference2, postcode_difference3)
			if minimun == postcode_difference1:
				print("The closest car retailer is located at: ", retailer_list[0].carretailer_address)
			if minimun == postcode_difference2:
				print("The closest car retailer is located at: ", retailer_list[1].carretailer_address)
			if minimun == postcode_difference3:
				print("The closest car retailer is located at: ", retailer_list[2].carretailer_address)
			
		elif choice == 'b':
			 # Option B: Display available car retailers and select a preferred retailer
			print("Available Car Retailers:")
			print("Retailer 1:")
			print("ID:", retailer_list[0].retailer_id, "Name:", retailer_list[0].retailer_name, 
			"Address:", retailer_list[0].carretailer_address, "Business Hours:", retailer_list[0].carretailer_business_hours)
			print("Retailer 2:")
			print("ID:", retailer_list[1].retailer_id, "Name:", retailer_list[1].retailer_name, 
			"Address:", retailer_list[1].carretailer_address, "Business Hours:", retailer_list[1].carretailer_business_hours)
			print("Retailer 3:")
			print("ID:", retailer_list[2].retailer_id, "Name:", retailer_list[2].retailer_name, 
			"Address:", retailer_list[2].carretailer_address, "Business Hours:", retailer_list[2].carretailer_business_hours)
			print()
			selected_retailer = None
			while selected_retailer not in (1, 2, 3):
				try:
					# Prompt for a valid retailer selection
					selected_retailer = int(input("Please select your preferred retailer - (1/2/3): "))
					if selected_retailer not in (1, 2, 3):
						print("Invalid input! Please select the option - (1/2/3): ")
				except ValueError:
					print("Invalid input! Please enter a valid integer value - (1/2/3): ")
			# Display the selected retailer
			if selected_retailer == 1:
				print("The selected retailer is: \nID:", retailer_list[0].retailer_id, "Name:", retailer_list[0].retailer_name, 
			"Address:", retailer_list[0].carretailer_address, "Business Hours:", retailer_list[0].carretailer_business_hours)
			if selected_retailer == 2:
				print("The selected retailer is: \nID:", retailer_list[1].retailer_id, "Name:", retailer_list[1].retailer_name, 
			"Address:", retailer_list[1].carretailer_address, "Business Hours:", retailer_list[1].carretailer_business_hours)
			if selected_retailer == 3:
				print("The selected retailer is: \nID:", retailer_list[2].retailer_id, "Name:", retailer_list[2].retailer_name, 
			"Address:", retailer_list[2].carretailer_address, "Business Hours:", retailer_list[2].carretailer_business_hours)
			
			# Displaying sub-menu options on selecting option B after user has selected a car retailer
			print()
			print("===============SUB-MENU===============")
			print("1) Recommend a car")
			print("2) Get all cars in stock")
			print("3) Get cars in stock by car types")
			print("4) Get probationary licence permitted cars in stock")
			print()
			
			sub_menu_option = None
			while sub_menu_option not in (1, 2, 3, 4):
				try:
					# Prompt for a valid option from the sub-menu
					sub_menu_option = int(input("Select an option from sub-menu - (1/2/3/4): "))
					if sub_menu_option not in (1, 2, 3, 4):
						print("Invalid input! Please select the option - (1/2/3/4): ")
				except ValueError:
					print("Invalid input! Please enter a valid integer value - (1/2/3/4): ")

			if sub_menu_option == 1:
				# Option 1: Recommend a car
				print()
			elif sub_menu_option == 2:
				# Option 2: Get all cars in stock
				print("Displaying the list of all cars in stock")
			elif sub_menu_option == 3:
				 # Option 3: Get cars in stock by car types
				print("Displaying the list of cars in stock car based on car types")
			elif sub_menu_option == 4:
				# Option 4: Get probationary licence permitted cars in stock
				print("Displaying probationary licence permitted cars in stock")

		elif choice == 'c':
			# Option C: Place an order
			print("Congratulations on placing your car order!")

		elif choice == 'd':
			# Option D: Exit the menu
			print("EXITING THE MENU")
			break

# This part checks if the current module is being run as the main program
if __name__ == "__main__":
	main()