# ASSIGNMENT-3 RASPI REPORT

Team Members:
Kuldeep Daram - SE20UARI083 - kuldeep20uari083@mahindrauniversity.edu.in
Mohammed Wasim Shaik - SE20UARI098 - wasim20uari098@mahindrauniversity.edu.in
Sai Arun Vakacherla - SE20UARI131 - arun20uari131@mahindrauniversity.edu.in
Sujith Sai Kalakonda - SE20UARI151 - sujith20uari151@mahindrauniversity.edu.in 

Title: Data Acquisition from DHT11 Sensor on Raspberry Pi

Introduction:
In this project, we used a Raspberry Pi to acquire data from a DHT11 digital sensor to monitor temperature and humidity levels. The DHT11 sensor is a commonly used sensor for environmental monitoring applications.

Sensor Description:
The DHT11 sensor is a low-cost digital sensor capable of measuring temperature and humidity. It communicates with the Raspberry Pi through a single data pin, making it relatively simple to interface with. The sensor provides data in a digital format, which can be easily read and processed by the Raspberry Pi.

DHT11 Temperature and Humidity Sensor Module for Arduino Raspberry Pi
![image](https://github.com/sujithsai-kalakonda/se20uari151_assign3_RasPi/assets/108214819/2f7191a6-6e28-4bed-a167-284fdeb52383)

Use Case:
For this project, we monitored environmental conditions, specifically temperature and humidity, using the DHT11 sensor. Our use case involved observing how changes in physical pressure on the sensor affected its readings. Here are the observed values during the experiment:
1. Initially, after starting the program, the humidity and temperature values were 69% and 28°C, respectively.
2. When gently holding the sensor, the humidity increased to 70%, while the temperature remained the same at 28°C.
3. Applying slightly more pressure to the sensor caused both the humidity and temperature values to increase, reaching 74% humidity and 32°C temperature.
These observations highlight the sensitivity of the DHT11 sensor to physical pressure, which could be relevant in scenarios where environmental conditions need to be monitored under varying physical conditions, such as in a weather station or greenhouse.

Python Code Explanation:
We used the Adafruit_DHT library to interface with the DHT11 sensor and Firebase to store the acquired data. Here's a breakdown of the key parts of the code:
1. Libraries Imported: Adafruit_DHT for sensor communication, pyrebase for Firebase integration.
2. We configure Firebase with your API key, authentication domain, database URL, and storage bucket.
3. The main loop continuously reads temperature and humidity values from the DHT11 sensor using Adafruit_DHT.read_retry().
4. If valid sensor readings are obtained, the data is printed and then pushed to Firebase for storage.
5. f there is an issue with reading the sensor, an error message is displayed.
6. The program runs in an infinite loop with a 1-second delay between readings.

Conclusion:
This project demonstrates how to use a Raspberry Pi and a DHT11 sensor to monitor temperature and humidity levels. We observed that physical pressure on the sensor affected the readings, which could be useful in certain environmental monitoring scenarios.
