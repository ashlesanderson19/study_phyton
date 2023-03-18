def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit

def convert_fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    return celsius

print("Welcome to the temperature converter!")
print("1. Convert Celsius to Fahrenheit")
print("2. Convert Fahrenheit to Celsius")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = convert_celsius_to_fahrenheit(celsius)
    print("{:.1f} Celsius is equivalent to {:.1f} Fahrenheit".format(celsius, fahrenheit))
elif choice == 2:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = convert_fahrenheit_to_celsius(fahrenheit)
    print("{:.1f} Fahrenheit is equivalent to {:.1f} Celsius".format(fahrenheit, celsius))
else:
    print("Invalid choice. Please enter 1 or 2.")
