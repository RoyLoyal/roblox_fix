import os
import shutil

# what is the dir of the partent dir of this file
working_dir = os.path.dirname(os.path.abspath(__file__))
# source of the client settings
client_settings = os.path.join(working_dir, "ClientSettings")

# path to the user folder
user_folder = os.path.expanduser("~")
# path to the roblox versions
roblox_pointer = os.path.join(user_folder, "AppData", "Local", "Roblox", "Versions")

# for every folder inside roblox folder
for folder in os.listdir(roblox_pointer):
    # create the path for every item inside the folder 
    roblox_folders = os.path.join(roblox_pointer, folder)

    # only select what is a dir
    if os.path.isdir(roblox_folders):
        # create how a path should look like after its done
        roblox_fix = os.path.join(roblox_folders, "ClientSettings")
        # if there is no path that looks like the roblox fix
        if not os.path.exists(roblox_fix):
            # copy client settings into a folder that uses the path of roblox fix
            shutil.copytree(client_settings, roblox_fix)
            # if the operation is successful print
            print(f"copied to {roblox_fix}")
        else:
            #if it already exists then print skip
            print(f"skipped : {roblox_fix}")