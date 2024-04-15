# Initialize the parking dictionary with pre-defined car plate numbers and positions
parking = {
    "MH04CC2": 1,
    "MH04C2820": 2,
    "MHO4BB3232": 3,
    "MH04CC2113": 4,
    "MHO4CC2878": 5,
    "MHO4BB8": 6,
    "MH04CC2888": 7,
    "MH04CC1313": 8,
    "MH04CC2222": 9,
    "MH04C1201": 10,
    "MH04CC555": 11,
    "MH04C6565": 12,
    "MHO4A7": 13
}

# Function to park a car
def Park(plateNumber):
    if len(plateNumber) >= 6 and len(plateNumber) <= 12:
        position = len(parking) + 1
        parking[plateNumber] = position
        return f"CAR PARKED AT POSITION: {position}"
    else:
        return "INVALID INPUT"

# Function to search for a car
def Search(plateNumber):
    if plateNumber in parking:
        position = parking[plateNumber]
        return f"CAR POSITION: {position}"
    else:
        return "CAR DOES NOT EXISTS"

# Main program
print("INPUT VALUE:")
option = int(input("Enter 1 for car parking or 2 for car searching: "))
plateNumber = input("Enter the car plate number: ")

if option == 1:
    output = Park(plateNumber)
elif option == 2:
    output = Search(plateNumber)
else:
    output = "INVALID INPUT"

print("OUTPUT VALUE:")
print(output)
