#
# 3DE4.script.name:	Soft clip toggle
#
# 3DE4.script.gui:	Main Window::Tools
# Author - https://t.me/vlad_osokin



if tde4.getIControlsEnabledFlag() == 1:
    tde4.setIControlsEnabledFlag(0)

current_cam = tde4.getCurrentCamera()
if current_cam is not None:
    current_softclip = tde4.getCamera8BitColorSoftclip(current_cam)
    new_softclip = 1 if current_softclip == 0 else 0
    tde4.setCamera8BitColorSoftclip(current_cam, new_softclip)
    print(f"Softclip for camera {current_cam} changed to {new_softclip}.")
else:
    print("No current camera selected.")
