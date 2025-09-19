
main_code = []

with open("main.persian","r",encoding="UTF-8") as f:
    main_code = f.read().split("\n")


for line in main_code:

    if line.startswith("bechap"):
        print(line[len("bechap")+1:])
        