from sys import argv
from random import shuffle

##passing inputs to the file
scriptname, players_list_input, pair_players_output = argv

#open the input file
players = open(players_list_input)

#readlines of the opened input file
players_list = players.readlines()

#shuffling the list of players
shuffle(players_list)

#dividing the list into two parts 1)players_list1 2)players_list2

players_list1 = players_list[:len(players_list)/2]
players_list2 = players_list[len(players_list)/2:]

#write the ouput to a file
players_ouput = open(pair_players_output, "w")

for players1_name,players2_name in zip(players_list1,players_list2):
    players_ouput.write("%s%s\n" %(players1_name,players2_name))

players_ouput.close()
