import glob

read_files = glob.glob("*.py")

with open("result.py", "w") as outfile:
    for f in read_files:
        with open(f, "r") as infile:
            outfile.write("## " + f + ":\n")
            outfile.write(infile.read())
            outfile.write("\n")
