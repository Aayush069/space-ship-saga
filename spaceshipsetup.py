import cx_Freeze
import sys
base = None
if sys.platform == "win32":
    base = "WIN32GUI"
shortcut_table = [
    ("DesktopShortcut",
    "DekstopFolder",
    "Iron Gauntlet",
    "TARGETDIR",
    "[TARGETDIR]\SpaceShipSaga.exe",
    None,
    None,
    None,
    None,
    None,
    "TARGETDIR",
    )
]
msi_data = {"Shortcut": shortcut_table}

bdist_msi_options = {'data': msi_data}

executables = [cx_Freeze.Executable(script="SpaceShipSaga.py", icon='iconspace.ico',base=base)]

cx_Freeze.setup(
    version="1.0",
    descroption="SPACESHIP GAME",
    author="Baaghi:-)",
    name="SpaceShipSaga",
    options={"build.exe":{"packages":["pygame"], "include files":['iconspace.ico','Grenade+1.mp3','Gun+Silencer.mp3','space.png','spaceship_red.png','spaceship_yellow.png']},
             "bdist.msi": bdist_msi_options,
             },
    executables = executables

    )


