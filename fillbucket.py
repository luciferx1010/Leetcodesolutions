import math

def fill_bucket(bucket_capacity, mug_capacities, water_in_mugs):
    min_mugs = math.ceil(bucket_capacity / max(mug_capacities))
    total_water = 0
    mug_count = 0

    for i, water in enumerate(water_in_mugs):
        total_water += water
        mug_count += 1

        if total_water > 0.8 * bucket_capacity:
            return "BUCKET FULL!\nNUMBER OF MUGS: " + str(mug_count)
    
    return "Bucket not filled to 80%"

# Example usage
bucket_capacity = int(input("Enter bucket capacity in litres: "))
mug_capacities = []
water_in_mugs = []

print("Enter mug capacities:")
while True:
    capacity = input()
    if capacity == "":
        break
    mug_capacities.append(int(capacity))

print("Enter amount of water in each mug:")
while True:
    water = input()
    if water == "":
        break
    water_in_mugs.append(int(water))

output = fill_bucket(bucket_capacity, mug_capacities, water_in_mugs)
print(output)
