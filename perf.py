import pandas as pd
import pyodbc
import pysftp
import re

server = pysftp.Connection(host=FTP_HOST,
                  username=FTP_USERNAME,
                  password=FTP_PASSWORD)
server.cwd(file path)
filelist = server.listdir()

for filename in filelist:
    filename= re.search(".*\.csv$", filename)

	sftp.get(remote_path, filename)
'''
Opening the File Path
'''
	data = pd.read_csv(r'filename')  #Path to be provided here where csv's are present or we can change the working directory abobe this live and pass the variable
	df = pd.DataFrame(data, columns = ['Result Time','Granularity Period','Object Name','Cell ID','CallAttemps'])
'''
Connecting with Database with information to be filled 
'''
	conn = pyodbc.connect('Driver','Server','Database','Trusted_Connection') #Database details to be provided
	cursor  = conn.cursor()
	cursor.execute('create table Perf (Result_Time nvarchar(50) , Granularity_Period nvarchar(100), Object_Name nvarchar(50), Cell_ID int , CallAttemps int ')

	for row in df.itertuples():
		cursor.execute(''' INSERT INTO DATABASENAME.PERF(Result_Time,Granularity Period,Object Name,Cell ID,CallAttemps) VALUES (?,?,?,?,?) ''',row.Result_Time,row.Granularity_Period,row.Object_Name , row.Cell_ID, row.CallAttemps)
	
conn.commit()
	
