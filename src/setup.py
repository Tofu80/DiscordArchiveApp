#!/usr/bin/env python3

token = input("Input your discord token here: ").strip()

with open("../.env", "w") as f:
    f.write(f"DISCORD_TOKEN={token}")

print("Token saved! You can now run explore.py")