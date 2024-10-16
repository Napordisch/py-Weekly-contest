import sys

verticals = dict()

for line in sys.stdin:
    line = line.strip()
    if not line:
        break
    tree = list(map(int, line.split()))
    if tree[0] not in verticals.keys():
        verticals[tree[0]] = set()
    verticals[tree[0]].add(tree[1])

areas = set()

for vertical1 in verticals.keys():
    for vertical2 in verticals.keys():
        if vertical1 < vertical2:
            common_points = verticals[vertical1].intersection(verticals[vertical2])
            if len(common_points) >= 2:
                common_points = sorted(common_points)
            for item_index in range(len(common_points) - 1):
                areas.add((common_points[item_index + 1] - common_points[item_index]) * (vertical2 - vertical1))


if areas:
    print(min(areas))
else:
    print(0)