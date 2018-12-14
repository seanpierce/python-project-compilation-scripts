import os

from colors import green, yellow, red

# secrets contains a list of Project objects
from secrets import projects

print(f'{green("Compile a Project!")}')

while True:
    print("--------------------")

    for project in projects:
        print(f'{yellow(f"[{project.number}]")} {project.name}')

    project_id = int(input("What project would you like to compile? "))

    selected_project = next(
        (x for x in projects if x.number == project_id), None)

    if selected_project == None:
        print(f'{red(f"Error: {project_id} is not an option.")}')
        continue

    print(f'{green(f"Compiling: {selected_project.name}...")}')
    os.chdir(selected_project.path)
    os.system(selected_project.command)
