import os
import shutil


working_dir = os.path.dirname(os.path.abspath(__file__))
client_settings = os.path.join(working_dir, "ClientSettings")

#path to the user folder
user_folder = os.path.expanduser("~")
#path to the roblox versions
roblox_pointer = os.path.join(user_folder, "AppData", "Local", "Roblox", "Versions")


for folder in os.listdir(roblox_pointer):
    roblox_folders = os.path.join(roblox_pointer, folder)
    roblox_fix = os.path.join(roblox_folders, "ClientSettings")

    if os.path.isdir(roblox_folders):
        if not os.path.exists(roblox_fix):
            shutil.copytree(client_settings, roblox_fix)
            print(f"copied to {roblox_fix}")
        else:
            print(f"skipped : {roblox_fix}")