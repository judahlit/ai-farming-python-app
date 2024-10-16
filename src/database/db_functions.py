import sqlite3

def build_tables():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    # execute sql file
    with open('src/database/schema.sql', 'r') as f:
        sql = f.read()
        c.executescript(sql)

    conn.commit()
    conn.close()
    
def delete_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    # execute sql file
    with open('src/database/delete.sql', 'r') as f:
        sql = f.read()
        c.executescript(sql)

    conn.commit()
    conn.close()
    
    
def insert_blood_sampling_data(id, sex, country, coat_color):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    # check if animal id already exists
    c.execute('SELECT * FROM blood_sampling_data WHERE id = ?', (id,))
    if c.fetchone() is not None:
        print('Animal with id:', id, 'already exists in the database, updating')
        c.execute('UPDATE blood_sampling_data SET sex = ?, country = ?, coat_color = ? WHERE id = ?', (sex, country, coat_color, id))
        return
    
    
    c.execute('INSERT INTO blood_sampling_data (id, country, coat_color) VALUES (?, ?, ?, ?)', (id, country, coat_color))
    
    conn.commit()
    conn.close()