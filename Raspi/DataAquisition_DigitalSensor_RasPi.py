import Adafruit_DHT # Library for interfacing with the DHT11 sensor
import time
import pyrebase # Library for Firebase integration

# Firebase configuration
config = {
    "apiKey": "your_api_key",
    "authDomain": "your_auth_domain",
    "databaseURL": "your_database_url",
    "storageBucket": "your_dbProject_name.appspot.com"}

# Initialize Firebase
firebase = pyrebase.initialize_app(config)

# Initialize the Firebase database
db = firebase.database()

# Define the sensor type (DHT11)
sensor = Adafruit_DHT.DHT11

# Define the GPIO pin to which the sensor is connected (pin 23)
pin = 23

# Start an infinite loop to continuously acquire and send sensor data
while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    # Check if valid sensor readings were obtained
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
        data = {"Temperature" : temperature, "Humidity" : humidity}

        # Push the data to the Firebase database under the "Status" node
        db.child("Status").push(data)

        # Update the data in Firebase (overwrite the previous data)
        db.update(data)
        print("Sent to Firebase")
    else:
        print('Failed to get reading. Try again!')
      
    time.sleep(1) # Wait for 1 second before the next sensor reading
