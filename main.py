"""Simple pay calculator script"""
# Create variables
hourly_rate = 0
hours_worked = 0


def calculate_base_pay():
    """Perform base pay calculation"""
    base_pay = float(hours_worked) * float(hourly_rate)
    return base_pay


def main():

    print("Base pay = $" + str(calculate_base_pay()))


main()
