lookup = [
    # 1    2    3    4    5    6
    ['0', '1', '2', '3', '4', '5'], # 1
    ['1', '0', '6', '7', '8', '9'], # 2
    ['2', '6', 'A', 'B', 'C', 'D'], # 3
    ['3', '7', 'B', 'A', 'E', 'F'], # 4
    ['4', '8', 'C', 'E', 'C', 'D'], # 5
    ['5', '9', 'D', 'F', '6', 'E']  # 6
]

def die_to_hex(rolls):
    return [lookup[rolls[n] - 1][rolls[n+1] - 1] for n in range(0, len(rolls), 2)]
