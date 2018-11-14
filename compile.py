import os

from colors import green, yellow, red

# declare file paths
AvellaSourceB_path = r"C:\Sites\Avella-SourceB\Avella_SourceB\App"

print(f'{green("Get your compile on!")}')

while True:
    print("--------------------")
    print(f'{yellow("[1]")} Avella - SourceB')
    print(f'{yellow("[2]")} SonoraQuest')

    project = int(input("What project would you like to compile? "))

    if project == 1:
        print(f'{green("Compiling: Avella - SourceB...")}')
        os.chdir(AvellaSourceB_path)
        os.system("gulp")
        break
    elif project != 1:
        print(f'{red("That command is unavailable at this time.")}')
        continue
