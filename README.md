We use PyQT5, Vscode, SQLTools MySQL/MariaDB/TiDB, SQLTools Extension, Anaconda Virtual Environment, Terminal, Mysql Workench.

1. Please download and install these extensions from the VSCode marketplace:
- **SQLTools MySQL/MariaDB/TiDB**
- **SQLTools Extension**
  
2. In SQLTools, choose MySQL as the database type.
Fill in the details for your root username, password. For database name, please type test (we use test for our database name). Then, save the connection.
Also, in the **data_generation.py** file, please update the following code with your database details:

```python
conn = mysql.connector.connect(
    host="localhost",
    user="",
    password="",
    database="test"
)```python

Please fill in " " with the details you configured in SQLTools.

4. In your VSCode Terminal, we use Anaconda to create and activate a virtual environment, here are the commands: 
conda create --name pyqt_env
conda activate pyqt_env

5. After activating the virtual environment, please type these commands:
python data_generation.py
mysql -u root -p < test.session.sql
python main.py
