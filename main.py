
main_code = []

with open("main.persian","r",encoding="UTF-8") as f:
    main_code = f.read().split("\n")


for line in main_code:
    print("---  start")


    
    if "riazi(" in line :
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
            print(eval(line[first+len("riazi("):end]))


            

    print("---  finished")
