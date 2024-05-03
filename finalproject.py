'''Import necessary libraries'''
import requests

'''Web scraping to collect car listing data'''
def get_car_data(make, model, year):
    """
    Fetches car data from an API based on the make, model, and year of the car.

    Parameters:
        make (str): The make of the car (e.g., Toyota, Honda).
        model (str): The model of the car (e.g., Camry, Civic).
        year (int): The year of the car.

    Returns:
        dict or None: A dictionary containing car data if the request is successful,
        otherwise None.x
    """
    url=f'https://zylalabs.com/api/2061/car+market+value+api/2775/get+vehicle+value?maker={make}&model={model}&year={year}'
    headers = {"Content-Type": "application/json","Authorization": r"Bearer Bearer 4369|sKvQ8eqHsKUXvjBLLhdI07Formz3T3RjhLf4PoIw"}
    response = requests.get(url, headers=headers, verify=False)
    if response.status_code == 200:
        return response.json()
    else:
        print(response.status_code)

print(get_car_data('audi', 'a3', 2020))

'''Main function to orchestrate the project'''
def main():
    make = input("Enter the make of the car: ")
    model = input("Enter the model of the car: ")
    year = int(input("Enter the year of the car: "))

    '''Scrape car data'''
    car_data = get_car_data(make, model, year)

    if car_data:
        average_market_price = car_data.get("average_market_price")
        if not average_market_price:
            print("Unable to fetch average market price. Please try again later.")
            return

        '''Estimate car value'''
        estimated_value = estimate_car_value(year, average_market_price)

        '''Display results'''
        print(f"Estimated value of the car: ${estimated_value}")

        '''Provide recommendations'''
        provide_recs(estimated_value, average_market_price)
    else:
        print("Failed to fetch car data. Please check your inputs and try again.")

def get_car_info():
    """
    This will ask the user to input the car info needed.

    Asks the user to input details about their  such as car, including make, model,
    year.

    Returns:
        tuple: Contains the car's make, model, year
    """
    print("Please enter the following information about your car:")
    make = input("Make: ")
    model = input("Model: ")
    year = input("Year: ")
    return make, model, year

'''Machine learning model to estimate car values'''
def estimate_car_value(year, average_market_price):
    """
    This function will estimate the car's value based on year, and the average market price.

    Parameters:
        year (str): The manufacture year of the car.
        average_market_price (float): The average market price of the car based on data collected.

    Returns:
        float: The estimated value of the car.
    """

    age = 2024 - int(year)  # Assuming the current year is 2024
    depreciation = age * 0.05
    estimated_value = average_market_price * (1 - depreciation)
    return max(estimated_value, 1000)  # Ensure the car value doesn't go below $1000

def provide_recs(estimated_value, average_market_price):
    """
    This function will provide recommendations about negotiating the selling price based on the estimated value and average market price.

    Parameters:
        estimated_value (float): The estimated value of the car based on the info provided.
        average_market_price (float): The average market price of similar cars in similar conditio s.

    The function then prints a recommendation for the user on how to proceed with selling their car based on the comparison
    between the estimated value and the average market price.
    """
    if estimated_value > average_market_price:
        print("Your car's estimated value is higher than the average market price. You have a good chance of negotiating a higher selling price.")
    elif estimated_value < average_market_price:
        print("Your car's estimated value is lower than the average market price. Be prepared for tough negotiations, and consider setting a slightly higher asking price.")
    else:
        print("Your car's estimated value matches the average market price. You're in a good position to start negotiations.")


'''Call the main function'''
if __name__ == "__main__":
    main()
