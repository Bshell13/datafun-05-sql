"""
This In this project, we will be working with Python and SQLite to grasp a statistical inference on some data files. 

"""
# Standard Python Libraries
import sqlite3
import pathlib

# External Libraries
import pandas as pd
import logging

# Local Libraries
import shellenberger_utils as utils

# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Program started")

# Define the database file in the current root project directory
db_file = pathlib.Path("project.db")

def create_database():
    """Function to create a database. Connecting for the first time
    will create a new database file if it doesn't exist yet.
    Close the connection after creating the database
    to avoid locking the file."""
    logging.info("Creating database")
    try:
        conn = sqlite3.connect(db_file)
        conn.close()
        logging.info("Database created successfully.")
    except sqlite3.Error as e:
        logging.exception("Error creating the database:", e)

def create_tables():
    """Function to read and execute SQL statements to create tables"""
    logging.info("Creating tables")
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql", "create_tables.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            logging.info("Tables created successfully.")
    except sqlite3.Error as e:
        logging.exception("Error creating tables:", e)

def insert_data_from_csv():
    """Function to use pandas to read data from CSV files (in 'data' folder)
    and insert the records into their respective tables."""
    logging.info("Inserting data from CSV files")
    try:
        players_data_path = pathlib.Path("data", "players.csv")
        schools_data_path = pathlib.Path("data", "schools.csv")
        players_df = pd.read_csv(players_data_path)
        schools_df = pd.read_csv(schools_data_path)
        with sqlite3.connect(db_file) as conn:
            # use the pandas DataFrame to_sql() method to insert data
            # pass in the table name and the connection
            players_df.to_sql("players", conn, if_exists="replace", index=False)
            schools_df.to_sql("schools", conn, if_exists="replace", index=False)
            logging.info("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        logging.exception("Error inserting data:", e)

def main():
    print(f'Byline: {utils.company_name}')
    
    create_database()
    create_tables()
    insert_data_from_csv()
    
    logging.info("Program ended")

if __name__ == "__main__":
    main()