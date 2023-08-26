from pathlib import Path
from pprint import pprint
import zipfile

rootpath = Path("./")  # where we are

output_zip_dir = rootpath.joinpath("output_zips")


if not output_zip_dir.exists():
    output_zip_dir.mkdir()

individual_projects = rootpath.glob(
    "**/*.kicad_pro"
)  # all kicad project files in the repo

project_roots = [
    x.parents[0] for x in individual_projects
]  # get their root directory, since we can usually expect them to be in a consistent directory.

# print(project_roots)

projects = []

for p in project_roots:
    gerber_folder = (
        p / "gerbers"
    )  # what the hell, this works?  Guess they override the division symbol.  Wild!

    gerber_files = [gerber_folder.glob(filetype) for filetype in ["*.gbr*", "*.drl*"]]
    gerber_files = [item for sublist in gerber_files for item in sublist]

    projects.append({"gerbers": gerber_files, "project_name": p.name})


for p in projects:
    if p["gerbers"] != []:
        output_zip_loc = Path(f"./output_zips/{p['project_name']}.zip")
        if output_zip_loc.exists():
            output_zip_loc.unlink()
            print(f"Removed {p['project_name']} to create new release.")
        with zipfile.ZipFile(output_zip_loc, mode="w") as archive:
            for filename in p["gerbers"]:
                archive.write(filename)

            print(f"Wrote new ZIP of {p['project_name']}!")
    else:
        print(
            f"Could not cut release for {p['project_name']}, as there were no gerbers in the output directory."
        )

print("*** Done exporting! ***")
