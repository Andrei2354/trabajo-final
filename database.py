import sqlite3

class Database:
    def __init__(self):
        pass

    def getAll(self, table:str):
        self.conn = sqlite3.connect('data/database.db') 
        self.cursor = self.conn.cursor()   
        self.cursor.execute('SELECT * FROM ' + table)
        return self.cursor
    
    def close(self):
        self.conn.close()

    def __del__(self):
        self.conn.close()

    def insert(self, table:str, sqlv:str, values:tuple):
        self.conn = sqlite3.connect('data/database.db') 
        self.cursor = self.conn.cursor()
        self.cursor.execute('INSERT INTO ' + table + ' VALUES ' + sqlv, values)
        self.conn.commit()
        self.conn.close()

    def update(self, table:str, set:str, where:str, values:tuple):
        self.conn = sqlite3.connect('data/database.db') 
        self.cursor = self.conn.cursor()
        self.cursor.execute('UPDATE ' + table + ' SET ' + set + ' WHERE ' + where, values)
        self.conn.commit()
        self.conn.close()

    def delete(self, table:str, where:str, values:tuple):
        self.conn = sqlite3.connect('data/database.db') 
        self.cursor = self.conn.cursor()
        self.cursor.execute('DELETE FROM ' + table + ' WHERE ' + where, values)
        self.conn.commit()
        self.conn.close()