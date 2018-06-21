class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
cup_of_life = Song(["The cup of life, this is the one","Now is the time, don't ever stop","Push it along, gotta be strong","Push it along, right to the top"])
titanic = Song(["Every night in my dreams","I see you, I feel you","That is how I know you go on","Far across the distance","And spaces between us","You have come to show you go on"])
cup_of_life.sing_me_a_song()
titanic.sing_me_a_song()
