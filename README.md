# DJIA Analysis

This is a Python program created as a capstone project for "Python For Everybody" course on Coursera. The program focuses on analyzing the stock data of DJIA (Dow Jones Industrial Average).

The program reads a CSV file containing the DJIA stock data, performs basic data cleaning and inserts it into an SQLite database. The second file of the program adds a simple visualization of the DJIA stock data with moving average.

## Installation

To run this program, you need to have Python 3 and the following packages installed:

- pandas
- matplotlib
- sqlite3

To install these packages, you can use pip, a package installer for Python. Here's the command to install them:

```
pip install pandas matplotlib sqlite3
```

## Usage

To use this program, you need to download the project files and save them in a directory. Then, navigate to that directory in the command line and run the following command to execute the program:

```
python 1.open_csv.py
```

This will execute the program and create a database in SQlite

Then execute the visual:

```
python 2.visual.py
```

This will execute the program and generate a visualization of the DJIA stock data with moving average.

## Acknowledgments

- "Python For Everybody" course on Coursera
- Dow Jones Industrial Average for providing the stock data.
