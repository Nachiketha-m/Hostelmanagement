import mysql.connector
user=input()
pwd=input()

mydb = mysql.connector.connect(host = "localhost",user = "root",password = "Amadpsnacha@123",database="projecthostel")
cur=mydb.cursor()
cur.execute(f"SELECT * from userpwd")
l=cur.fetchone()
while l is not None:
    print(l)
    if user in l:
        print('ok')
        break
    l=cur.fetchone()
##if not cur.fetchone():
##    print("User Name not Found")
##else:
##    print("User Found ")

