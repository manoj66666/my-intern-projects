# Length Converter

def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def length_converter():
    print("Length Converter")
    while True:
        try:
            value = float(input("Enter the value: "))
            source_unit = input("Enter the source unit (meters or feet): ").strip().lower()
            target_unit = input("Enter the target unit (meters or feet): ").strip().lower()

            if source_unit == "meters" and target_unit == "feet":
                result = meters_to_feet(value)
                print(f"{value} meters is equal to {result} feet.")
            elif source_unit == "feet" and target_unit == "meters":
                result = feet_to_meters(value)
                print(f"{value} feet is equal to {result} meters.")
            else:
                print("Unsupported units. Please enter 'meters' or 'feet' for source and target units.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")
        finally:
            another_conversion = input("Do you want to perform another conversion? (yes/no): ").strip().lower()
            if another_conversion != "yes":
                break

length_converter()
