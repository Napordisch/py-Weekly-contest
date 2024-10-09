original_string = input()

sorted_sequence = sorted(set(map(int, original_string.split())))

sub_sequences = []
sub_sequence_start = sorted_sequence[0]

for i in range(len(sorted_sequence)):

    if i + 1 <= len(sorted_sequence) - 1:
        if sorted_sequence[i + 1] == sorted_sequence[i] + 1:
            continue

    if sub_sequence_start == sorted_sequence[i]:
        entry = sub_sequence_start
    else:
        entry = [sub_sequence_start, sorted_sequence[i]]
    
    sub_sequences.append(entry)
    if i + 1 <= len(sorted_sequence) - 1:
        sub_sequence_start = sorted_sequence[i + 1]

        
for item in sub_sequences:
    if type(item) is list:
        print(str(item[0]) + "->" + str(item[1]))
    else:
        print(item)