#
# 3DE4.script.name:	Gamma toggle
#
# 3DE4.script.gui:	Main Window::Tools
# Author - https://t.me/vlad_osokin

if tde4.getIControlsEnabledFlag() == 1:
    tde4.setIControlsEnabledFlag(0)


gamma_values = [1, 1.8, 2.2, 2.4, 2.6]

current_cam = tde4.getCurrentCamera()
if current_cam is not None:
    current_gamma = tde4.getCamera8BitColorGamma(current_cam)


    if current_gamma in gamma_values:
        current_index = gamma_values.index(current_gamma)
    else:
        current_index = -1  


    new_index = (current_index + 1) % len(gamma_values)
    new_gamma = gamma_values[new_index]

    tde4.setCamera8BitColorGamma(current_cam, new_gamma)
    print(f"Gamma for camera {current_cam} changed to {new_gamma}.")
else:
    print("There is no currently selected camera.")
