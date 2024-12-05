'''
We are running a small business. We have a list of 
regions where our customers are ('North', 'South', 'East',
'West'), a dictionary containing how many packages need 
to be sent to each region (50, 30, 20, 40 respectively), 
and another list containing the profit made on each 
successful delivery in that region (5.00, 4.50, 6.00, 5.50 
respectively). The goal is to calculate our expected 
profit.
'''

regions = ['North', 'South', 'East','West']

packages = {
    'North': 50,
    'South': 30,
    'East': 20,
    'West': 40
}

profit_per_delivery = [5.00, 4.50, 6.00, 5.50]  # Can we improve this option?

expected_profit = 0

# 50 x 5.00
# packages['North'] * profit_per_delivery[0]
# packages['South'] * profit_per_delivery[1]

for idx, region in enumerate(regions):
    # first iteration: i = 0 and region = 'North'
    # second iteration: i = 1 and region = 'South'
    region_profit = packages[region] * profit_per_delivery[idx]

    expected_profit += region_profit

print(expected_profit)

# ------------- Improvement for above
regions = ["North", "South", "East", "West"]

packages_diction = {
    "North": 50,
    "South": 30,
    "East": 20,
    "West": 40
}

profit_per_delivery = {
    "North": 5.00,
    "South": 4.50,
    "East": 6.00,
    "West": 5.50
 }

expected_profit = 0

for region in regions:
    region_profit = packages_diction[region] * profit_per_delivery[region]

    expected_profit += region_profit

# -------------  Additional Fun example with better naming conventions 
fav_movies_list = ["Dancing with Wolves", "The Gift", "The Shack", "Blended", "Avatar"]

# Referenced https://pythonbasics.org/enumerate/ for enumerate command in Python
# We will loop over the list using the enumerate command

# movie_index_int is the index and movie_name_str is the movie name
for movie_index_int, movie_name_str in enumerate(fav_movies_list):
    print(f"Movie {movie_index_int + 1}\'s name : {movie_name_str}")
