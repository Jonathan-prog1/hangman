import sqlite3
# Creates the words Table
def create_table():
    # Connect to database file
    conn = sqlite3.connect("wordlist.db")
    # Crate a cursor
    c = conn.cursor()
    # Create Table
    c.execute("CREATE TABLE words (name text)")
    # Commit our comand and close connection
    conn.commit()
    conn.close()

# add one word to the words table
def add_one(word):
    # Connect to database file
    conn = sqlite3.connect("wordlist.db")
    # Crate a cursor
    c = conn.cursor()
    
    # Add one value to the table
    c.execute(f"INSERT INTO words VALUES (?)", (word,))
    # Commit our comand and close connection
    conn.commit()
    conn.close()

# This adds a few words to a new table for peole who are first loading this  up
def add_sample(list):
    # Connect to database file
    conn = sqlite3.connect("wordlist.db")
    # Crate a cursor
    c = conn.cursor()
    
    c.executemany("INSERT INTO words VALUES (?)",(list))

    # Commit our comand and close connection
    conn.commit()
    conn.close()

# Qury The DB and Return All Records
def showall():
    # Connect to database file
    conn = sqlite3.connect("wordlist.db")
    # Crate a cursor
    c = conn.cursor()
    # Query the Database
    c.execute("SELECT rowid, * FROM words")
    items = c.fetchall()
    
    for item in items:
        print(item[0], item[1])

    # Close our connection with the db file
    conn.close()

# Returns all words to get picked at random
def all_words():
    # Connect to database file
    conn = sqlite3.connect("wordlist.db")
    # Crate a cursor
    c = conn.cursor()
    # Query the Database
    c.execute("SELECT name FROM words")
    items = c.fetchall()
    
    # Close our connection with the db file
    conn.close()
    # Flatten the list of tuples to a list of strings
    return [item[0] for item in items]

    
    
# Delete one word form the DB
def delete_one(id):
    # Connect to database file
    conn = sqlite3.connect("wordlist.db")
    # Crate a cursor
    c = conn.cursor()
    
    # Remove one word from the table
    c.execute("DELETE FROM words WHERE rowid = (?)", id)

    # Commit our comand and close connection
    conn.commit()
    conn.close()

if __name__ == "__main__":    
    #create_table()
    showall()