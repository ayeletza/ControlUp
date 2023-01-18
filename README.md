# ControlUp
A basic code to connect AWS cloud with a local service.

The main purpose of this project is to read from the cloud a simple file which contains links to "zap" site, for each url, the system finds the prices and calculates the maximum, minimum and average prices.<br>
The results, timestamp included, are saved in a DB located in AWS cloud.
<br>

## In this project there are 5 Python files as follow:
* main.py - the main file to run the system.
* ReadFile.py - a code to read the simple file from the cloud.
* SearchTheNet.py - reads url and calculates the maximum, minimum and average prices.
* Backend.py - a code to build the DB and table if needed, and add entry to the DB as requested.
* Constants.py - a file which contains all the constants that are needed for the project.

