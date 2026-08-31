import random

achievements = ["First Steps",
                "Crafting Genius",
                "Strategist",
                "World Savior",
                "Speed Runner",
                "Survivor",
                "Master Explorer",
                "Treasure Hunter",
                "Unstoppable",
                "Collector Supreme",
                "Untouchable",
                "Sharp Mind",
                "Boss Slayer",
                "Hidden Path Finder"]


def gen_player_achievements(achievements):
    nbr = random.randint(3, 7)
    return set(random.sample(achievements, nbr))


def main():
    print("=== Achievement Tracker System ===")
    print()
    alice = gen_player_achievements(achievements)
    bob = gen_player_achievements(achievements)
    charlie = gen_player_achievements(achievements)
    dylan = gen_player_achievements(achievements)
    print("Player Alice:", alice)
    print("Player Bob:", bob)
    print("Player Charlie:", charlie)
    print("Player Dylan:", dylan)
    all_achievements = set.union(alice, bob, charlie, dylan)
    print("All distinct achievements:", all_achievements)
    common = set.intersection(alice, bob, charlie, dylan)
    print()
    print("Common achievements:", common)
    print()
    print("Only Alice has:",
          set.difference(alice, set.union(bob, charlie, dylan)))
    print("Only Bob has:",
          set.difference(bob, set.union(alice, charlie, dylan)))
    print("Only Charlie has:",
          set.difference(charlie, set.union(alice, bob, dylan)))
    print("Only Dylan has:",
          set.difference(dylan, set.union(alice, bob, charlie)))
    print()
    print("Alice is missing:", set.difference(all_achievements, alice))
    print("Bob is missing:", set.difference(all_achievements, bob))
    print("Charlie is missing:", set.difference(all_achievements, charlie))
    print("Dylan is missing:", set.difference(all_achievements, dylan))


if __name__ == "__main__":
    main()
