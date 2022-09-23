'''

Program:    Zip Protocol
Author:     Zach Franke
Date:       2022-09-22

Description: This program will target a provided directory in the cli argument and unzip any folders present. 
A log will be kept in the program directory.

'''

from zipfile import ZipFile
import sys

#Define function to unzip the directory and unzip it to the specified directory
def unzip_directory(directory, targetDirectory):
    with ZipFile('sampleDir.zip', 'r') as zipObj:
        zipObj.extractall(targetDirectory)
        
        
#Define function to log the unzipping of the directory
def log_unzip(directory, targetDirectory):
    with open('log.txt', 'a') as log:
        log.write(f'Unzipped {directory} to {targetDirectory}.')
    
#Define main function
def main():
    
    #Check if the directory is provided in the cli argument
    if len(sys.argv) < 2:
        print('Please provide the directory to unzip.')
        sys.exit(1)
        
    #Assign the directory to a variable
    directory = sys.argv[1]
    
    #Assign the target directory to a variable
    targetDirectory = sys.argv[2]
    
    #Call the unzip_directory function
    unzip_directory(directory, targetDirectory)
    
    #Call the log_unzip function
    log_unzip(directory, targetDirectory)
    