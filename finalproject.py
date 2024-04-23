'''Import necessary libraries'''
import requests
from bs4 import BeautifulSoup
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import tkinter as tk
from tkinter import messagebox

'''Web scraping to collect car listing data'''
def scrape_car_data(make, model, year, mileage, condition, location):
    url = f"https://example.com/cars/{make}/{model}/{year}"
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the response using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")
        # Extract relevant data from the webpage
        # Will replace this with actual scraping logic based on the website structure
        price_tag = soup.find("span", class_="price")
        if price_tag:
            price = float(price_tag.text.replace("$", "").replace(",", ""))
            return {"price": price}
    return None

'''User interface for inputting car information and displaying results'''
def create_user_interface():
    # Your GUI code here
    pass

'''Main function to orchestrate the project'''
def main():
    # Input variables
    make = input("Enter the make of the car: ")
    model = input("Enter the model of the car: ")
    year = int(input("Enter the year of the car: "))
    mileage = int(input("Enter the mileage of the car: "))
    condition = input("Enter the condition of the car (e.g., excellent, good, fair, poor): ")
    location = input("Enter the location of the car: ")

    '''Scrape car data'''
    car_data = scrape_car_data(make, model, year, mileage, condition, location)

    '''Estimate car value'''
    estimated_value = estimate_car_value(car_data)

    '''Display results'''
    print(f"Estimated value of the car: ${estimated_value}")

def get_car_info():
    """
     This will ask the user to input the car info needed.

    Asks the user to input details about their  such as car, including make, model,
    year, mileage, condition, and location.

    Returns:
        tuple: Contains the car's make, model, year, mileage, condition, and location.
    """
    print("Please enter the following information about your car:")
    make = input("Make: ")
    model = input("Model: ")
    year = input("Year: ")
    mileage = input("Mileage: ")
    condition = input("Condition (Excellent, Good, Fair, Poor): ")
    location = input("Location (City/State): ")
    return make, model, year, mileage, condition, location

'''Machine learning model to estimate car values'''
def estimate_car_value(year, mileage, condition, average_market_price):
    """
    This function will estimate the car's value based on year, mileage, condition, and the average market price.

    Parameters:
        year (str): The manufacture year of the car.
        mileage (str): The current mileage of the car.
        condition (str): The used condition of the car (Excellent, Good, Fair, Poor).
        average_market_price (float): The average market price of the car based on data collected.

    Returns:
        float: The estimated value of the car.
    """
   
    # Simplified estimation logic will work on more later
    condition_multiplier = {"Excellent": 1.1, "Good": 1.0, "Fair": 0.9, "Poor": 0.8}
    age = 2024 - int(year)  # Assuming the current year is 2024
    depreciation = age * 0.05
    estimated_value = average_market_price * condition_multiplier[condition] * (1 - depreciation)
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
