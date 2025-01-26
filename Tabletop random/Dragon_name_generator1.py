import random


def generate_dragon_name():
    prefixes = {
        "Drak", "Rhae", "Bal", "Mer", "Syra", "Sun", "Ver", "Dre", "Zyra",
        "Ign", "Kael", "Thal", "Anc", "Glaur", "Thaur", "Vran", "Nid",
        "Faf", "Jor", "Bah", "Tia", "Ash", "Kla", "Aur", "Imr", "Verm"
    }

    cores = {
        "gon", "gal", "ion", "rion", "zar", "thor", "zul", "vyr", "ax",
        "ara", "nor", "aug", "rung", "lor", "ath", "nir", "hogg", "gandr",
        "mat", "mith", "rith", "xal", "drel"
    }

    suffixes = {
        "thos", "mir", "nar", "zith", "arok", "ynix", "arion", "fyre",
        "nor", "rax", "ath", "gon", "aur", "lor", "nirch", "gandr", "ith",
        "onar", "thrax"
    }

    # Decide on the name length (short or long)
    name_length = random.choices(["short", "long"], weights=[0.6, 0.4], k=1)[0]

    # Randomly assemble the name
    prefix = random.choice(list(prefixes))
    core = random.choice(list(cores))
    suffix = random.choice(list(suffixes)) if random.random() > 0.5 else ""

    # Add extra components based on probability
    if random.random() < 0.1:  # 10% chance for an extra suffix
        suffix += random.choice(list(suffixes))
    elif random.random() < 0.1:  # 10% chance for an extra core+suffix
        core += random.choice(list(cores))
        suffix += random.choice(list(suffixes))

    return f"{prefix}{core}{suffix}"


def main():
    """
    Main function to generate and display a list of dragon names.
    """
    # Generate 20 unique names
    unique_names = set()
    while len(unique_names) < 20:
        unique_names.add(generate_dragon_name())

    # Print the names
    for n, name in enumerate(unique_names):
        print(f"{n + 1}: {name}")


# Generate and print a few dragon names
if __name__ == "__main__":
    main()