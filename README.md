We developed a desktop inventory management application named Grocify using PyQt5 on macOS. The development environment includes VS Code, Anaconda virtual environment, and Terminal. For database management, we used MySQL accessed via SQLTools MySQL/MariaDB/TiDB extension in VS Code as well as MySQL Workbench.
![image](https://github.com/user-attachments/assets/2d2f52ac-9055-4271-b41e-8319f2469801)

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
)
```

3. In your VSCode Terminal, we use Anaconda to create and activate a virtual environment, here are the commands: 
- conda create --name pyqt_env
- conda activate pyqt_env
- pip install pyqt5
- pip install mysql-connector-python

4. After activating the virtual environment, please type these commands:
- python data_generation.py
- mysql -u root -p < test.session.sql
- python main.py
