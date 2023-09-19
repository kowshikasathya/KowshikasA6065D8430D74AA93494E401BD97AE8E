# Define the Batsman class
class Batsman:
    def __init__(self, name):
        self.name = name

    def play(self):
        print(f"{self.name} is batting.")

# Define the Bowler class
class Bowler:
    def __init__(self, name):
        self.name = name

    def play(self):
        print(f"{self.name} is bowling.")

# Create objects of Batsman and Bowler classes
batsman = Batsman("Batsman A")
bowler = Bowler("Bowler X")

# Call the play() method for each object
batsman.play()
bowler.play()