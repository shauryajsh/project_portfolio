"""
Name: Shaurya Joshi
Student ID: 34034897
Creation date: 18 October 2023
Last modified date: 22 October 2023

Description:
	The main class functions as the central component of the Investor Application,
	acting as the entry point from where the whole program will run. It imports both
	SimpleDataAnalyser and DataVisualiser classes to establish
	a user-friendly, menu-driven interface for engaging with property datasets.
	Through this application, users can carry out a range of operations,
	including tasks like currency conversion, the examination of suburb property summaries,
	the computation of average land sizes, exploration of property value distributions,
	scrutiny of sales trends, and pinpointing property prices within specific suburbs.
    Within the main function, it manages user input, presenting the menu for action selection,
    and ensuring robust error handling to validate inputs .

    Parameters:
    None

    Returns:
    None
"""

from data_analyser import SimpleDataAnalyser
from data_visualiser import DataVisualiser

def main():
    # Path of property information file
    file_path = 'property_information.csv'
    # Creating an instance of SimpleDataAnalyser class
    data_analyser = SimpleDataAnalyser()
    # Creating and instance of DataVisualiser class
    data_visualiser = DataVisualiser()
    while True:
        try:
            # Extract property information from the CSV file
            dataframe = data_analyser.extract_property_info(file_path)

            # Creating a function to display menu to the user
            def show_menu():
                print()
                print("=============================")
                print("||Investor Application Menu||")
                print("=============================")
                print("1. Perform Currency Exchange")
                print("2. View Suburb Property Summary")
                print("3. Calculate Average Land Size")
                print("4. Explore Property Value Distribution")
                print("5. Analyse Sales Trends")
                print("6. Find Prices in a Specific Suburb")
                print("7. Exit")
                print()

            while True:
                # Calling out the function to show user menu
                show_menu()
                # Ask user for entering the menu choice
                choice = input("Select an option (1-7): ")
                # Choice 1 is to get the converted currency
                if choice == '1':
                    while True:
                        try:
                            exchange_rate = input("Enter the exchange rate: ")
                            if not exchange_rate:
                                raise ValueError("Exchange rate cannot be blank. Please enter a valid exchange rate.")
                            try:
                                exchange_rate = float(exchange_rate)
                            except ValueError:
                                raise ValueError("The entered value is not a valid numeric value.")
                            if exchange_rate < 0:
                                raise ValueError("The exchange rate cannot be negative. "
                                                 "Please enter a valid exchange rate.")
                            elif exchange_rate == 0:
                                raise ValueError("The exchange rate cannot be 0. Please enter a valid exchange rate.")
                            else:
                                transformed_prices = data_analyser.currency_exchange(dataframe, exchange_rate)
                                print("Converted prices: ", transformed_prices)
                                break
                        except ValueError as e:
                            print("Invalid input:", e)
                # Choice 2 is to get the suburb property summary
                elif choice == '2':
                    while True:
                        try:
                            suburb = input("Enter the suburb (or 'all' to include all suburbs) to analyse: ")
                            if not suburb:
                                raise ValueError("Suburb name cannot be blank. Please enter a valid suburb name.")
                            if not all(char.isalpha() or char.isspace() for char in suburb):
                                raise ValueError("Please provide a valid suburb name containing "
                                                 "only alphabetic characters.")
                            if suburb.lower() not in dataframe['suburb'].str.lower().values and suburb.lower() != 'all':
                                raise ValueError("The entered suburb is not present. Please enter a valid suburb name.")
                            data_analyser.suburb_summary(dataframe, suburb)
                            break
                        except ValueError as e:
                            print("Invalid input:", e)
                # Choice 3 is to calculate the average land size
                elif choice == '3':
                    while True:
                        try:
                            suburb = input("Enter the suburb (or 'all' to include all suburbs) to analyse: ")
                            if not suburb:
                                raise ValueError("Suburb name cannot be blank. Please enter a valid suburb name.")
                            if not all(char.isalpha() or char.isspace() for char in suburb):
                                raise ValueError("Please provide a valid suburb name containing "
                                                 "only alphabetic characters.")
                            if suburb.lower() not in dataframe['suburb'].str.lower().values and suburb.lower() != 'all':
                                raise ValueError("The entered suburb is not present. Please enter a valid suburb name.")
                            size = data_analyser.avg_land_size(dataframe, suburb)
                            if size is None:
                                print("Suburb does not exist. Please enter another valid suburb name.")
                            else:
                                print("The average size of the land is:", size, "sq. meters")
                                break
                        except ValueError as e:
                            print("Invalid input:", e)
                # Choice 4 is to show a visualisation graph as a histogram
                elif choice == '4':
                    while True:
                        try:
                            suburb = input("Enter the suburb (or 'all' to include all suburbs) to analyse: ")
                            if not suburb:
                                raise ValueError("Suburb name cannot be blank. Please enter a valid suburb name.")
                            if not all(char.isalpha() or char.isspace() for char in suburb):
                                raise ValueError("Please provide a valid suburb name containing "
                                                 "only alphabetic characters.")
                            while True:
                                try:
                                    target_currency = input("Enter the target currency (eg. USD, AUD, etc.) (default "
                                                            "currency is taken as 'AUD' if target "
                                                            "currency is not present): ").upper()
                                    data_visualiser.prop_val_distribution(dataframe, suburb, target_currency)
                                    break
                                except ValueError as e:
                                    print("Invalid input:", e)
                            break
                        except Exception as e:
                            print("Invalid input:", e)
                # Choice 5 is to display the annual sales trend as a line chart
                elif choice == '5':
                    try:
                        data_visualiser.sales_trend(dataframe)
                    except Exception as e:
                        print("Error found:", e)
                # Choice 6 is to locate if any targeted price is present in the price list of a specific suburb
                elif choice == '6':
                    while True:
                        try:
                            target_suburb = input("Enter the suburb to analyse: ")
                            if not target_suburb:
                                raise ValueError("Suburb name cannot be blank. Please enter a valid suburb name.")
                            if not all(char.isalpha() or char.isspace() for char in target_suburb):
                                raise ValueError("Please provide a valid suburb name "
                                                 "containing only alphabetic characters.")
                            if target_suburb.lower() not in dataframe['suburb'].str.lower().values:
                                raise ValueError("The targeted suburb is not present. Please enter a valid suburb name.")
                            while True:
                                try:
                                    target_price = input("Enter the target price: ")
                                    if not target_price:
                                        raise ValueError("Price cannot be blank. Please enter a valid numeric value.")
                                    try:
                                        target_price = float(target_price)
                                        result = data_visualiser.locate_price(target_price, dataframe, target_suburb)
                                        if result is True:
                                            print("This value of price is present in the targeted suburb.")
                                        break
                                    except ValueError:
                                        print("The entered value is not a valid numeric value. "
                                              "Please enter the details again.")
                                except ValueError as e:
                                    print("Invalid input:", e)
                            break
                        except ValueError as e:
                            print("Invalid input:", e)
                # Use Choice 7 to exit the investor application
                elif choice == '7':
                    print("Exiting the application.")
                    break
                # If any choice other than the given choices is entered, then show as invalid input
                else:
                    print("Invalid input. Please select an option between (1-7).")
            break
        except Exception:
            print("File Not Found. Please check the file path.")
        break

