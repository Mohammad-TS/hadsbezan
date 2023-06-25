import random

print("be bazi hads adad khosh amadid!")
min_num = int(input("Lotfan kochektarin adad dar range ra vared konid:"))
max_num = int(input("Lotfan bozorgtarin adad dar range ra vared konid:"))

secret_num = random.randint(min_num, max_num)

guess = None
num_guesses = 0

while guess != secret_num:
    guess = int(input("Adad ra hads bezanid: "))
    num_guesses += 1
    
    if guess < secret_num:
        print("Adadi ke dar nazare man ast bozorgtar ast.")
    elif guess > secret_num:
        print("Adadi ke dar nazare man ast kuchektar ast.")
    else:
        print(f"Tabrik migoyam! Shoma adad {secret_num} ra ba {num_guesses} hads hads zadid.")