import os


if not os.path.isdir("hi"):
    os.mkdir("hi")
else:
    print("already exists!")
