lines = open("projects3/travelers.csv").read().split("\n")
print(lines)
for line in lines:
    print(line.split())
for line in lines:
    if "Jeff" in line:
        print("Jeff: " + line)