if __name__ == "__main__":
    main()

# # Test Code
# sda = SimpleDataAnalyser()
# dv = DataVisualiser()

# # Extract Property Information
# file_path = 'property_information.csv'
# df = sda.extract_property_info(file_path)
# # Print to see the output of the dataframe
# print(df)

# # Currency Exchange
# exchange_rate = 0.66
# transformed_prices = sda.currency_exchange(df, exchange_rate)
# # Output
# # [636900. 267300. 581460. ... 500280. 442200. 343728.]

# # Suburb Summary
# suburb = Caulfield
# sda.suburb_summary(df, suburb_name)
# # Output
# # Property details are listed below:
# #           bedrooms   bathrooms  parking_spaces
# # count   972.000000  972.000000      972.000000
# # mean      2.853909    1.756173        1.656379
# # median    3.000000    2.000000        2.000000
# # std       1.057198    0.756171        0.719903
# # min       0.000000    1.000000        0.000000
# # max       7.000000    6.000000        6.000000

# # Average Land Size
# suburb = Clayton
# size = sda.avg_land_size(df, suburb)
# # Output
# # The average size of the land is: 571.0422074788902 sq. meters

# # Property Value Distribution
# suburb = all
# target_currency = HKD
# sda.prop_val_distribution(df, suburb, target_currency)
# # Output will display the histogram image on running the code

# # Sales Trend
# sda.sales_trend(df)
# # Output will display the line chart on running the code

# # Locate Price
# target_suburb = Clayton
# target_price = 465000
# result = sda.locate_price(target_price, df, target_suburb)
# # Output - True
# # This value of price is present in the targeted suburb.