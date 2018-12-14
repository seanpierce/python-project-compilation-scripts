# Python Project Compilation Scripts

A simple Python app that I use to compile my front-end projects at work.

### Usage

-   Rename the `secrets.example.py` file to `secrets.py`
-   Replace the placeholder info with actual info relevant to your projects
-   From the repo's root, run `$ python compile.py`

### Optional

It's helpful to create a shell alias that points toward the `compile.py` file.
Append the alias to your `.bashrc` file by running `$ echo "alias compile=\"cd path/to/compile.py && python compile.py\"" >> ~/.bashrc`.
Restart your shell. Now, running `$ compile` from anywhere will run this program!
