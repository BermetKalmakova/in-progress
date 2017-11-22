import sqlite3  

f="data/users.db"
db = sqlite3.connect(f)
c = db.cursor()    

def table_gen():
    create_users = "CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT)"
    c.execute(create_users)
              
table_gen()

db.commit() #save changes
db.close()  #close database
