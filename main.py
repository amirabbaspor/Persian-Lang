
main_code = []

with open("main.persian","r",encoding="UTF-8") as f:
    main_code = f.read().split("\n")


for line in main_code:
    print("---  start")


    
    while "riazi(" in line :
        first = line.index("riazi(")
        x_ = 0 
        founded = 0
        end = None
        while True:
            if line[first+len("riazi(")+x_] == "(":
                founded = founded + 1
            elif line[first+len("riazi(")+x_] == ")":
                if founded > 0:
                    founded = founded - 1
                else :
                    end = first + len("riazi(") + x_
                    break
            x_ += 1
        
        if end != None :
            line = line[0:first] + str(eval(line[first+len("riazi("):end])) + line[end+1:]





    if line.startswith("bechap"):
        print(line[len("bechap"):])

            

    print("---  finished")
