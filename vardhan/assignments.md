# Assignments 
## June 2nd 2021
- Get familiar with MQTT with Python 
- Create both a subsciber and a publisher on your own computer (Publish random data say speed of a vehicle)
- Graph the data using the subscriber code (Can use matplotlib or any other means) 

## June 7th 2021
- Create mock publisher data for multiple sensors with one Node ID. The node ID on  our systems is the mac Adress of the small PC we have on each node. In your case it would be the mac address of your pc. Having said that you cant hard code or justtype it in. The code should be smart enough to figure it on its own. 
- When publishing data, the json string which lets say wheatherSensor should be under the topic NODEID/wheatherSensor and it should have the following attributes.
     - Datetime in UTC 
     - Temperature 
     - Humidity
     - Pressure 
     - Altitude

- Create two more sensors(speedometor, rainsensor) in a similar manner.





