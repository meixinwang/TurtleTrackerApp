# -*- coding: utf-8 -*-
#-------------------------------------------------------------
# ARGOSTrackingTool.py
# 
# Description: Reads in an ARGOS tracking data file and 
# allows the user to view the location of the turtle
# for a specified date entered via user input.

# Author: Meixin Wang (meixin.wang@duke.edu)
# Date: Fall 2022
#--------------------------------------------------------------

# Ask the user for a date, specifying the format
user_date = input("Enter a date (M/D/YYYY):")

# Create a variable pointing to the data file
file_name = 'data/raw/Sara.txt'

# Create a file object from the file
file_object = open(file_name,'r')

# Read contents of file into a list
lineList = file_object.readlines()
file_object.close()

# Create empty dictionaries for date and location data, key recordID
date_dict = {}
location_dict = {}

# Extract one data line into a variable
for lineString in lineList:
    
    # Check to see if the line is a data line
    if lineString[0] in ("#", "u"):
        continue
    
    # Split the string into a list of data items
    lineData = lineString.split()
    
    # Extract items in list into variables
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7]
    
    if obs_lc in ("1", "2", "3"):
    
        #Print the location of sara
        #print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")
        
        date_dict[record_id] = obs_date
        location_dict[record_id] = (obs_lat, obs_lon)
        
# Create an empty key list
matching_keys = []

# Loop through all key-value pairs in the date dictionary
for the_key, the_value in date_dict.items():
    # Check if the date matches the user date
    if the_value == user_date:
        matching_keys.append(the_key)
        
# Report whether no keys were found
if len(matching_keys) == 0:
    print(f"Sara was not located on {user_date}")
else:  
    # Reveal locations for each key in matching_keys
    for matching_key in matching_keys:
        obs_lat, obs_lon = location_dict[matching_key]
        print(f"Record {matching_key} indicates Sara was seen at lat:{obs_lat}, lon:{obs_lon} on {user_date}")