import requests

def get_car_data(make, model, year):
    """
    Fetches car data from an API based on the make, model, and year of the car.

    Parameters:
        make (str): The make of the car (e.g., Toyota, Honda).
        model (str): The model of the car (e.g., Camry, Civic).
        year (int): The year of the car.

    Returns:
        dict or None: A dictionary containing car data if the request is successful,
        otherwise None.
    """
    url = f'https://zylalabs.com/api/2061/car+market+value+api/2775/get+vehicle+value?maker={make}&model={model}&year={year}'
    headers = {"Content-Type": "application/json", "Authorization": r"Bearer Bearer 4369|sKvQ8eqHsKUXvjBLLhdI07Formz3T3RjhLf4PoIw"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for unsuccessful requests
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching car data: {e}")
        return None

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

if __name__ == "__main__":
    main()
