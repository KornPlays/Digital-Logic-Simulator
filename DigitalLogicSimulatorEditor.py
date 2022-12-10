import os
import json
while True:
    dir=os.getenv("APPDATA").replace("Roaming","LocalLow\\Sebastian Lague\\Digital Logic Sim\\SaveData")
    edit=input("Chip/Save (C/S):\n")
    if edit.lower()=="c":
        save=input("\nSave name:\n")
        dir=f"{dir}\\{save}"
        if not os.path.exists(dir):
            exit()
        option=input("\n\nDelete/Rename (D/R):\n")
        name=input("\nName:\n")
        if not os.path.exists(f"{dir}\\{name}"):
            exit()
        if option.lower()=="d":
            os.remove(f"{dir}\\{name}.txt")
            os.remove(f"{dir}\\WireLayout\\{name}.txt")
        elif option.lower()=="r":
            rename=input("\n\nRename:\n").upper()
            with open(f"{dir}\\{name}.txt", 'r+') as f:
                data=json.load(f)
                data['name']=rename
                f.seek(0)
                json.dump(data,f,indent=4)
                f.truncate()
            f.close()
            os.rename(f"{dir}\\{name}.txt",f"{dir}\\{rename}.txt")
            os.rename(f"{dir}\\WireLayout\\{name}.txt",f"{dir}\\WireLayout\\{rename}.txt")
    elif edit.lower()=="s":
        save=input("\nSave name:\n")
        if not os.path.exists(f"{dir}\\{save}"):
            exit()
        option=input("\nDelete/Rename (D/R):\n")
        if option.lower()=="d":
            os.remove(f"{dir}\\{save}")
        elif option.lower()=="r":
            rename=input("\nRename:\n")
            os.rename(f"{dir}\\{save}",f"{dir}\\{rename}")
    os.system('cls')