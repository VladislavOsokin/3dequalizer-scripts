#
# 3DE4.script.name: Toggle 3d model render mode
# 3DE4.script.addlabel: Model render mode
# 3DE4.script.gui.button:	Lineup Controls:Polygons/Lines, align-bottom-right , 90 , 15

# 3DE4.script.gui: Main Window::Tools
# 3DE4.script.version: v1.0
#
# Internal comment:	v1.0 - initial
#
# Internal comment:	Author - Vladislav Osokin
#


import tde4

pg_list = tde4.getPGroupList()
pg = tde4.getCurrentPGroup()

rendering_modes = [(False, True, False), (False, False, True),]

for p_group in pg_list:
    tde4.setCurrentPGroup(p_group)
    mlist = tde4.get3DModelList(p_group, 1)

    for m in mlist:
        current_mode = tde4.get3DModelRenderingFlags(p_group, m)

        current_mode_index = rendering_modes.index(tuple(current_mode)) if tuple(current_mode) in rendering_modes else 3

        next_mode_index = (current_mode_index + 1) % len(rendering_modes)

        next_mode = rendering_modes[next_mode_index]

        tde4.set3DModelRenderingFlags(p_group, m, *next_mode)

tde4.setCurrentPGroup(pg)
