#1
Inventory = { "Tomatoes": {"stock": 150, "price_per_unit": 5.0}, "Onions": {"stock": 80, "price_per_unit": 3.5}, "Garden Eggs": {"stock": 200, "price_per_unit": 1.0}}

transactions = 0

while True:
    item = input("Enter item name to purchase (Tomatoes, Onions, Garden Eggs) or exit: ")

    if item == "exit":
        print("Closing sales. Total transactions completed:", transactions)
        break

    if item not in Inventory:
        print("Item not found in stock. Check spelling.")
        continue

    quantity = int(input("Enter quantity to buy: "))

    if quantity > Inventory[item]["stock"]:
        print(f"Sorry, only {Inventory[item]['stock']} units of {item} remaining.")
    else:
        cost = quantity * Inventory[item]["price_per_unit"]
        Inventory[item]["stock"] -= quantity
        transactions += 1
        print(f"Sale successful! Cost: GHS {round(cost, 2)}. "
              f"{Inventory[item]['stock']} units of {item} remaining.")




#2

SERVICE_CHARGE = 15.00

consumption = int(input("Enter Total water consumption for the month (in cubic meters): "))



if consumption <= 15:
    consumption_cost = consumption * 0.90
elif consumption <= 30:
    consumption_cost = (15 * 0.90) + ((consumption - 15) * 1.20)
else:
    consumption_cost = (15 * 0.90) + (15 * 1.20) + ((consumption - 30) * 1.80)

total_bill = SERVICE_CHARGE + consumption_cost

print("\n--- Monthly Water Bill Summary ---")
print(f"Consumption: {consumption} m3")
print("Service Charge: GHS 15.00")
print(f"Consumption Cost: GHS {round(consumption_cost, 2)}")
print(f"Total Bill: GHS {round(total_bill, 2)}")








#3
recorded_speeds = [95, 110, 100, 85, 125, 90, 105, 115, 70, 130, 99, 101, 88]
SPEED_LIMIT = 100

speeding_violations = []
total_speed = 0

for speed in recorded_speeds:
    total_speed += speed
    if speed > SPEED_LIMIT:
        print(f"WARNING: Vehicle recorded at {speed} km/h. "
              f"Exceeded limit of {SPEED_LIMIT} km/h.")
        speeding_violations.append(speed)

total_vehicles = len(recorded_speeds)
total_violations = len(speeding_violations)
percentage_speeding = (total_violations / total_vehicles) * 100
average_speed = total_speed / total_vehicles

print("\n--- Speed Analysis Summary ---")
print("Total vehicles recorded:", total_vehicles)
print("Total speeding violations:", total_violations)
print(f"Percentage speeding: {round(percentage_speeding, 2)}%")
print(f"Average speed: {round(average_speed, 2)} km/h")

# Slicing for targeted analysis
focused_segment = recorded_speeds[2:8]
print("Speeds for focused inspection segment (3rd to 8th vehicle):", focused_segment)



recorded_speeds = [95, 110, 100, 85, 125, 90, 105, 115, 70, 130, 99, 101, 88]
SPEED_LIMIT = 100

speeding_violations = []
total_speed = 0

for speed in recorded_speeds:
    total_speed += speed
    if speed > SPEED_LIMIT:
        print(f"WARNING: Vehicle recorded at {speed} km/h. "
              f"Exceeded limit of {SPEED_LIMIT} km/h.")
        speeding_violations.append(speed)

total_vehicles = len(recorded_speeds)
total_violations = len(speeding_violations)
percentage_speeding = (total_violations / total_vehicles) * 100
average_speed = total_speed / total_vehicles

print("\n--- Speed Analysis Summary ---")
print("Total vehicles recorded:", total_vehicles)
print("Total speeding violations:", total_violations)
print(f"Percentage speeding: {round(percentage_speeding, 2)}%")
print(f"Average speed: {round(average_speed, 2)} km/h")

# Slicing for targeted analysis
focused_segment = recorded_speeds[2:8]
print("Speeds for focused inspection segment (3rd to 8th vehicle):", focused_segment)