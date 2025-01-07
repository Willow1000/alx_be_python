FAHRENHEIT_TO_CELSIUS = lambda f: (f - 32) * 5/9
CELCIUS_TO_FAHRENHEIT = lambda c: (c * 9/5) + 32

def convert_to_celcius(fahrenheit):
    return FAHRENHEIT_TO_CELSIUS(fahrenheit)

def convert_to_fahrenheit(celcius):
    return CELCIUS_TO_FAHRENHEIT(celcius)

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