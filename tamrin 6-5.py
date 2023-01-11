# tamrin 6-5
height_players = input("please enter your height : ")
list_height_players = height_players.split()
print("list_height_players =", list_height_players)
count = len(list_height_players)
for i in range(0, count):
    list_height_players[i] = int(list_height_players[i])
sum_final = sum(list_height_players)
ave = sum_final // count
print("ave ::", ave, "cm")
