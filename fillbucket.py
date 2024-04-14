import math

def fill_bucket(bucket_capacity, mug_capacity, water_in_mugs):
    min_mugs = math.ceil(bucket_capacity / mug_capacity)
    total_water = 0
    mug_count = 0

    for water in water_in_mugs:
        total_water += water
        mug_count += 1

        if total_water > 0.8 * bucket_capacity:
            return "BUCKET FULL!\nNUMBER OF MUGS: " + str(mug_count)
    
    return "Bucket not filled to 80%"

# Example usage
bucket_capacity = int(input("Enter bucket capacity in litres: "))
mug_capacity = int(input("Enter mug capacity in litres: "))
water_in_mugs = []

print("Enter amount of water in each mug:")
while True:
    water = input()
    if water == "":
        break
    water_in_mugs.append(int(water))

output = fill_bucket(bucket_capacity, mug_capacity, water_in_mugs)
print(output)
