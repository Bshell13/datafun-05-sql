# datafun-05-sql
In this project, we will be working with Python and SQLite to grasp a statistical inference on some data files. 

## Before Starting the Project
First, we will need to activate a virtual environment and install any exteranl libraires through the terminal. Make sure to create the .gitignore file to report that .venv and .vscode contents are not pushed to your GitHub repo.

```shell
py -m venv .venv
.venv\Scripts\activate
py -m pip install pandas pyarrow
py -m pip freeze > requirements.txt
ni .gitignore
```

In the root project folder, we need to create a folder to store all the CSV and JSON files. Also, since we are using SQLite, we should create a folder to store all the sql files.
```shell
mkdir data
mkdir sql
```

Lastly, do not forget to create your main Python script. This is where we will use the data files and the SQL files to run a SQL query for analysis. In this case, I will be using my last name and what the project is.
```shell
ni shellenberger_sql.py
```

## Logging
In the root project, there will be a txt file for logging each major function. In each major function, a piece of code will be executed `logging.info("message to display")`. This will print to the txt file with some information about when the function was called. There might be some other information if an exception is called during the program running.