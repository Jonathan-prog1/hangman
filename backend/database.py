import sqlite3
class Database:
    def __init__(self):
        # Connect to database file
        self.conn = sqlite3.connect("backend/wordlist.db")
        # Crate a cursor
        self.cursor = self.conn.cursor()
    
    def close(self):
        self.conn.close()
    
    def create_table(self):
        """This creates the words Table for all the words for the hang man game."""
        
        # Create Table
        self.cursor.execute("CREATE TABLE words (name text)")
        # Commit our comand
        self.cursor.commit()

    def add_one(self, word:str):
        """add one word to the words table"""
        # Add one value to the table
        self.cursor.execute("INSERT INTO words VALUES (?)", (word,))
        # Commit our comand
        self.conn.commit()

    def add_sample(self, words:list):
        """This adds a few words to a new table for peole who are first loading this  up"""
        
        self.cursor.executemany("INSERT INTO words VALUES (?)",(words))

        # Commit our comand
        self.conn.commit()

    def showall(self):
        """This Qury The DB and Return All Records"""
        
        # Query the Database
        self.cursor.execute("SELECT rowid, * FROM words")
        words = self.cursor.fetchall()
        return words

    def all_words(self):
        """Returns all words to get picked at random"""
        # Query the Database
        self.cursor.execute("SELECT name FROM words")
        items = self.cursor.fetchall()
        # Flatten the list of tuples to a list of strings
        return [item[0] for item in items]  
      
    def delete_one(self, selected_id:str):
        """Delete one word form the DB"""
        
        # Remove one word from the table
        self.cursor.execute(f"DELETE FROM words WHERE rowid = (?)", (selected_id,))

        # Commit our comand
        self.conn.commit()
        
    def update_word(self, word:str, selected_id:str):
        """This Update's a Record in the Database"""
        
        # updates one value to the table
        self.cursor.execute("UPDATE words SET name = ? WHERE rowid = ? ", (word, selected_id))
        
        # Commit our comand
        self.conn.commit()

    def one_word(self, selected_id:str):
        """This get's one Word from the Database"""
        # Query the Database
        self.cursor.execute(f"SELECT * FROM words WHERE rowid = (?)",(selected_id, ))
        word = self.cursor.fetchone()
        return word
