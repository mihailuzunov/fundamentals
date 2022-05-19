referee_book = input().split(" ")

count_A = 11
count_B = 11
referee_book_without_dublicates = list(set(referee_book))
for player in referee_book_without_dublicates:
    player = player.split("-")
    if player[0] == "A":
        count_A -= 1
    else:
        count_B -= 1
print(f"Team A - {count_A}; Team B - {count_B}")
if count_A < 7 or count_B < 7:
    print("Game was terminated")


#test
