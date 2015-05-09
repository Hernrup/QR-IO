import os, os.path, sys

def pip(cmd):
    def modcmd(arg):
        os.system(sys.executable+" "+sys.prefix+"/bin/"+arg)

    if not(os.path.exists(sys.prefix+"/bin/pip")):
        print("You need to install pip first.")
        modcmd(cmd)
