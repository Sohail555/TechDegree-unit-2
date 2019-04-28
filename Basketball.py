from constants import PLAYERS, TEAMS


def basketball(PLAYERS):
    names = []
    for item in PLAYERS:
        output = ""

        for key, values in item.items():
            if key == "name":
                output += values
                names.append(output)
    return names


def display_stats(team_str, players_str):
    print("Team: " + team_str + " Stats:\n-------------------\n" + players_str)


def team_pathers(player_name_string):
    pathers = player_name_string[0:6]
    pathers_string = ", ".join(pathers)
    # print("Team: Pathers Stats:\n-------------------\n" + pathers_string)
    return pathers_string


def team_Bandits(player_name_string):
    bandits = player_name_string[6:12]
    bandits_string = ",".join(bandits)
    # print("Team: Bandits Stats:\n-------------------\n" + bandits_string)
    return bandits_string


def team_warriors(player_name_string):
    warriors = player_name_string[12:]
    warriors_string = ",".join(warriors)
    # print("Team: Warriors Stats:\n-------------------\n" + warriors_string)
    return warriors_string


def start():
    print("BASKETBALL TEAM STATS TOOL")
    print()
    print("---- MENU----")
    print("Here are your choices\n1) Display Team\n2) Quit\n")


if __name__ == '__main__':

    while True:
        start()
        menu_option = input("> ")

        if menu_option == "2":
            break

        select_team = input("Please Select the Team for the stats\n\n1) Panthers\n2) Bandits\n3) Warriors\n ")

        # Store list players.
        player_name_string = basketball(PLAYERS)

        if select_team == str(1):
            # Pass the list of players to get a comma separated string back.
            panthers_str = team_pathers(player_name_string)

            # Pass the comma separated string into function that knows how to print that string.
            display_stats("Panthers", panthers_str)
            continue
        elif select_team == str(2):
            bandits_str = team_Bandits(player_name_string)
            display_stats("Bandits", bandits_str)
            continue
        elif select_team == str(3):
            warriors_str = team_warriors(player_name_string)
            display_stats("Warriors", warriors_str)
            continue