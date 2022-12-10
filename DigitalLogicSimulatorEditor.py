import os
import json
while True:
    dir=os.getenv("APPDATA").replace("Roaming","LocalLow\\Sebastian Lague\\Digital Logic Sim\\SaveData")
    edit=input("Chip/Save (C/S):\n").lower()
    #
    # Chip Editor
    #
    if edit.lower()=="c":
        save=input("\nSave name:\n")
        dir=f"{dir}\\{save}"
        if not os.path.exists(dir):
            exit()
        way=input("Chip Manager/Text Manager (C/T):\n").lower()
        chip=input("\nChip name:\n")
        if not os.path.exists(f"{dir}\\{chip}"):
            exit()
        # Chip Manager
        if way=="c":
            option=input("\n\nDelete/Recolour (D/R):\n").lower()
            if option=="d":
                os.remove(f"{dir}\\{chip}.txt")
                os.remove(f"{dir}\\WireLayout\\{chip}.txt")
            elif option=="r":
                color=input("Please enter a RGB value (0-255) seperated by ,'s\n").split(",")
                with open(f"{dir}\\{chip}.txt","r+") as f:
                    data = json.load(f)
                    data['colour']['r'] = int(color[0])/255
                    data['colour']['g'] = int(color[1])/255
                    data['colour']['b'] = int(color[2])/255
                    f.seek(0)
                    json.dump(data,f,indent=4)
                    f.truncate()
                f.close()
        # Text Manager
        elif way=="t":
            option=input("\n\nRename/Text Colour (R/T):\n").lower()
            if option=="r":
                rename=input("\n\nRename:\n").upper()
                with open(f"{dir}\\{chip}.txt", 'r+') as f:
                    data=json.load(f)
                    data['name']=rename
                    f.seek(0)
                    json.dump(data,f,indent=4)
                    f.truncate()
                f.close()
                os.rename(f"{dir}\\{chip}.txt",f"{dir}\\{rename}.txt")
                os.rename(f"{dir}\\WireLayout\\{chip}.txt",f"{dir}\\WireLayout\\{rename}.txt")
            elif option=="t":
                color=input("Please enter a RGB value (0-255) seperated by ,'s\n").split(",")
                with open(dir+"\\"+chip.upper()+".txt","r+") as f:
                    data = json.load(f)
                    data['nameColour']['r'] = int(color[0])/255
                    data['nameColour']['g'] = int(color[1])/255
                    data['nameColour']['b'] = int(color[2])/255
                    f.seek(0)
                    json.dump(data,f,indent=4)
                    f.truncate()
                f.close()
    #
    # Save Editor
    #
    elif edit=="s":
        save=input("\nSave name:\n")
        if not os.path.exists(f"{dir}\\{save}"):
            exit()
        option=input("\nDelete/Rename (D/R):\n").lower()
        if option=="d":
            os.remove(f"{dir}\\{save}")
        elif option=="r":
            rename=input("\nRename:\n")
            os.rename(f"{dir}\\{save}",f"{dir}\\{rename}")
    os.system('cls')
