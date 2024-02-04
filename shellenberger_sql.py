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

def create_database(db_file):
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

def insert_data_from_csv(db_file):
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

def execute_sql_from_file(db_file, sql_file):
    '''
    Executes the related SQL file and updates the database.
    :param db_filepath: Path to the database
    :param sql_file: Path to the SQL file
    '''
    try:
        with sqlite3.connect(db_file) as conn:
            with open(pathlib.Path("sql").joinpath(sql_file), 'r') as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            logging.info(f"Executed SQL from: {sql_file}")
    except sqlite3.Error as e:
        logging.error(f"Error executing SQL: {sql_file}", e)

def main():
    """Main function"""    
    # Configure logging to write to a file, appending new logs to the existing file
    logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("Program started")
    
    print(f'Byline: {utils.company_name}')
    
    # Define the database file in the current root project directory
    db_file = "project.db"
    
    create_database(db_file)
    
    execute_sql_from_file(db_file, 'create_tables.sql')
    insert_data_from_csv(db_file)
    execute_sql_from_file(db_file, 'insert_records.sql')
    execute_sql_from_file(db_file, 'update_records.sql')
    execute_sql_from_file(db_file, 'delete_records.sql')
    execute_sql_from_file(db_file, 'query_aggregation.sql')
    execute_sql_from_file(db_file, 'query_filter.sql')
    execute_sql_from_file(db_file, 'query_sorting.sql')
    execute_sql_from_file(db_file, 'query_group_by.sql')
    execute_sql_from_file(db_file, 'query_join.sql')
    
    logging.info("Program ended")
    

if __name__ == "__main__":
    main()