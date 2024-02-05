# datafun-05-sql
In this project, we will be working with Python and SQLite to grasp a statistical inference on some data files. 

## Before Starting the Project
First, we will need to activate a virtual environment and install any exteranl libraires through the terminal. Make sure to create the .gitignore file and report that .venv and .vscode contents are not pushed to your GitHub repo.
```shell
py -m venv .venv
.venv\Scripts\activate
py -m pip install pandas pyarrow
py -m pip freeze > requirements.txt
ni .gitignore
```

At any time you want to commit to the project, simply do the following:
```shell
git add.
git commit -m "commit message"
git push
```

In the root project folder, we need to create a folder to store all the CSV and JSON files. Also, since we are using SQLite, we should create a folder to store all the sql files.
```shell
mkdir data
mkdir sql
```

If you are using VS Code, You will need to install the SQLite Viewer to view the database.

## Gathering Data
I gathered my data from the following website which is a hub for sports statistics. The link will take you to the page that I used for this project.
-  [Sports Refrerence](https://www.sports-reference.com/cbb/conferences/big-12/men/2024-stats.html)

## Making the Query Files
I made SQL files for each query. You can either run a piece of code to accopmlish the same thing.
```shell
ni name_of_query.sql
```

## Python Script
```shell
ni file_name.py
```
In this script, I created a database, tables for the database, and inserted the data into the tables. For each function there will be a log on whether it has succeeded for failed. The file for the log is log.txt.
