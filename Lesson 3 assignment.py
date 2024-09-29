# interest_calculation.py

# User input for the investment amount
investment_amount = int(input("Enter an investment amount (greater than 0 and less than 50,000): "))
while investment_amount <= 0 or investment_amount >= 50000:
    print("Invalid investment amount. Please enter a value greater than 0 and less than 50,000.")
    investment_amount = int(input("Enter an investment amount (greater than 0 and less than 50,000): "))

# User input for interest rate.
annual_interest_rate = int(input("Enter an interest rate (greater than 0 and less than 15): "))
while annual_interest_rate <= 0 or annual_interest_rate >= 15:
    print("Invalid interest rate. Please enter a value greater than 0 and less than 15.")
    annual_interest_rate = int(input("Enter an interest rate (greater than 0 and less than 15): "))

# User input for investment in years.
investment_duration_years = int(input("Enter the duration of the investment in years (greater than 0): "))
while investment_duration_years <= 0:
    print("Invalid duration. Please enter a value greater than 0.")
    investment_duration_years = int(input("Enter the duration of the investment in years (greater than 0): "))

# duration from years to months
# calculate the monthly interest rate
total_months = investment_duration_years * 12
monthly_interest_rate = (annual_interest_rate / 12) / 100

# Start with the  investment as total amount
total_investment = investment_amount

# Loop through each month to calculate the compounded investment
for month in range(1, total_months + 1):
    # Calculate interest for the current month
    interest_earned = round(total_investment * monthly_interest_rate, 2)
    total_investment += round(interest_earned, 2)

    # If it's the end of a year, print the current investment value
    if month % 12 == 0:
        current_year = month // 12
        print(f"Year {current_year}: Investment value is ${round(total_investment, 2):,.2f}")

# end
print(f"\nTotal investment after {investment_duration_years} years at an annual interest rate of {annual_interest_rate}%")
print(f"Monthly investment amount: ${round(investment_amount, 2):,.2f}")
print(f"Total amount of investment After compounding: ${round(total_investment, 2):,.2f}")

print("Completed by, Armando Gaona")
