files = ["payload.exe", "notes.txt", "malware.zip", "readme.md"]
files.append("keylogger.py")
files[1] = "credentials.txt"
files.remove("readme.md")
files.insert(1, "hashdump.log")
print(files)

