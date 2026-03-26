with open("myfile.txt", "a") as f:
    f.write("\nNew content")
with open("myfile.txt") as f:
    print(f.read())