# datafun-05-sql
In this project, we will be working with Python and SQLite to grasp a statistical inference on some data files. These files are CSV and are used from [Sports Refrerence](https://www.sports-reference.com/cbb/schools/kansas/men/2024.html) which are current KU baskeball roster and total statistics.

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
