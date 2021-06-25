import re
from operator import itemgetter, attrgetter

def tally(rows):
    table = ["Team                           | MP |  W |  D |  L |  P"]
    # standings = {'Team':['MP', 'W', 'D', 'L', 'P']}
    standings = {}
    for row in rows:
        # # # First we split our input row into a list of useful info. Eg:
        # # # Allegoric Alaskans;Blithering Badgers;loss --> ["Allegoric Alaskans", "Blithering Badgers","loss"]
        outcome = row.split(';')
        # initalize a team if not already in standings
        if outcome[0] not in standings.keys():
            standings[outcome[0]] = [0,0,0,0,0]
        if outcome[1] not in standings.keys():
            standings[outcome[1]] = [0,0,0,0,0]
        if outcome[2] == "win":
            # match played increases by 1 for the first team
            standings[outcome[0]][0] += 1
            # win increaases by 1 for the first team
            standings[outcome[0]][1] += 1
            # points increase by 3 for the first team
            standings[outcome[0]][4] += 3
            # match played increases by 1 for the second team
            standings[outcome[1]][0] += 1
            # loss increaases by 1 for the second team
            standings[outcome[1]][3] += 1
            # points do not increase for the second team
        elif outcome[2] == "loss":
            # match played increases by 1 for the first team
            standings[outcome[0]][0] += 1
            # loss increaases by 1 for the first team
            standings[outcome[0]][3] += 1
            # points do not increase for the first team
            # match played increases by 1 for the second team
            standings[outcome[1]][0] += 1
            # win increaases by 1 for the second team
            standings[outcome[1]][1] += 1
            # points increase by 3 for the second team
            standings[outcome[1]][4] += 3
        elif outcome[2] == "draw":
            # match played increases by 1 for the first team
            standings[outcome[0]][0] += 1
            # draw increaases by 1 for the first team
            standings[outcome[0]][2] += 1
            # points increase by 1 for the first team
            standings[outcome[0]][4] += 1
            # match played increases by 1 for the second team
            standings[outcome[1]][0] += 1
            # draw increaases by 1 for the second team
            standings[outcome[1]][2] += 1
            # points increase by 3 for the second team
            standings[outcome[1]][4] += 1
        else:
            raise Exception(f"Should be win, draw, or loss. \n{row}")
    # # # Now i have to return the list of formated strings
    # match = re.match('(.*)|(.*)|(.*)|(.*)|(.*)|(.*)', table[0])
    # team_length = len(match.group(1)) ==> 31
    alph_sort = dict(sorted(standings.items()))
    # print(alph_sort)
    st = sorted(alph_sort.items(), key=lambda x: x[1][4],reverse=True)
    # print(st)
    # print(standings)
    for element in st:
        # output_line = element + (" " * (len(match.group(1))-len(element))) + "|  " + str(standings[element][0]) + " |  " + str(standings[element][1]) + " |  " + str(standings[element][2]) + " |  " + str(standings[element][3]) + " |  " + str(standings[element][4])
        output_line = f"{element[0] :30} |  {standings[element[0]][0]} |  {standings[element[0]][1]} |  {standings[element[0]][2]} |  {standings[element[0]][3]} |  {standings[element[0]][4]}"
        table.append(output_line)
    return table


# result = [
#     "Courageous Californians;Devastating Donkeys;win",
#     "Allegoric Alaskans;Blithering Badgers;win",
#     "Devastating Donkeys;Allegoric Alaskans;loss",
#     "Courageous Californians;Blithering Badgers;win",
#     "Blithering Badgers;Devastating Donkeys;draw",
#     "Allegoric Alaskans;Courageous Californians;draw",
# ]
# results = ["Blithering Badgers;Allegoric Alaskans;win"]
# esults = [
#     "Allegoric Alaskans;Blithering Badgers;win",
#     "Allegoric Alaskans;Blithering Badgers;win",
# ]
# print(tally(result))
# print(tally(results))
# print(tally(esults))
