FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELCIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celcius(fahrenheit):
    return (fahrenheit - 32) *FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celcius):
    return (CELCIUS_TO_FAHRENHEIT_FACTOR*celcius) + 32

def main():
    temperature = float(input("Enter temperature to convert: "))
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if unit == 'C':
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {result}°F")
    elif unit == 'F':
        result = convert_to_celcius(temperature)
        print(f"{temperature}°F is {result}°C")
    else:
        print("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")
if __name__ == "__main__":
    main()