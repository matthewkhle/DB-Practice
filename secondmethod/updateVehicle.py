import json
from vehicleDataFormat import *
from datetime import datetime


# Create vehicle dictionary from vehicleDataFormat.py
vehicleEntry = vehicleDataFormat.dataFormat()


# updateStage(time, newestStage)

# TODO: finish method for time & general stage (logic is in testing.py)

now = datetime.now()

class updateStage():

    def checkTime(newTime, newStage):
        # #### Used for resetting updateStage.json ###########################
        # # The default time and stage will be 12 AM and 0 
        # oldTime = now.replace(hour=0, minute=0, second=0, microsecond=0)
        # generalStage = 0

        # # Dictionary format to be saved to JSON File 
        # stageFormat = {
        #     "time": str(oldTime),
        #     "general_stage": generalStage
        # }

        # # Writing dictionary into updateStage.json 
        # jsonFile = open("updateStage.json", "w")
        # json.dump(stageFormat, jsonFile)
        # jsonFile.close()
        # ####################################################################

        # Open the updateStage.json and load it 
        jsonFile = open("updateStage.json")
        dataValue = json.load(jsonFile)

        # Declare variable for the stored time and convert from string to time data type
        jsonValue = dataValue['time']
        jsonTime = datetime.strptime(jsonValue, '%Y-%m-%d %H:%M:%S')
        oldTime = jsonTime.time()

        newTime = datetime.strptime(newTime, '%Y-%m-%d %H:%M:%S')

        # Check if newTime is greater and update the JSON File
        if (newTime.time() > oldTime):

            # Dictionary format for the new time and stage
            stageFormat = {
            "time": str(newTime),
            "general_stage": newStage
            }

            # Write the dictionary to the JSON File
            jsonFile = open("updateStage.json", "w")
            json.dump(stageFormat, jsonFile)
            jsonFile.close()

class updateVehicle():

    # TODO: add the methods for all datapoints
    
    # Methods to save the new datapoints into the vehicle dictionary
    def newAltitude(altitude):
        vehicleDataFormat.setAltitude(vehicleEntry, altitude)
        return vehicleEntry 

    # Altitude color
    def newAltitudeColor(altitudeColor):
        vehicleDataFormat.setAltitudeColor(vehicleEntry, altitudeColor)
        return vehicleEntry 

    def newBattery(battery):
        vehicleDataFormat.setBattery(vehicleEntry, battery)
        return vehicleEntry
        
    # Battery color 
    def newBatteryColor(batteryColor):
        vehicleDataFormat.setBatteryColor(vehicleEntry, batteryColor)
        return vehicleEntry

    def newCurrentStage(stage):
        vehicleDataFormat.setCurrentStage(vehicleEntry, stage)
        return vehicleEntry 

    def newGeofenceCompilant(isCompilant):
        vehicleDataFormat.setGeofenceCompliant(vehicleEntry, isCompilant)
        return vehicleEntry 

    # Geofence Color

    def newLatitude(latitude):
        vehicleDataFormat.setLatitude(vehicleEntry, latitude)
        return vehicleEntry 

    def newLongitude(longitude):
        vehicleDataFormat.setLongitude(vehicleEntry, longitude)
        return vehicleEntry 

    def newPitch(pitch):
        vehicleDataFormat.setPitch(vehicleEntry, pitch)
        return vehicleEntry 

    # Pitch color

    def newPropulsion(propulsion):
        vehicleDataFormat.setPropulsion(vehicleEntry, propulsion)
        return vehicleEntry 
    
    # Propulsion Color

    def newRoll(roll):
        vehicleDataFormat.setRoll(vehicleEntry, roll)
        return vehicleEntry 
    
    # Roll Color

    def newSensorsOk(sensorOk):
        vehicleDataFormat.setSensorsOk(vehicleEntry, sensorOk)
        return vehicleEntry 

    def newSpeed(speed):
        vehicleDataFormat.setSpeed(vehicleEntry, speed)
        return vehicleEntry

    def newStageCompleted(stageComplete):
        vehicleDataFormat.setStageCompleted(vehicleEntry, stageComplete)
        return vehicleEntry

    def newStatus(status):
        vehicleDataFormat.setStatus(vehicleEntry, status)
        return vehicleEntry
    
    def newYaw(yaw):
        vehicleDataFormat.setYaw(vehicleEntry, yaw)
        return vehicleEntry

    def newTimeSinceLastPacket(timeSinceLastPacket):
        vehicleDataFormat.setTimeSinceLastPacket(vehicleEntry, timeSinceLastPacket)
        return vehicleEntry

    def newLastPacketTime(lastPacketTime):
        vehicleDataFormat.setLastPacketTime(vehicleEntry, lastPacketTime)
        return vehicleEntry

    def newTime(time):
        vehicleDataFormat.setTime(vehicleEntry, time)
        return vehicleEntry

# # For testing 
# newestPacketTime = now.replace(hour=8, minute=6, second=0, microsecond=0)
# updateStage.checkTime(newestPacketTime, 4)