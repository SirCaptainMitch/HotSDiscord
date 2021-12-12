import pyodbc

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=192.168.0.245;DATABASE=lookingglass;UID=thecaptain;PWD=99Redbal00ns')
cursor = cnxn.cursor()
