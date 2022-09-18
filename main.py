import glob
import os
import shutil
dest = os.getenv("LOCALAPPDATA")+r"\Roblox\Versions\*\content\sounds\\" # Roblox ouch dir
list_ = glob.glob(dest)
for i in list_:
    shutil.copyfile("ouch.ogg", os.path.relpath(i, os.path.dirname(os.path.realpath(__file__))) + "\\ouch.ogg") # copy file to game
    shutil.copyfile("ouch.ogg", os.path.relpath(i, os.path.dirname(os.path.realpath(__file__))) + "\\volume_slider.ogg") # also replace volume slider sound
