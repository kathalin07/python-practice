weight = int(input("Enter your weight:"))
units = input("lbs or Kg:")
if units.upper() == "L":
    converted = weight*0.45
    print(f"your weight is{converted} kilos")
else:
    converted = weight/0.45
    print(f"your weight is{converted} pounds")
