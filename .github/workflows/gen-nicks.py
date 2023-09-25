import random

def generate_minecraft_username():
    prefixes = ["Cool", "Pro", "Epic", "Awesome", "Master", "Crafty", "Super", "Ultra", "Mega", "Gamer"]
    suffixes = ["Player", "Gamer", "Minecrafter", "Builder", "Adventurer", "Champion", "Hero", "Ninja", "Wizard", "Explorer"]

    prefix = random.choice(prefixes)
    suffix = random.choice(suffixes)
    number = random.randint(1000, 9999)

    return f"{prefix}{suffix}{number}"

def generate_many_usernames(number_of_usernames):
    usernames = set()
    while len(usernames) < number_of_usernames:
        username = generate_minecraft_username()
        usernames.add(username)
    return usernames

def main():
    number_of_usernames = 500000  # Задайте желаемое количество никнеймов

    generated_usernames = generate_many_usernames(number_of_usernames)

    with open("minecraft_usernames.txt", "w") as file:
        for username in generated_usernames:
            file.write(username + "\n")

if __name__ == "__main__":
    main()
