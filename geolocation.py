# import geocoder


# def get_my_coordinates():
#     g = geocoder.ip("me")  # 'me' fetches your device's IP-based location
#     if g.ok:
#         return g.latlng
#     else:
#         return None


# # Example usage
# coordinates = get_my_coordinates()

# if coordinates:
#     print(f"My current coordinates are: {coordinates}")
# else:
#     print("Could not determine location.")

import requests


def get_my_coordinates():
    response = requests.get("https://ipinfo.io")
    data = response.json()
    location = data["loc"].split(",")
    return float(location[0]), float(location[1])


# Example usage
coordinates = get_my_coordinates()

if coordinates:
    print(f"My current coordinates are: {coordinates}")
else:
    print("Could not determine location.")
