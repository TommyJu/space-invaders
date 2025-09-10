import os

file_path = "high_score.txt"

# Function to load high score
def load_high_score():
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            try:
                return int(f.read())
            except ValueError:
                # Handle case where file is empty or corrupted
                return 0
    else:
        # File doesn't exist yet
        return 0

# Function to save high score
def save_high_score(score):
    with open(file_path, "w") as f:
        f.write(str(score))