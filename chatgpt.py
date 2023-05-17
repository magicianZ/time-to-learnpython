import random

# Pokémon class
class Pokemon:
    def __init__(self, name, level, type, max_hp, current_hp, moves):
        self.name = name
        self.level = level
        self.type = type
        self.max_hp = max_hp
        self.current_hp = current_hp
        self.moves = moves

    def __str__(self):
        return f"{self.name} (Level {self.level})"

    def choose_move(self):
        print(f"{self.name}'s Moves:")
        for i, move in enumerate(self.moves):
            print(f"{i + 1}. {move}")
        move_choice = int(input("Enter the move number: ")) - 1
        return self.moves[move_choice]

# Battle function
def battle(player_pokemon, opponent_pokemon):
    print("A wild", opponent_pokemon, "appears!\n")
    while True:
        print("Your Pokémon:", player_pokemon)
        print("Opponent's Pokémon:", opponent_pokemon)

        # Player's turn
        player_move = player_pokemon.choose_move()
        print(f"\n{player_pokemon.name} uses {player_move}!")
        opponent_pokemon.current_hp -= random.randint(10, 20)

        # Check if opponent's Pokémon is defeated
        if opponent_pokemon.current_hp <= 0:
            print(f"\nOpponent's {opponent_pokemon.name} faints!")
            print("You win!")
            break

        # Opponent's turn
        opponent_move = random.choice(opponent_pokemon.moves)
        print(f"\nOpponent's {opponent_pokemon.name} uses {opponent_move}!")
        player_pokemon.current_hp -= random.randint(10, 20)

        # Check if player's Pokémon is defeated
        if player_pokemon.current_hp <= 0:
            print(f"\n{player_pokemon.name} faints!")
            print("You lose!")
            break

        print()

# Main game loop
def play_game():
    # Create player's Pokémon
    player_pokemon = Pokemon("Charmander", 5, "Fire", 50, 50, ["Ember", "Scratch", "Growl", "Leer"])

    # Create opponent's Pokémon
    opponent_pokemon = Pokemon("Bulbasaur", 5, "Grass", 50, 50, ["Vine Whip", "Tackle", "Growl", "Leer"])

    print("Welcome to the Pokémon Battle!")
    print("You have encountered a wild Pokémon.\n")

    # Start the battle
    battle(player_pokemon, opponent_pokemon)

# Start the game
play_game()
