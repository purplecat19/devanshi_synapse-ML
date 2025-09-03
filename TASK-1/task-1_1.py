#Pikachu, I CHOOSE YOU!!

#given pokedex:
pokedex = {
    "Pikachu": ("Electric"),
    "Charizard": ("Fire", "Flying"),
    "Lapras": ("Water", "Ice"),
    "Machamp": ("Fighting",),
    "Mewtwo": ("Psychic", "Fighting"),
    "Hoopa": ("Psychic", "Ghost", "Dark"),
    "Lugia": ("Psychic", "Flying", "Water"),
    "Squirtle": ("Water",),
    "Gengar": ("Ghost", "Poison"),
    "Onix": ("Rock", "Ground")
}

def generate_combos(k, poke_list, start=0, current=None, result=None):     #start - to avoid repeating prev pokemons
    if current is None:
        current=[]
    if result is None:
        result=[]

    if len(current)==k:
        result.append(tuple(current))
        return result
    
    for i in range(start, len(poke_list)):
        current.append(poke_list[i])  
        generate_combos(k, poke_list, i+1, current, result)
        current.pop()           # go back

    return result

def find_strongest_team(pokedex):
    poke_list = list(pokedex.keys()) #convert names of pokedex dictionary to a list
    n = len(poke_list)

    for k in range(1, n+1):
        max_types = 0
        best_teams = []
        teams = generate_combos(k, poke_list)


        for combo in teams:
            type_set = set()   #a set to store uniwue values
            for poke in combo:
                type_set.update(pokedex[poke])
            count = len(type_set)

            if count > max_types:
                max_types = count
                best_teams = [combo]
            elif count == max_types:
                best_teams.append(combo)

        print(f"k={k}, Max types={max_types}")
        for team in best_teams:
            print(" -", team)
        print("-"*25)


if __name__ == "__main__":
    find_strongest_team(pokedex)