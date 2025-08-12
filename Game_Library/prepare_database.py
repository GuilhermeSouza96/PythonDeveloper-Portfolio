import mysql.connector
from mysql.connector import errorcode

print("Connecting...")
try:
      conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='admin'
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Something is wrong with your user name or password')
      else:
            print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `game_library`;")

cursor.execute("CREATE DATABASE `game_library`;")

cursor.execute("USE `game_library`;")

TABLES = {}
TABLES['Games'] = ('''
                   CREATE TABLE `Games` (
                    `id` int(11) NOT NULL AUTO_INCREMENT,
                    `name` varchar(50) NOT NULL,
                    `category` varchar(40) NOT NULL,
                    `console` varchar(20) NOT NULL,
                   PRIMARY KEY (`id`)
                   ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Users'] = ('''
      CREATE TABLE `users` (
      `name` varchar(20) NOT NULL,
      `nickname` varchar(15) NOT NULL,
      `password` varchar(100) NOT NULL,
      PRIMARY KEY (`nickname`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for tabel_name in TABLES:
      tabel_sql = TABLES[tabel_name]
      try:
            print('Creating tabel {}:'.format(tabel_name), end=' ')
            cursor.execute(tabel_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Already exists')
            else:
                  print(err.msg)
      else:
            print('OK')

users_sql = 'INSERT INTO users (name, nickname, password) VALUES (%s, %s, %s)'
users = [
      ('Guilherme', 'Guilherme96', 'senha'),
      ("Bruno Divino", "BD", "alohomora"),
      ("Camila Ferreira", "Mila", "paozinho"),
      ("Guilherme Louro", "Cake", "python_eh_vida")
]
cursor.executemany(users_sql, users)

cursor.execute('select * from game_library.users')
print(' -------------  Users:  -------------')
for user in cursor.fetchall():
    print(user[1])

# inserindo jogos
games_sql = 'INSERT INTO games (name, category, console) VALUES (%s, %s, %s)'
games = [
      ('Tetris', 'Puzzle', 'Atari'),
      ('God of War', 'Hack n Slash', 'PS2'),
      ('Mortal Kombat', 'Luta', 'PS2'),
      ('Valorant', 'FPS', 'PC'),
      ('Crash Bandicoot', 'Hack n Slash', 'PS2'),
      ('Need for Speed', 'Corrida', 'PS2'),
]
cursor.executemany(games_sql, games)

cursor.execute('select * from game_library.games')
print(' -------------  Games:  -------------')
for game in cursor.fetchall():
    print(game[1])

# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()