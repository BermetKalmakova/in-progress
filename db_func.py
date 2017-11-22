import sqlite3

f="data/users.db"
#==========================================================

def validate(username, password):
    db = sqlite3.connect(f)
    c = db.cursor()
    # print ("SELECT count(*) FROM users WHERE username = '%s' AND password = %s" % (username, password))
    found = c.execute("SELECT count(*) FROM users WHERE username = '%s' AND password = '%s'" % (username, password))
    for num in found:
        db.commit()
        db.close()
        return (num[0] == 1)

def hasUsername(username):
    db = sqlite3.connect(f)
    c = db.cursor()
    # print ("SELECT count(*) FROM users WHERE username = '%s'" % (username))
    found = c.execute("SELECT count(*) FROM users WHERE username = '%s'" % (username))
    for num in found:
        db.commit()
        db.close()
        return (num[0] == 1)

def addUser(username, password):
    db = sqlite3.connect(f)
    c = db.cursor()
    c.execute("INSERT INTO users VALUES('%s', '%s')" % (username, password))
    db.commit()
    db.close()
    
def updatePassword(username, newpass):
    db = sqlite3.connect(f)
    c = db.cursor()
    c.execute("UPDATE users SET password = '%s' WHERE username = '%s'" % (newpass, username))
    db.commit()
    db.close()

