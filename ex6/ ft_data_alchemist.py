import random


def main():
    print("=== Game Data Alchemist ===")

    players = ["Alice", "bob", "Charlie", "dylan", "Emma",
               "Gregory", "john", "kevin", "Liam"]

    print(f"Initial list of players: {players}")

    capitalized = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {capitalized}")

    capitalized_only = [name for name in players if name[0].isupper()]
    print(f"New list of capitalized names only: {capitalized_only}")

    scores = {name: random.randint(1, 1000) for name in capitalized}
    print(f"Score dict: {scores}")

    average = round(sum(scores.values()) / len(scores), 2)
    print(f"Score average is {average}")

    high_scores = {
        name: scores[name] for name in scores if scores[name] > average
        }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
