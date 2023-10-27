def get_platform():
    import platform
    sys_platform = platform.platform().lower()
    if "windows" in sys_platform:
        return "windows";
    elif "macos" in sys_platform:
        return "macos";
    elif "linux" in sys_platform:
        return "linux";
    else:
        print("other systemC")

if get_platform() == "windows":
    import ColorHelper_Win
else:
    import ColorHelper_Mac
 
#green
def printGreen(mess):
    if get_platform() == "windows":
        ColorHelper_Win.printGreen(mess);
    else:
        ColorHelper_Mac.printGreen(mess);

#red
def printRed(mess):
    if get_platform() == "windows":
        ColorHelper_Win.printRed(mess);
    else:
        ColorHelper_Mac.printRed(mess);

  
#yellow
def printYellow(mess):
    if get_platform() == "windows":
        ColorHelper_Win.printYellow(mess);
    else:
        ColorHelper_Mac.printYellow(mess);


