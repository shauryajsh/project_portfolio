"""
Name: Shaurya Joshi
Student ID: 34034897
Creation date: 19 October 2023
Last modified date: 21 October 2023

Description:
	The DataVisualiser class is implemented for visualizing and analyzing property-related data.
	It includes several methods to interact with property datasets, providing valuable insights
	for decision-making and analysis. This class allows users to visualize the distribution of
	property values in a specific suburb and provides the flexibility to choose a target currency
	for price conversion. It displays the annual property sales trend, enabling the assessment
	of property sales trends over time. User can locate specific property prices within the data
	of a given suburb using a combination of reverse insertion sort and recursive binary search.
    These methods allow users to get a detailed analysis for various property-related insights.
"""

from data_analyser import SimpleDataAnalyser
import matplotlib.pyplot as plt
import pandas as pd

class DataVisualiser:
    def prop_val_distribution(self, dataframe, suburb, target_currency = "AUD"):

        """
        Description:
            Visualize the property value distribution for a specific suburb.

        Parameters:
            dataframe (pandas dataframe): DataFrame containing property data.
            suburb (str): The name of the suburb to analyze.
            target_currency (str): The target currency for property values. Defaults to value "AUD".

        Returns:
            None
        """

        data_analyser = SimpleDataAnalyser()
        currency_dic = {"AUD": 1, "USD": 0.66, "INR": 54.25, "CNY": 4.72, "JPY": 93.87,
                        "HKD": 5.12, "KRW": 860.92, "GBP": 0.51, "EUR": 0.60, "SGD": 0.88}

        # Verify if the suburb is not present in the dataset and set it to 'all' to consider all suburbs.
        if suburb.lower() != 'all' and suburb.lower() not in dataframe['suburb'].str.lower().values:
            print("Suburb '" + suburb + "' is not present in the dataset. Considering all suburbs to be shown.")
            suburb = 'all'
        # Narrow down the dataset based on the selected suburb if suburb value is not 'all'.
        if suburb.lower() != 'all':
            dataset = dataframe[dataframe['suburb'].str.lower() == suburb.lower()]
        else:
            dataset = dataframe
        # Check the 'price' column in the dataset.
        if 'price' in dataframe.columns:
            # Check if currency code is present in currency dictionary and proceed
            if target_currency in currency_dic:
                # Perform currency exchange operation utilizing the method from class SimpleDataAnalyser.
                dataset = data_analyser.currency_exchange(dataset, currency_dic[target_currency])
                dataset = pd.DataFrame(dataset).reset_index()
                dataset = dataset.rename(columns={0: 'price'})
                # Visualize the property value distribution and show it using a graphical plot.
                if not dataset.empty:
                    plt.hist(dataset['price'], edgecolor='black')
                    plt.xlabel("Property Value in " + target_currency)
                    plt.ylabel("Number of Properties")
                    plt.title("Property Value Distribution of Suburb: " + suburb.upper())
                    # To display the histogram, uncomment the below line
                    # plt.show()
                    plt.savefig("property_value_distribution.png")
                else:
                    print("No data present to display")
            # If currency code is not present in currency dictionary, take the default currency value 'AUD'
            else:
                print("Target currency not present in dictionary. Using the default currency 'AUD'.")
                target_currency = 'AUD'
                # Visualize the property value distribution and show it using a graphical plot.
                if not dataframe.empty:
                    plt.hist(dataframe['price'], edgecolor='black')
                    plt.xlabel("Property Value in " + target_currency)
                    plt.ylabel("Number of Properties")
                    plt.title("Property Value Distribution of Suburb " + suburb.upper())
                    # To display the histogram, uncomment the below line
                    # plt.show()
                    plt.savefig("property_value_distribution.png")
                else:
                    print("No data present to display")
        else:
            print("Price column not found in the dataset")

    def sales_trend(self, dataframe):

        """
        Description:
            Display the yearly property sales trend.

        Parameters:
            dataframe (pandas dataframe): DataFrame containing property data having a 'sold_date' column.

        Returns:
            None
        """

        try:
            # Verify if 'sold_date' column is present in the dataframe.
            if 'sold_date' not in dataframe.columns:
                print("Unable to find date column in the dataset. Cannot create a sales trend chart.")
            else:
                # Converting the 'sold_date' to datetime using formatting.
                dataframe['sold_date'] = pd.to_datetime(dataframe['sold_date'], format = '%d/%m/%Y')
                dataframe['year'] = dataframe['sold_date'].dt.year
                # Group the data by year and generate a line plot illustrating the annual sales trend.
                sales_year_data = dataframe.groupby('year').size()
                sales_year_data.plot(kind = 'line', marker = 'o')
                plt.title("Annual Property Sales Trend")
                plt.xlabel("Year")
                plt.ylabel("Number of Properties Sold")
                plt.grid(True)
                plt.savefig("annual_sales_trend.png")
                # To display the line chart, uncomment the below line
                # plt.show()
        except Exception as e:
            print("Error found:", e)

    def locate_price(self, target_price, data, target_suburb):

        """
        Description:
            Find a particular property price within the data of a suburb using reverse insertion sort
            and recursive binary search.

        Parameters:
            target_price (float): The specific price to locate.
            data (pandas dataframe): DataFrame containing property data.
            target_suburb (str): The name of the suburb in which to search for the price.

        Returns:
            boolean value: True if the target price exists in the suburb's data, False otherwise.
        """

        suburb_data = data[data['suburb'].str.lower() == target_suburb.lower()]
        # Retrieve the property prices from the suburb's data and arrange them in descending order.
        price_list = suburb_data['price'].dropna().tolist()
        for i in range(1, len(price_list)):
            key_value = price_list[i]
            j = i - 1
            while j >= 0 and key_value > price_list[j]:
                price_list[j + 1] = price_list[j]
                j -= 1
            price_list[j + 1] = key_value

        # Creating a recursive binary search function to find the target price within the sorted list.
        def binary_search(arr, low, high, target):
            if high >= low:
                mid = (low + high) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] > target:
                    return binary_search(arr, mid + 1, high, target)
                else:
                    return binary_search(arr, low, mid - 1, target)
            else:
                print("There is no data present for this price in the targeted suburb.")
                return False

        return binary_search(price_list, 0, len(price_list) - 1, target_price)