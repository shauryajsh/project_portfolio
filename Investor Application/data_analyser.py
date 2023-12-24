"""
Name: Shaurya Joshi
Student ID: 34034897
Creation date: 17 October 2023
Last modified date: 21 October 2023

Description:
	The SimpleDataAnalyser class provides a range of functions to work with property data.
	It enables you to import property information from CSV files, convert property prices
	using currency exchange, create summaries of property details for specific suburbs,
	and compute average land sizes. This class is a used for analyzing property-related data.
"""

import numpy as np
import pandas as pd

class SimpleDataAnalyser:
    def extract_property_info(self, file_path):

        """
        Description:
            Retrieves property data from a CSV file.

        Parameters:
            file_path (str): The file path to the CSV file that holds property information.

        Returns:
            file_data: A DataFrame containing property data from the CSV file.
        """

        try:
            file_data = pd.read_csv(file_path)
            return file_data
        except FileNotFoundError:
            print("File not found: ", file_path, "\nPlease provide a valid path for the file.")
            return None
        except Exception as e:
            print("Error in reading the file ", e)
            return None

    def currency_exchange(self, dataframe, exchange_rate):

        """
        Description:
            Converts property prices to a different currency.

        Parameters:
            dataframe (pandas dataframe): A DataFrame containing property information.
            exchange_rate (float): The exchange rate for currency conversion.

        Returns:
            converted_prices_array: An array of converted property prices.
        """

        try:
            # Remove rows with blank price information
            dataframe = dataframe[dataframe['price'].notna()]
            # Perform currency conversion based on the exchange rate
            converted_prices = dataframe['price'] * exchange_rate
            # Convert the outcome into a NumPy array and return the array
            converted_prices_array = np.array(converted_prices)
            return converted_prices_array
        except KeyError:
            print("Unable to find the column 'Price' in the dataset.")
            return None

    def suburb_summary(self, dataframe, suburb):

        """
        Description:
            Generates a summary of property details for a specific suburb.

        Parameters:
            dataframe (pandas dataframe): A DataFrame containing property information.
            suburb (str): The name of the suburb for which the summary is requested.
                          Use 'all' to get a summary for all suburbs.

        Returns:
            None
        """

        if suburb.lower() == 'all':
            specified_suburb = dataframe
        else:
            specified_suburb = dataframe[dataframe['suburb'].str.lower() == suburb.lower()]

        # Calculate the statistics of the dataset and show a summary of property details.
        property_details = specified_suburb[['bedrooms', 'bathrooms', 'parking_spaces']].describe().loc[[
             'count', 'mean', '50%', 'std', 'min', 'max']]
        property_details = property_details.rename(index={'50%': 'median'})
        print("Property details are listed below:")
        print(property_details)

    def avg_land_size(self, dataframe, suburb):

        """
        Description:
            Calculates the average land size in square meters for a specific suburb.

        Parameters:
            dataframe (pandas dataframe): A DataFrame containing property information.
            suburb (str): The name of the suburb for which the average land size is calculated.
        Use 'all' to get the average for all suburbs.

        Returns:
            size: The average land size in square meters for the specified suburb.
        """

        if suburb.lower() == 'all':
            specified_suburb = dataframe
        else:
            specified_suburb = dataframe[dataframe['suburb'].str.lower() == suburb.lower()]

        # Exclude rows with blank or negative land size values.
        specified_suburb = specified_suburb[specified_suburb['land_size'].notna()]
        specified_suburb = specified_suburb[specified_suburb['land_size'] >= 0]

        # If necessary, convert land size values from hectares to square meters.
        if (specified_suburb['land_size_unit'] == 'ha').any():
            mask = specified_suburb['land_size_unit'] == 'ha'
            specified_suburb['land_size'] = np.where(mask, specified_suburb['land_size'] * 10000,
                                                     specified_suburb['land_size'])
        if not specified_suburb.empty:
            size = np.mean(specified_suburb['land_size'])
            return size
        else:
            return None