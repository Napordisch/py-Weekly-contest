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
            for horizontal1 in common_points:
                for horizontal2 in common_points:
                    if horizontal1 < horizontal2:
                        areas.add((vertical2 - vertical1) * (horizontal2 - horizontal1))

if areas:
    print(min(areas))
else:
    print(0)