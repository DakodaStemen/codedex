from math import radians, sin, cos, sqrt, atan2

# === Haversine Formula ===
# Used to calculate the great-circle distance between two points on the Earth's surface
def haversine(coord1, coord2):
    R = 6371.0  # Earth's radius in kilometers

    # Convert decimal degrees to radians (Trig Conversion)
    # Formula: radians = degrees × (π / 180)
    lat1, lon1 = map(radians, coord1)
    lat2, lon2 = map(radians, coord2)

    # Δlat and Δlon: Difference in latitude and longitude
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine formula:
    # a = sin²(Δlat / 2) + cos(lat1) × cos(lat2) × sin²(Δlon / 2)
    # c = 2 × atan2(√a, √(1−a))
    # distance = R × c
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c  # Final distance in kilometers

# === Your Location ===
my_location = (34.144260, -118.001945)     # Monrovia

# === Friend Locations ===
friend1 = (34.052235, -118.243683)         # Los Angeles
friend2 = (35.689487, 139.691711)          # Tokyo
friend3 = (40.712776, -74.005974)          # New York City

# Print each friend’s coordinates
print("Friend 1 (Los Angeles):", friend1)
print("Friend 2 (Tokyo):", friend2)
print("Friend 3 (New York City):", friend3)

# Store friends in a dictionary
friends = {
    "Friend 1 (Los Angeles)": friend1,
    "Friend 2 (Tokyo)": friend2,
    "Friend 3 (New York City)": friend3
}

# === Calculate distances using the Haversine formula ===
distances = {name: haversine(my_location, coord) for name, coord in friends.items()}

# === Find the friend with the max distance ===
furthest_friend = max(distances, key=distances.get)
furthest_distance = distances[furthest_friend]

print(f"\nThe friend furthest from you is {furthest_friend}, approximately {furthest_distance:.2f} km away.")
