import requests

def main():
    
    while True:
        try:
            sum_height = int(input("Enter an integer: "))
            break
        except ValueError:
            print("Please enter an integer.")

    pairs = get_pair_player(sum_height)
    if not pairs:
        print('No matches found!!')
    else:
        print("Pairs found: \n\n" + "\n".join(pairs))


def get_pair_player(sum_height):
    url = "https://mach-eight.uc.r.appspot.com/"
    response = requests.get(url)
    data = response.json()
    players = data["values"]

    pairs = list()
    num_dict = dict()
    for player in players:
        p_name = get_name(player)
        h_in = int(player["h_in"])
        diff = sum_height - h_in

        player2 = None

        if diff in num_dict:
            player2 = num_dict[diff].pop(0)
            if len(num_dict[diff]) == 0:
                del num_dict[diff]

        if player2:
            pairs.append(get_pair(p_name, h_in, player2, diff))    
        
        add_player(h_in, p_name, num_dict)

    pairs.reverse()
    return pairs


def add_player(h_in, p_name, num_dict):
        if h_in not in num_dict:
            num_dict[h_in] = [p_name]
        else:
            if p_name not in num_dict[h_in]:
                num_dict[h_in].append(p_name)

def get_name(player):
    return player["first_name"] + " " + player["last_name"]
def get_pair(player1, h1, player2, h2):
    return "[" + player1 + "\t" + str(h1) + "\n" + player2 + "\t" + str(h2) + "]\n"


if __name__ == "__main__":
    main()


