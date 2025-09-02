'''
Notes: since bomb is (m x m) m being odd, there is a centre, which should land on LAND.
maximize damage: no. of 1s should more around the bomb matrix's centre.
'''

#BOMBARDING THE REGION

#given grid
grid = [
    [1,0,0,0,1],
    [1,0,1,1,1],
    [1,1,0,1,1],
    [1,0,1,1,0],
    [0,1,0,1,1]
]

n = len(grid)  # size of map (no.of rows)

# taking bomb size from user
m = int(input("Enter size of the bomb (odd number): "))

offset = m // 2  # how many steps is the centre away from the edges in the bomb square
max_damage = 0
best_coord = (0, 0)

# looping over all possible centers

for r in range(offset, n - offset):
    for c in range(offset, n - offset):
        if grid[r][c] == 1:  # since bomb only works if center is land
            damage = 0
            
            # calculating damage around center
            for i in range(r - offset, r + offset + 1):
                for j in range(c - offset, c + offset + 1):
                    if grid[i][j] == 1:
                        damage = damage + 1
            
            if damage > max_damage:
                max_damage = damage
                best_coord = (c, n - 1 - r)  # change to bottom-left (0,0) coord system

print("Maximum damage:", max_damage)
print("Best coordinates to drop bomb:", best_coord)