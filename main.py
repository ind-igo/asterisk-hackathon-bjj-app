from trueskill import Rating, rate_1vs1
from player_manager import PlayerManager
from constants import BeltColor as belt

player_exec = PlayerManager()

def create_test_players():
  p1_rating = Rating()
  p2_rating = Rating()
  p3_rating = Rating()
  p4_rating = Rating()
  p5_rating = Rating()
  player_exec.create_player('Saad', 145, belt.BLUE, p1_rating.mu, p1_rating.sigma)
  player_exec.create_player('Joseph', 180, belt.WHITE, p2_rating.mu, p2_rating.sigma)
  player_exec.create_player('Brandon', 145, belt.PURPLE, p3_rating.mu, p3_rating.sigma)
  player_exec.create_player('Omar', 145, belt.WHITE, p4_rating.mu, p4_rating.sigma)
  player_exec.create_player('Matt', 145, belt.BLUE, p5_rating.mu, p5_rating.sigma)

def create_match():
  # create player tuples and corresponding rating objects
  player_joseph = player_exec.get_player(2)
  player_omar = player_exec.get_player(4)
  joseph_rating = Rating(player_joseph[2],player_joseph[3])
  omar_rating = Rating(player_omar[2],player_omar[3])

  # Rate a single 1v1 match and reassign those values
  joseph_rating, omar_rating = rate_1vs1(joseph_rating, omar_rating)

  # Update players in DB
  player_exec.update_player_rating(player_joseph[0], joseph_rating.mu, joseph_rating.sigma) 
  player_exec.update_player_rating(player_omar[0], omar_rating.mu, omar_rating.sigma)

def main():
  create_test_players()
  create_match()


if __name__ == "__main__":
  main()
  pass