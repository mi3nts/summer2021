# Daily Notes
## June 24, 2019
### Task 1: Disassembling Sensors
#### 1.1 Disassmebling the interior
 - Disconnect USBs and other wires
 - Unscrew the circuit boards from the sensor
 - Take out SD cards
 - Sort out parts into separate piles
#### 1.2 Disassembling exterior
 - Unscrew the lid of the sensor
 - Take out wires
 - Take apart the solar shields
 - Take out the circuit board and the wiresmega168 

## June 25, 2019
### Task 2: Set Up Arduino Environment
#### 2.1 Set up Arduino Development Envioronment
 - Go to the web development editor [here](https://www.arduino.cc/en/Main/Software) and create an account
 - Download the Arduino Create plugin [here](https://create.arduino.cc/getting-started/plugin?page=2)
#### 2.2 Do the first exercise
 - Write the following code in the editor:
````
/*
// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
   // print out a String of your choice 
  Serial.println("Hello MINTS: Multi-scale Integrated Sensing and Simulation");
  // Delay for 1000 miliseconds 
  delay(1000);        // delay in between reads for stability
    }
````
 - The serial monitor will now print "Hello MINTS: Multi-scale Integrated Sensing and Simulation" on loop
#### 2.3 Do another exercise
 - Change the code to:
 ````
 void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(500);                       // wait for a second
  digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
  delay(500);                       // wait for a second
}
````
 - The LED light now flashes every half second
 #### 2.4 Exercise 4
 - Try the following:
  ````
 // the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

// the loop routine runs over and over again forever:
void loop() {
  // Delay for 1000 miliseconds 
  if(random(1, 10) > 5)
    digitalWrite(LED_BUILTIN, LOW);
  else
    digitalWrite(LED_BUILTIN, HIGH);
  delay(200);
}
````
#### 2.5 Set up Desktop Arduino IDE
 - Download the desktop IDE [here](https://www.arduino.cc/en/Main/Software)
 - Make sure to pause the plugin downloaded earlier
 - Try out the exercises from before

#### 2.6 Set up Atom environment
 - Download Atom [here](https://atom.io/)
 - Download the PlatformIO package within Atom. Details [here](https://platformio.org/install/ide?install=atom)
 - Search up Seeed BME280 in Libraries in PlatformIO and install

### Task 3: Check the Sensors
#### 3.1 Connect hardware of the BME280 Sensor
 - Connect the Arduino to the board
 - Connect the barometer sensor to the Arduino
   - SCL wire goes to A5
   - SDA to A4
   - UCC to 5V
   - GND to the GND hole on the board
#### 3.2 Create the program
 - Write the following code: 
 ````
 /*Test of the BME280 sensor, displaying temp, humidity, altitude, and pressure*/

#include <Arduino.h>
#include "Seeed_BME280.h"
#include <Wire.h>

BME280 bme280;

void setup() {
  Serial.begin(9600);
  Serial.println("Began");
  if(!bme280.init()){
    Serial.println("Device error!");
  }
}

// the loop function runs over and over again forever
void loop() {
  float pressure;

  //get and print temperatures
  Serial.print("Temp: ");
  Serial.print(bme280.getTemperature());
  Serial.println("C");//The unit for  Celsius because original arduino don't support speical symbols

  //get and print atmospheric pressure data
  Serial.print("Pressure: ");
  Serial.print(pressure = bme280.getPressure());
  Serial.println("Pa");

  //get and print altitude data
  Serial.print("Altitude: ");
  Serial.print(bme280.calcAltitude(pressure));
  Serial.println("m");

  //get and print humidity data
  Serial.print("Humidity: ");
  Serial.print(bme280.getHumidity());
  Serial.println("%");

  delay(1000);

}
````
 - Watch the temperature, pressure, altitude, and humidity being displayed on the serial monitor
   - Temp: 26.22C
   - Pressure: 99034.00Pa
   - Altitude: 192.48m
   - Humidity: 51%
#### 3.3 Use the SCD30 CO2 Sensor
 - Connect the four wires from the arduino to the sensor
 - Install SparkFun_SCD30_Arduino_Library
 - Write the following code:
 ````
/*Test of the SCD30 sensor, displaying CO2, temperature, and humidity*/
#include <Arduino.h>
#include <Wire.h>
#include "SparkFun_SCD30_Arduino_Library.h"

SCD30 airSensor;

void setup()
{
  Wire.begin();

  Serial.begin(9600);
  Serial.println("SCD30 Example");

  airSensor.begin(); //This will cause readings to occur every two seconds
}

void loop()
{
  if (airSensor.dataAvailable())
  {
    Serial.print("co2(ppm):");
    Serial.print(airSensor.getCO2());

    Serial.print(" temp(C):");
    Serial.print(airSensor.getTemperature(), 1);

    Serial.print(" humidity(%):");
    Serial.print(airSensor.getHumidity(), 1);

    Serial.println();
  }
  else
    Serial.println("No data");

  delay(1000);
}
````
 - Temperature is around 26 degrees Celsius, humidity is 53.2%, which is relatively close to the measurements from the BME280 sensor
 - CO2 ppm seems to be oscillating from 600 to 1500
#### 3.4 Use the Sunlight Sensor
 - Connect the wires to the sensor
 - The library for this sensor is not in Atom
 - Type the following code:
````
#include "Arduino.h"
#include <Wire.h>
#include "SI114X.h"


SI114X SI1145 = SI114X();

void setup() {

  Serial.begin(9600);
  Serial.println("Beginning Si1145!");

  while (!SI1145.Begin()) {
    Serial.println("Si1145 is not ready!");
    delay(1000);
  }
  Serial.println("Si1145 is ready!");
}

void loop() {
  Serial.print("//--------------------------------------//\r\n");
  Serial.print("Vis: ");
  Serial.println(SI1145.ReadVisible());
  Serial.print("IR: ");
  Serial.println(SI1145.ReadIR());
  //the real UV value must be div 100 from the reg value , datasheet for more information.
  Serial.print("UV: ");
  Serial.println((float)SI1145.ReadUV()/100);
  delay(1000);
}
````
 - When exposed to the room's light, the sensor read:
   - Vis: 275
   - IR: 326
   - UV: 0.10
 - When covered, it read:
   - Vis: 259
   - IR: 253
   - UV: 0.01
#### 3.5 Use Light-Gesture-Color-Proximity Sensor
 - Connect the hardware
 - Download the library from [here](https://github.com/Seeed-Studio/Seeed_TMG3993)
 - Copy the folder with the library into the lib folder inside your project
 - Write the following code (found in the example from the library):
 ````
 #include <Arduino.h>
#include <Wire.h>
#include "Seeed_TMG3993.h"

TMG3993 tmg3993;

void setup()
{
  Serial.begin(9600);
  Serial.println("TMG3993 Proximity Example");

  Wire.begin();

  if (tmg3993.initialize() == false)
  {
    Serial.println("Device not found. Check wiring.");
    while (1);
  }
  tmg3993.setupRecommendedConfigForProximity();
  tmg3993.enableEngines(ENABLE_PON | ENABLE_PEN | ENABLE_PIEN);
}

void loop()
{
  if (tmg3993.getSTATUS() & STATUS_PVALID)
  {
    uint8_t proximity_raw = tmg3993.getProximityRaw();  //read the Proximity data will clear the status bit
    Serial.print("Proximity Raw: ");
    Serial.println(proximity_raw);
  }
  delay(1);
}
````
- Check that the output changes as you move your hand closer and further

### Task 4: Connect all sensors together in one program
#### 4.1 Connect hardware
 - Use wire bridges and some more boards to connect all of the sensors to the arduino
#### 4.2 Import necessary libraries
 - Import the seeed_TMG3993 and the MultichannelGasSensor libraries
 - Make sure you have installed all the necessary libraries for the other sensors
 - All of these libraries were refrenced earlie, with the exception of the MultichannelGasSensor library which can be found in this project.
#### 4.3 Create program
 - Type the following code, which will run all of the five sensors:
 ````
 #include <Arduino.h>
#include <Wire.h>

#include "Seeed_TMG3993.h"
#include "Seeed_BME280.h"
#include "SparkFun_SCD30_Arduino_Library.h"
#include "SI114X.h"
#include "MutichannelGasSensor.h"

TMG3993 tmg3993;
BME280 bme280;
SCD30 scd30;
SI114X SI1145 = SI114X();

void setup()
{
  Serial.begin(9600);
  Serial.println("TMG3993 Proximity Example");

  Wire.begin();

  //Initialize TMG3993 sensor
  if (tmg3993.initialize() == false)
  {
    Serial.println("Device not found. Check wiring.");
    while (1);
  }
  tmg3993.setupRecommendedConfigForProximity();
  tmg3993.enableEngines(ENABLE_PON | ENABLE_PEN | ENABLE_PIEN);

  //Initialize BME 280 sensor
  if(!bme280.init()){
     Serial.println("Device error!");
  }

  scd30.begin();

  //Initialize SI1145
  while (!SI1145.Begin()) {
    Serial.println("Si1145 is not ready!");
    delay(1000);
  }

  //Initialize MutichannelGasSensor
  gas.begin(0x04);//the default I2C address of the slave is 0x04
  gas.powerOn();

}

void trybme280(){
  //Get BME280 reading
  float pressure;

  //get and print temperatures
  Serial.print("Temp: ");
  Serial.print(bme280.getTemperature());
  Serial.println("C");//The unit for  Celsius because original arduino don't support speical symbols

  //get and print atmospheric pressure data
  Serial.print("Pressure: ");
  Serial.print(pressure = bme280.getPressure());
  Serial.println("Pa");

  //get and print altitude data
  Serial.print("Altitude: ");
  Serial.print(bme280.calcAltitude(pressure));
  Serial.println("m");

  //get and print humidity data
  Serial.print("Humidity: ");
  Serial.print(bme280.getHumidity());
  Serial.println("%");
}

void loop()
{
  //Get TMG3993 reading
  if (tmg3993.getSTATUS() & STATUS_PVALID)
  {
    uint8_t proximity_raw = tmg3993.getProximityRaw();  //read the Proximity data will clear the status bit
    Serial.print("Proximity Raw: ");
    Serial.println(proximity_raw);
  }

  Serial.println("_________________________");
  trybme280();
  Serial.println("_________________________");

  if (scd30.dataAvailable())
   {
     Serial.print("co2(ppm):");
     Serial.print(scd30.getCO2());

     Serial.print(" temp(C):");
     Serial.print(scd30.getTemperature(), 1);

     Serial.print(" humidity(%):");
     Serial.print(scd30.getHumidity(), 1);

     Serial.println();
   }
   else
     Serial.println("No data");

  Serial.println("_________________________");

  Serial.print("Vis: ");
  Serial.println(SI1145.ReadVisible());
  Serial.print("IR: ");
  Serial.println(SI1145.ReadIR());
  //the real UV value must be div 100 from the reg value , datasheet for more information.
  Serial.print("UV: ");
  Serial.println((float)SI1145.ReadUV()/100);
  Serial.println("_________________________");


  //Multichannel Gas Sensor Readings
  float c;

  c = gas.measure_NH3();
  Serial.print("The concentration of NH3 is ");
  if(c>=0) Serial.print(c);
  else Serial.print("invalid");
  Serial.println(" ppm");

  c = gas.measure_CO();
  Serial.print("The concentration of CO is ");
  if(c>=0) Serial.print(c);
  else Serial.print("invalid");
  Serial.println(" ppm");

  c = gas.measure_NO2();
  Serial.print("The concentration of NO2 is ");
  if(c>=0) Serial.print(c);
  else Serial.print("invalid");
  Serial.println(" ppm");

  c = gas.measure_C3H8();
  Serial.print("The concentration of C3H8 is ");
  if(c>=0) Serial.print(c);
  else Serial.print("invalid");
  Serial.println(" ppm");

  c = gas.measure_C4H10();
  Serial.print("The concentration of C4H10 is ");
  if(c>=0) Serial.print(c);
  else Serial.print("invalid");
  Serial.println(" ppm");

  c = gas.measure_CH4();
  Serial.print("The concentration of CH4 is ");
  if(c>=0) Serial.print(c);
  else Serial.print("invalid");
  Serial.println(" ppm");

  c = gas.measure_H2();
  Serial.print("The concentration of H2 is ");
  if(c>=0) Serial.print(c);
  else Serial.print("invalid");
  Serial.println(" ppm");

  c = gas.measure_C2H5OH();
  Serial.print("The concentration of C2H5OH is ");
  if(c>=0) Serial.print(c);
  else Serial.print("invalid");
  Serial.println(" ppm");
  Serial.println("_________________________");


  delay(1000);

  Serial.println();
  Serial.println();
  Serial.println();

}
````
 - Watch the output and check for correctness

## June 26, 2019 & July 2, 2019
### Task 5: Building Sensor
The follwoing procedures may have some errors or omissions
#### 5.1 Splitting wires
 - Take a four-wire cable and cut in the middle, and separate the four wires
 - Expose the ends of each wire
 - Hook the end of each wire and tie to combine with two more wires
 - Solder the wires together, to make each of the four wires split into two wires
 - Cover the exposed wire with heat shrink
#### 5.2 Prepare the two voltage sensors (one for the battery and one for the solar panel)
 - Attach a two-pin wire holder to each sensor and solder
 - For each of the sensor, attach four of the split wires into the designated holes (GND, VCC, SDA, SLC)
#### 5.3 Prepare the Sunny Buddy
 - Connect a two wire cable to the port on the Sunny Buddy
 - Connect the black wire from this cable to the "solar -" hole and solder. Solder another wire to its other side in order to extend it. Cover exposed wire with heat shrink.
#### 5.4 Connect Seeduino to voltage sensors
 - Connect a blue wire to the "solar +" hole on the Sunny Buddy
 - Connect this blue wire to the pin on the solar panel voltage sensor
 - Solder a bit of tin onto the address of the solar panel voltage sensor to change the address
 - Connect the red wire from the port on the Sunny Buddy to the battery sensor
#### 5.5 Finish up
 - Connect the four-wire cable to the main Seeduino
 - Connect one end of a two-wire cable to port of the Seeduino, and solder the other end to the load wire holes of the Sunny Buddy
 - Cover the Seeduino with a base shield

## July 8, 2019
### Task 6: Checking wire connections to sensors
#### 6.1 Connect wires to arduino
 - Connect the red wire to 5V
 - Black goes to GND
 - White tp D10
 - Blue to D11
 - Green to D12
 - Yellow wire to D13
 - Connect the wires to the sensor and connect the arduino to the computer with a USB cable
#### 6.2 Collect data
 - Type the following on the terminal: 
 ```` screen /dev/cu.usbserial-AH06AI47 ````
 - Check that the device provides the correct data. It should eventually print ```#mintsO!OPCN2>1:``` followed by some number, followed by a lot more data.
#### 6.3 Finish up
 - If wire collects data correctly, disconnect from the arduino and sensor, cover exposed wire with heat shrink, and heat. Then put aside.
 
### Task 7: Connect wires
 - Get 3 four-pin cable and one of the six-wire cables from task 6
 - Wrap all the red wires among these together and wrap with a copper solid wire around them. Do the same for the black wires.
 - Wrap all the yellow wires from the 4-pin cable together (DO NOT use the wire from the six-wire cable) and wrap with a solid wire. Do the same for the white wires.
 
## July 9, 2019
### Task 8: Assemble sensors
Mount a BME2800 sensor, a dust sensor, and a multichannel gas sensor, as well as two arduinos, on the sensor.

### Task 9: Write text input to CSV
Full python program can be found in this directory, named "SerialReader.python"
#### 9.1 Get input
 - Type ```` screen /dev/cu.usbserial-AH06AI47 ```` to get serial inputs and copy-paste some of the data to a text file.
#### 9.2 Process data
 - Process serial data, splitting the string at ````#mintsO!````, in order to make it easier to transfer to a python dictionary.
````
#Get data
file = open(r"Data.txt", "r") #Read file
contents = file.read()
#Process data
contents.replace("~", "") #Get rid of the ~ in the string
contents = contents.split("#mintsO!B") #Split the file into a list of strings for each iteration of data
del contents[0] # Get rid of empty first string
````
#### 9.3 Make dictionaries
 - Make one dictionary for each sensor and set to 0
 ````
 #Create a dictionary for each sensor's variables
BME280 = {"var1": 0, "var2": 0, "var3": 0, "var4": 0, "time": 0}
MGS001 = {"var1": 0, "var2": 0, "var3": 0, "var4": 0, "var5": 0, "var6": 0, "var7": 0, "var8": 0, "time": 0}
OPCN2 = {"var1": 0, "var2": 0, "var3": 0, "var4": 0, "var5": 0, "var6": 0, "var7": 0, "var8": 0, "var9": 0, "time": 0,
         "var10": 0, "var11": 0, "var12": 0, "var13": 0, "var14": 0, "var15": 0, "var16": 0, "var17": 0,
         "var18": 0, "var19": 0, "var20": 0, "var21": 0, "var22": 0, "var23": 0, "var24": 0, "var25": 0,
         "var26": 0, "var27": 0, "var28": 0, "time": 0}
SCD30 = {"var1": 0, "var2": 0, "var3": 0, "time": 0}
````
#### 9.4 Create a function to fill data into the dictionary
````
def fillDict(num, dict, data):
  curDat = [data[num].split(":")[0].split(">")[1]] +  data[num].split(":")[1:]
  for key, dat in zip(dict.keys(), curDat):
      dict[key] = dat
  dict["time"] = datetime.now()
````
#### 9.5 Create a function to make a csv file from each dictionary
````
def makeCSV(dict, fileName):
    makeHeader = not(os.path.isfile(fileName))
    keys = list(dict.keys())
    with open(fileName, "a") as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=keys);
        if(makeHeader):
            writer.writeheader()
            print()
        writer.writerow(dict)
    csvFile.close()
````
#### 9.6 Loop over each iteration of data and update csv files
````
for data in contents:
    #Split vars of into sensors
    data = data.split("~#mintsO!")

    #Put variables of each sensor into the list
    fillDict(0, BME280, data)
    fillDict(1, MGS001, data)
    fillDict(2, OPCN2, data)
    fillDict(3, SCD30, data)

    #Make the csv file for each sensor
    makeCSV(BME280, "BME280.csv", not(os.path.isfile("BME280.csv")))
    makeCSV(MGS001, "MGS001.csv", not(os.path.isfile("MGS001.csv")))
    makeCSV(OPCN2, "OPCN2.csv", not(os.path.isfile("OPCN2.csv")))
    makeCSV(SCD30, "SCD30.csv", not(os.path.isfile("SCD30.csv")))
````

## July 10, 2019
### Task 10: Read serial input and write to CSV
Full python program can be found in this directory, named "SerialReader.python", including changes from July 9th's program.
#### 10.1 Set up serial port
 - Connect USB from device to computer
 - Run ````screen /dev/cu.usbserial-AH06AI47```` to make sure device is properly connected.
 - Write ````ser = serial.Serial("/dev/cu.usbserial-A90837L7", 9600, timeout=5)```` in your python program to set up the serial.
#### 10.2 Read set-up data
 - This device prints 182 lines before it sets up. To run through them, add the following to your python code:
````
i = 0
while i < 182:
    print(i, (ser.readline()).decode('utf-8'))
    i = i + 1

print("SET UP COMPLETE\nREADING DATA")
````
#### 10.3 Read data
 - We will have to read data each time until '~' is reached. Write the following:
````
curData = ""
while True:
    char = (ser.read(1)).decode('utf-8')
    if(char == '~'):
        processData(curData)
        curData = ""
    else:
        curData = curData + str(char)
````
#### 10.4 Process data
- Write a function that processes the data and performs the commands to write it to the csv using functions from earlier:
````
def processData(data):
    print(data)
    data = data.split(">")
    if(data[0] == "#mintsO!BME280"):
        fillDict(BME280, data[1])
        makeCSV(BME280, "BME280.csv")
    if(data[0] == "#mintsO!MGS001"):
        fillDict(MGS001, data[1])
        makeCSV(MGS001, "MGS001.csv")
    if(data[0] == "#mintsO!SCD30"):
        fillDict(SCD30, data[1])
        makeCSV(SCD30, "SCD30.csv")
    if(data[0] == "#mintsO!OPCN2"):
        fillDict(OPCN2, data[1])
        makeCSV(OPCN2, "OPCN2.csv")
````
#### 10.5 Change time to utc-time
 - Change the `"time"` key in the dictionaries to `"utc-time"`
 - change the line in the ``fillDict`` function to read:
 ```  dict["utc-time"] = datetime.utcnow()```
#### 10.6 Implement try-ctach
 - Add a try catch in the loop where it reads by character, in case it cannot find a '~' or other problems.
 - Add a try catch in loop where it processes data as well, in case it gets stuck while processing.
#### 10.7 Move definitions to separate file
 - Create a new function called `getDirPath` in a separate definitions file:
 ````
 def getDirPath(time):
      dir = "MintsData/raw/" + str(macAddress) + "/" + str(time.year) + "/" + ('%02d' % time.month) + "/" + ('%02d' % time.day)
      return dir
````
 - Create a new functions called `getFilePath` in the definitions file:
 ````
 def getFilePath(time, dir, name):
    filePath = dir + "/" + "MINTS_" + macAddress + "_" + name + "_" + str(time.year) + "_" + ('%02d' % time.month) + "_" + ('%02d' % time.day) + ".csv"
    return filePath
````
 - Now instead of creating the file name and directory in the makeCSV function in serialReader, call these functions. This will make it easier to change file/directory names if necessary
#### 10.8 Put most recent measurements on a json file
 - Create a function called `jsonMaker` as follows:
 ````
 def jsonMaker(fileName, dict):
    with open(fileName, 'w') as f:
        json.dump(dict, f, default=str)
````
 - Call this function to update the json file each time after you update the dictionary, inside the `processData` function.
#### 10.9 Connecting to multiple ports
 - We must allow the computer to read data from multiple arsuinos simultaneously. In order to do this, we will need to run several programs at the same time. For reading from three arduinos, start by copy-pasting all of the code in the file you have created into two more files.
 -
#### Task 10 summary:
 - Each arduino is connected to multiple sensors; every "cycle", each sensor prints out its own data. Each arduino works (and runs) independnetly.
 - When the sensor prints out data, it starts with ````#mintsO!````, and then prints the sensor name, followed by `>` and then a series of numbers separated by `:`, which correspond to the data the sensor read. Each line ends in `~`
 - <b>Reading stage:</b> The program reads each character that the arduino sends and adds it into a string until `~` is reached, at which point the string is completed and sent to "processing"
 - <b>Processing stage:</b> The program separates each sensor's readout. Then, it puts the data from each sensor into a dictionary, where each value is put into its corresponding variable in order
 - <b>Recording stage:</b> After processing the sensor's reading, the program writes the data from the dictionary into a CSV file.
 - The program then cycles back to the reading stage to read the next sensor's input
#### Task 10: Set-up


## July 15-17
### Task 11: Assemble sensors
#### 11.1 Connect parts to the cylinder portion
 - Connect two arduinos to each board
 - Connect three sensors (BME280, SCD30, OPCN2, MGS001) to one arduino
 - Connect the fourth sensor (PPD42NSDuo) to the other arduino
 - Test the device on the code from task 10
 - Put the wind shields on the device
#### 11.2 Connect to sensor box
 - Connect the cylinder to the board of the sensor box
 - Put the cables through the box and screw lid
#### 11.3 Building interior sensors
 - Connect a GPS to each board with a CPU with fan and camera
 - Put an arduino base on each board
 - Connect a USB to the CPU
### Task 12: Set-up CV2
#### 12.1 Install CV2
 - Install the lastest version of cv2 <a href="https://opencv.org/releases/">here</a>
 - Check that it is working correctly by typing
 ````
 import cv2
 print(cv2.__version__)
 ````
#### 12.2 Open an image using cv2
 - Type the following program:
````
import numpy as np
import cv2

img = cv2.imread('image.jpg') #Change the address of this image to any image you are using
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
````
 - The image should open when you run the program. To close it, type 0 in the image window.
#### 12.3 Get features from an image to use in machine learning
 - Complete necessary imports
````
import numpy as np
import cv2
import sys
import csv
from skimage import io, color
````
 - Load the image
````
img = cv2.imread('startrails.jpg')
````
 - Get the RGB value of all pixels in the image in a column
````
# Get RGB data
inputImage_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
Image_Array_RGB = np.array(inputImage_RGB)
Image_Shape = Image_Array_RGB.shape

One_D_Image_Red   = np.transpose(np.matrix(Image_Array_RGB[:, :, 0].ravel()))
One_D_Image_Green = np.transpose(np.matrix(Image_Array_RGB[:, :, 1].ravel()))
One_D_Image_Blue  = np.transpose(np.matrix(Image_Array_RGB[:, :, 2].ravel()))


One_D_Image_RGB = np.concatenate((One_D_Image_Red, One_D_Image_Green, One_D_Image_Blue), axis=1)
````
 - Do the same to get the HSV values
````
# Get HSV data
inputImage_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
Image_Array_HSV = np.array(inputImage_HSV)

One_D_Image_Hue   = np.transpose(np.matrix(Image_Array_HSV[:, :, 0].ravel()))
One_D_Image_Saturation   = np.transpose(np.matrix(Image_Array_HSV[:, :, 1].ravel()))
One_D_Image_Value   = np.transpose(np.matrix(Image_Array_HSV[:, :, 2].ravel()))

One_D_Image_HSV = np.concatenate((One_D_Image_Hue, One_D_Image_Saturation, One_D_Image_Value), axis=1)
````
 - cv2 cannot convert to LAB values; instead, use the color package from skimage
````
# Get LAB Data
inputImage_LAB = color.rgb2lab(io.imread('startrails.jpg'))
Image_Array_LAB = np.array(inputImage_LAB)

One_D_Image_L   = np.transpose(np.matrix(Image_Array_LAB[:, :, 0].ravel()))
One_D_Image_A   = np.transpose(np.matrix(Image_Array_LAB[:, :, 1].ravel()))
One_D_Image_B   = np.transpose(np.matrix(Image_Array_LAB[:, :, 2].ravel()))

One_D_Image_LAB = np.concatenate((One_D_Image_L, One_D_Image_A, One_D_Image_B), axis=1)
````
 - Join all matrices together to a new matrix:
````
One_D_Image = np.concatenate((One_D_Image_RGB, One_D_Image_HSV, One_D_Image_LAB), axis=1)
````
- This matrix contains all of the features that we will later train the algorithm on
- Write the matrix to a csv
````
with open("colors.csv", "a") as csvFile:
    np.savetxt("colors.csv", One_D_Image, delimiter=",", header="Red, Green, Blue, Hue, Saturation, Color, Lightness, A*, B*", fmt='%3.f')
````

## July 22-23, 2019
### Task 13: Assemble and put small sensors in housing
#### 13.1 Set the cable
 - Take a big 8-wire cable
 - Cut both ends to expose wires
 - Cut down the white-orange and white-brown wires, to leave 6 wires on both ends.
 - Put the wire through the box with all the arduinos and put the knob on to lock it in.
#### 13.2 Shield side
 - Put the top of the housing through the wire
 - Connect three I2C cables together, twisting together like colors
 - Take a Shinyei cable (5-pin connector with three wires, red, black, yellow) and connect a black wire to both the spots the are missing wire
 - Connect a resitor to the black wire on one end of the connector; connect the other end to the black wire at the other side of the resistor. Connect another wire to the resistor to extend. Solder together and cover with heat shrink.
 - Twist the black wire with the resistor into the black wires from the I2C. Solder all of this into the brown wire in the cable
 - Twist the red wire from the Shinyei into the red wires from the I2C. Solder all of this into the orange wire in the cable
 - Connect all the white wires from the I2C that had been twisted together to the white-green wire in the cable. Solder and apply heat shrink.
 - Connect all the yellow wires from the I2C that had been twisted together to the green wire in the cable. Solder and apply heat shrink.
 - Connect the yellow wire from the Shinyei to the blue wire in the cable. Solder and put heat shrink.
 - Connect the black wire left on the Shinyei to the white-blue wire in the cable
 - Connect sensors (CO2, BME280, and multichannel gas) to all the 4-pin ocnnectors, and connect the Shinyei to the Shinyei cable.
 - Put all of this through the housing and connect to the top of the housing.
#### 13.3 Box Side
 - Get two 4-pin connector (I2C). For one of them, cut all wires but the yellow one; this will be the D7 connector, and the unaltered one will be the I2C.
 - Get another 4-pin connector that only has 3 wires (black, red, yellow). This will be the D8 connector.
 - Twist the red wires of the I2C and D8 together and solder to the orange wire of the 6-wire cable.
 - Twist the black wires of the I2C and D8 together and solder to the brown wire of the 6-wire cable.
 - Solder the yellow wire of the D8 to the blue wire of the 6-wire cable.
 - Solder the white wire of the I2C to the white-green wire of the 6-wire cable.
 - Solder the yellow wire of the I2c to the green wire of the 6-wire cable.
 - Solder the yellow wire of the D7 to the blue-white wire of the 6-wire cable.
 - Connect the D7, D8, and I2C to their respective spots on the Arduino shield in the box. Put on the lead.

## August 5, 2019
### Task 14: Prepare the bigger sensors
#### 14.1 Connect sensors to the stand
 - Connect BME280, Shinyei, multichannel gas sensor, and CO2 sensors to their respective places, and screw into place.
#### 14.2 Prepare Shinyei cable
 - Take the Shinyei five-pin connector with three wires. 
 - Connect black wires to the empty spots.
 - Solder the two black wires on either side of the 5-pin connector to the one resistor, and extend with an extra wire. Cover with heat shrink.

## August 6, 2019
### Task 15: Create a big chessboard pattern
 - Use metallic tape to create a chessboard pattern on a big piece of foam. This will be used to calibrate the sensor on the thermal camera.
### Task 16: Read data from a model15 sensor
#### 16.1 Change previously written code to read new data format
 - Copy code from sensorReader.py to otherSensorReader.py and update necessary changes
 - Change from separating data by `:` to separating by `,`
 - Read by line instead of by character
 - Etc.
#### 16.2 Write script to access menu of the sensor

## August 9, 2019
### Task 17: Use Machine Learning to Predict Sensor Data
 - Create a linear regressor, neural network, and random forest algorithm predictor for each of a wine quality dataset, and a data set consisting of data from grimms and LoRa sensors, where the LoRa data is used to predict corresponding grimms data.
 - Used sklearn library for all machiine learning algorithms
 - Used pandas to handle datasets
 - See code on documents wine.py and calibrate.py
