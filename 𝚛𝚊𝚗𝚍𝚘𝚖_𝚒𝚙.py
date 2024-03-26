import random
import multitasking
from geopy.geocoders import Nominatim
import geocoder

def get_location_from_ip(ip_address):
    """
    Get location information based on an IP address.
    """
    try:
        # Use geocoder library to get location information
        location = geocoder.ip(ip_address)
        return location.json  # Returns a dictionary containing location details
    except Exception as e:
        return f"Error: {e}"



def gen_random_ip():
     # 122.161.74.115
    return f"{random.randint(0,255)}.{random.randint(161,161)}.{random.randint(0,255)}.{random.randint(0,255)}"

def get_location(latitude, longitude):
  """
  Get location information based on latitude and longitude coordinates.
  """
  # Initialize geocoder
  geolocator = Nominatim(user_agent="geo_locator")

  # Combine latitude and longitude into a string format
  coordinates = f"{latitude}, {longitude}"

  # Try to get location information
  try:
      location = geolocator.reverse(coordinates)
      return location.address
  except Exception as e:
      return 0

@multitasking.task 
def main():
   latitude = None  # Default value
   isnone = 0
   while True:
     

      ip_address = gen_random_ip()# Replace this with the actual IP address

      location_info = get_location_from_ip(ip_address)

      try:
          latitude = location_info['lat']
          IP = location_info['ip']
      except KeyError as e:
          continue
      except Exception as e:
          continue

      try:
       longitude = int(location_info['lng'])
      except KeyError as e:
          continue
      except Exception as e:
          continue


      location_info = get_location(int(latitude), int(longitude))

      if(location_info!=0):
        print('IP Adress',IP)
        print("Location:", location_info,"\n")
        
        with open('ipADRESS.txt',"a") as file:
          file.write(f"IP ADDRESS: {IP} \n")
          file.write(f"LOCATION INFO: {location_info} \n")
          file.write("\n")
          file.close()
          

        
if __name__ == "__main__":
  
  while True:
    main()
  
    



# <--------------------------RANDOM PLACES----------------------------->
# def generate_random_coordinates():
#     """
#     Generate random coordinates.
#     """
#     # Assuming coordinates are within a certain range
#     latitude = random.uniform(-90, 90)
#     longitude = random.uniform(-180, 180)
#     return latitude, longitude

# def get_location(latitude, longitude):
#   """
#   Get location information based on latitude and longitude coordinates.
#   """
#   # Initialize geocoder
#   geolocator = Nominatim(user_agent="geo_locator")

#   # Combine latitude and longitude into a string format
#   coordinates = f"{latitude}, {longitude}"

#   # Try to get location information
#   try:
#       location = geolocator.reverse(coordinates)
#       return location.address
#   except Exception as e:
#       return 0


# def main():
#     """
#     Main function to continuously generate and print random coordinates.
#     """
#     while True:
#         latitude, longitude = generate_random_coordinates()
#         location_info = get_location(latitude, longitude)

#         if location_info ==0:
#           continue
#         print(location_info)
#         time.sleep(0.01)  # Wait for 1 second

# if __name__ == "__main__":
#     main()

