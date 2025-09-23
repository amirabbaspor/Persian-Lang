
variable = {
    "abbas": "creator :-",
}
main_code = []


def getArg(line: str,func: str) -> str :
    start = line.index(func)
    length = len(func)
    founded = 0
    steps = 0
    finding = True
    while finding:
        # print(line)
        if (line[start+length+steps] == "("):
            founded += 1
        elif (line[start+length+steps] == ")"):
            if founded > 0 :
                founded -= 1
            else :
                finding = False
                return line[start+length:start+length+steps]
        steps += 1


with open("main.persian","r",encoding="UTF-8") as f:
    main_code = f.read().replace("\n","").split(";")


print("---  start")

for line in main_code:
    if line == "":
        continue

    

    
    while "riazi(" in line :
        first = line.index("riazi(")
        x_ = 0 
        founded = 0
        end : int = None
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
            line : str = line[0:first] + str(eval(line[first+len("riazi("):end])) + line[end+1:]


    while "$" in line :
        start = line.index("$") + 1
        if line[start-2] == "\\":
            line = line[0:start-2] + "<dollar>" + line[start:]
            print(line)
            continue
        steps = 0
        end = None
        while True:
            if line[start+steps] in [" ",")"]:
                end = start + steps
                break
            steps += 1
        var = line[start:end]
        line = line[0:start-1] + variable[var].strip("\"") + line[end:]



    if line.startswith("bechap("):
        line = line.replace("<dollar>","$")
        print(getArg(line,"bechap("))


    elif line.startswith("yadet bashe "):
        line_ = line[line.index("yadet bashe ")+len("yadet bashe "):]
        name = line_.split("=")[0][0:-1]
        value = line_.split("=")[1][1:]
        if (name.find(" ")) != -1:
            raise Exception("esm motegaier nabayd \" \" dashte bashad.")
        else :
            variable[name] = value
            

    
print("---  finished")
print(variable)
