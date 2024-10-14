emails = []
input_file = open("input.txt", "r")

for line in input_file:
    emails += list(line.split())

unique_emails = set()

for address in emails:
    unique_address = address.replace(".", "")
    if "+" in unique_address:
        unique_address = unique_address[:unique_address.index("+")] + unique_address[unique_address.index("@"):]
    unique_emails.add(unique_address)

print(len(unique_emails))
