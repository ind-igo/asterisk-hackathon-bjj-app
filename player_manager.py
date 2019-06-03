import sqlite3

class PlayerManager():
  sql_db = "/home/sali/Projects/bjj_app_hackathon/flowy.sqlite"
  db = sqlite3.connect(sql_db)
  cur = db.cursor()
  
  def __init__(self):
    #init tables
    self.cur.execute("""CREATE TABLE IF NOT EXISTS Players (
      player_id INTEGER PRIMARY KEY,
      player_name TEXT NOT NULL,
      weight INTEGER NOT NULL,
      belt INTEGER NOT NULL,
      rating_mu REAL NOT NULL,
      rating_sigma REAL NOT NULL,
      lookingForMatch BOOLEAN)""")
    
    self.cur.execute("""CREATE TABLE IF NOT EXISTS Matches (
      match_id INTEGER PRIMARY KEY,
      player_id INTEGER NOT NULL,
      opponent_id INTEGER NOT NULL,
      result CHAR NOT NULL,
        FOREIGN KEY (player_id) REFERENCES Players(player_id))""")

  def __del__(self):
    self.db.close()

  def create_player(self, name_, weight_, belt_, mu_, sigma_):
    add_player = "INSERT INTO Players (player_name, weight, belt, rating_mu, rating_sigma, lookingForMatch) VALUES (?, ?, ?, ?, ?, ?)"
    self.cur.execute(add_player, (str(name_), int(weight_), int(belt_), float(mu_), float(sigma_), 1))
    self.db.commit()
  
  def get_player(self, playerId_):
    #self.cur.execute("SELECT DISTINCT player_id, player_name, weight, belt, rating_mu, rating_sigma, lookingForMatch FROM Players WHERE player_id = ?", (playerId_))
    self.cur.execute("SELECT player_id, player_name, rating_mu, rating_sigma FROM Players WHERE player_id = :Id", {"Id": playerId_})
    return self.cur.fetchone()

  def update_player_rating(self, playerId_, playerMu_, playerSigma_):
    self.cur.execute("UPDATE Players SET rating_mu = ?, rating_sigma = ? WHERE player_id = ?", (playerMu_, playerSigma_, playerId_))
    self.db.commit()

  def record_match(self, playerId_, opponentId_, result_):
    if result_ == 'W':
      opponent_result = 'L'
    elif result_ == 'L':
      opponent_result = 'W'
    else:
      print("Error recording match")
      pass

    add_match = "INSERT INTO Matches (player_id, opponent_id, result) VALUES (?, ?, ?)"
    self.cur.execute(add_match, (int(playerId_), int(opponentId_), str(result_)))
    db.commit()
    self.cur.execute(add_match, (int(opponentId_), int(playerId_), str(opponent_result)))
