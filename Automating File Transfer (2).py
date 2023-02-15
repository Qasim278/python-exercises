''' You work at a company that receives daily data files from external partners. These files need to be processed and analyzed, but first, they need to be transferred to the company's internal network.

The goal of this project is to automate the process of transferring the files from an external FTP server to the company's internal network.

Here are the steps you can take to automate this process:

    Use the ftplib library to connect to the external FTP server and list the files in the directory.

    Use the os library to check for the existence of a local directory where the files will be stored.

    Use a for loop to iterate through the files on the FTP server and download them to the local directory using the ftplib.retrbinary() method.

    Use the shutil library to move the files from the local directory to the internal network.

    Use the schedule library to schedule the script to run daily at a specific time.

    You can also set up a log file to keep track of the files that have been transferred and any errors that may have occurred during the transfer process. '''

# import libraries
from ftplib import FTP
import os
import shutil
from datetime import datetime
import schedule

# Config Parameters
host_config = {
    "host" : "ftp.dlptest.com",
    "username" : "dlpuser",
    "password" : "rNrKYTX9g7z3RgJRmxWuGHbeu"
}

# host_config = {
#     "host" : "ftp.otenet.gr",
#     "username" : "speedtest",
#     "password" : "speedtest"
# }

local_directory = "./temp"
network_directory = "./my_network_dir"

execution_time = "12:52:00"

def create_dir(path):
    # Check if directory exists
    if os.path.exists(path):
        print(f"Directory Exists ==> {path}")
    else:
        print(f"Directory Doesn't Exists ==> {path}")
        
        print("Creating Directory")
        os.makedirs(path)
        
        print("Directory Successfully Created")

def main():
    print(f"Current time: {str(datetime.now())}")
    # Connect to FTP Server
    ftp = FTP(
        host= host_config["host"],
        user=host_config["username"], 
        passwd=host_config["password"]
    )

    print(f"Successfully connected to FTP server @ {host_config['host']}")
    print(f"--------------- Welcome message from server ---------------\n{ftp.getwelcome()}\n")

    # Check if local directory exists and create it
    print(f"Verifying local directory ==> {local_directory}")
    create_dir(local_directory)

    # Download files from server
    print(f"Downloading files from server path: {ftp.pwd()}")
    print("--------------------")
    for file in ftp.nlst():    
        if file not in ["frep", "input"]:
            print(f"Current File ==> {file}")
            with open(f"{local_directory}/{file}", "wb") as output_file:
                ftp.retrbinary(f"RETR {file}", output_file.write)
            print(f"Downloaded successfully\n") 
    print("--------------------")
    print("All files downloaded successfully.")

    # Close the connection
    print("Closing the ftp connection.")
    ftp.close()

    # Check if network directory exists and create it
    print(f"Verifying network directory ==> {network_directory}")
    create_dir(network_directory)

    # Move files to the network directory
    for file in os.listdir(local_directory):
        print(file)
        shutil.move(f"{local_directory}/{file}", network_directory)


if __name__ == "__main__":
    # Scheduling using Schedule libary
    schedule.every().day.at(execution_time).do(main)

    while True:
        schedule.run_pending()

