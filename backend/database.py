import sqlite3

def connect():
    # Connect to database file
    conn = sqlite3.connect("backend/wordlist.db")
    # Crate a cursor
    c = conn.cursor()
    return conn , c
# Creates the words Table
def create_table():
    # Connect to database
    conn, c = connect()
    # Create Table
    c.execute("CREATE TABLE words (name text)")
    # Commit our comand and close connection
    conn.commit()
    conn.close()

# add one word to the words table
def add_one(word):
    # Connect to database
    conn, c = connect()
    
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
    # Connect to database
    conn, c = connect()
    # Query the Database
    c.execute("SELECT rowid, * FROM words LIMIT 10")
    words = c.fetchall()
    # Close our connection with the db file
    conn.close()
    return words

# Returns all words to get picked at random
def all_words():
    # Connect to database
    conn, c = connect()
    # Query the Database
    c.execute("SELECT name FROM words")
    items = c.fetchall()
    
    # Close our connection with the db file
    conn.close()
    # Flatten the list of tuples to a list of strings
    return [item[0] for item in items]  
    
# Delete one word form the DB
def delete_one(selected_id):
    conn, c = connect()
    
    # Remove one word from the table
    c.execute("DELETE FROM words WHERE rowid = (?)", selected_id)

    # Commit our comand and close connection
    conn.commit()
    conn.close()

# Update Records
def update_word(word, selected_id):
    # Connect to database
    conn, c = connect()
    
    # updates one value to the table
    c.execute("UPDATE words SET name = ? WHERE rowid = ? ", (word, selected_id))
    
    # Commit our comand and close connection
    conn.commit()
    conn.close()

# Get one Word
def one_word(selected_id):
    # Connect to database
    conn, c = connect()
    # Query the Database
    c.execute("SELECT * FROM words WHERE rowid = (?)", selected_id)
    word = c.fetchone()
    # Close our connection with the db file
    conn.close()
    return word