# ASSIGNMENT-3 RASPI REPORT

<h3>Team Members: </h3>
Mohammed Wasim Shaik - SE20UARI098 - wasim20uari098@mahindrauniversity.edu.in <br>
Sai Arun Vakacherla - SE20UARI131 - arun20uari131@mahindrauniversity.edu.in <br>
Sujith Sai Kalakonda - SE20UARI151 - sujith20uari151@mahindrauniversity.edu.in <br>
Mudunuri Naga Sathya Prasad Raju - SE20UARI100 - nagasathya20uari100@mahindrauniversity.edu.in <br>
<br>

<h3>Title: Data Acquisition from DHT11 Sensor on Raspberry Pi</h3> 

<h3>Introduction:</h3>
In this project, we used a Raspberry Pi to acquire data from a DHT11 digital sensor to monitor temperature and humidity levels. The DHT11 sensor is a commonly used sensor for environmental monitoring applications.
<br>

<h3>Sensor Description:</h3>
The DHT11 sensor is a low-cost digital sensor capable of measuring temperature and humidity. It communicates with the Raspberry Pi through a single data pin, making it relatively simple to interface with. The DHT11 sensor typically uses three pins (VCC, GND, and DATA) to interface with the Raspberry Pi. The sensor provides data in a digital format, which can be easily read and processed by the Raspberry Pi. <br>
<br>
<br>

DHT11 Temperature and Humidity Sensor Module for Arduino Raspberry Pi: <br>
<br>
![image](https://github.com/sujithsai-kalakonda/se20uari151_assign3_RasPi/assets/108214819/2f7191a6-6e28-4bed-a167-284fdeb52383) <br>
<br>

Raspberry Pi: <br>
<br>
![image](https://github.com/sujithsai-kalakonda/se20uari151_assign3_RasPi/assets/108214819/d93004f0-623a-4fb0-bcbe-dbb0ccb8b5d9) <br>
<br>

<h3>Use Case:</h3>
For this project, we monitored environmental conditions, specifically temperature and humidity, using the DHT11 sensor. Our experiment aimed to observe how changes in physical pressure on the sensor affected its readings. We first connected the DHT11's 3 pins to the following pins on the Raspberry Pi: <br>
1. 3V3 Power <br>
2. Ground <br>
3. GPIO 23 <br>
<br>

Here are the observed values during the experiment: <br>
1. Initially, after starting the program, the humidity and temperature values were 69% and 28°C, respectively. <br>
2. When gently holding the sensor, the humidity increased to 70%, while the temperature remained the same at 28°C. <br>
3. Applying slightly more pressure to the sensor caused both the humidity and temperature values to increase, reaching 74% humidity and 32°C temperature. <br>

**Status:**

| Humidity | Temperature |
|----------|-------------|
| 69       | 28          |
| 69       | 28          |
| 69       | 28          |
| 69       | 28          |
| 70       | 28          |
| 70       | 28          |
| 71       | 28          |
| 71       | 28          |
| 71       | 28          |
| 72       | 29          |
| 72       | 29          |
| 71       | 30          |
| 71       | 30          |
| 71       | 30          |
| 72       | 31          |
| 72       | 31          |
| 73       | 31          |
| 73       | 32          |
| 73       | 32          |
| 73       | 32          |
| 74       | 32          |

These observations highlight the sensitivity of the DHT11 sensor to physical pressure, which could be relevant in scenarios where environmental conditions need to be monitored under varying physical conditions, such as in a weather station or greenhouse. <br>
<br>

<h3>Python Code Explanation:</h3>
We used the Adafruit_DHT library to interface with the DHT11 sensor and Firebase to store the acquired data. Here's a breakdown of the key parts of the code: <br>
1. Libraries Imported: Adafruit_DHT for sensor communication, pyrebase for Firebase integration. <br>
2. We configure Firebase with your API key, authentication domain, database URL, and storage bucket. <br>
3. The main loop continuously reads temperature and humidity values from the DHT11 sensor using Adafruit_DHT.read_retry(). <br>
4. If valid sensor readings are obtained, the data is printed and then pushed to Firebase for storage. <br>
5. If there is an issue with reading the sensor, an error message is displayed. <br>
6. The program runs in an infinite loop with a 1-second delay between readings. <br>
<br>

<h3>Conclusion:</h3>
This project demonstrates how to use a Raspberry Pi and a DHT11 sensor to monitor temperature and humidity levels. We observed that physical pressure on the sensor affected the readings, which could be useful in certain environmental monitoring scenarios.
