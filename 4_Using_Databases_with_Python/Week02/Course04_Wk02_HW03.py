# Course 04 Week 02 Assignment 03
# Adam Britt
# 03/02/2018
#
# Problem Definition:
#
# Following Links in Python
#
# Read the mailbox data from mbox.txt and count the number of email messages
# per organization (i.e. domain name of the email address) using a database with
# the following schema to maintain the counts.
#
#   CREATE TABLE Counts (org TEXT, count INTEGER)
#
# After running the program, upload the resulting database for grading.
#
# Hint: The top organizational count is 536.
#
################################################################################


import sqlite3

conn = sqlite3.connect('Course04_Wk02_HW03.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    pieces2 = email.split('@')
    org = pieces2[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
