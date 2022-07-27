import glob
import os
import shutil
dest = os.getenv("LOCALAPPDATA")+r"\Roblox\Versions\*\content\sounds\\" # Roblox ouch dir
list_ = glob.glob(dest)
for i in list_:
    shutil.copyfile(".\\ouch.ogg",os.path.relpath(i,os.getcwd())+"\\ouch.ogg") # copy file to game