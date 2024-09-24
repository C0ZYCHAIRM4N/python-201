# Add an API call to your CLI game that assigns a name to your player.
import requests

def get_random_name():
    url = "https://uzby.com/api.php?min=3&max=10"  
    response = requests.get(url)
    if response.status_code == 200:
        return response.text

class Player:
    def __init__(self):
        self.name = get_random_name()

def main():
    player = Player()
    print(f"Welcome, {player.name}!")

if __name__ == "__main__":
    main()
