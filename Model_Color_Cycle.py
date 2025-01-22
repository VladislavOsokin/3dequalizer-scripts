# 3DE4.script.name:    Model Color Cycle
# 3DE4.script.version: v1
# 3DE4.script.gui.button:	Lineup Controls:Model Color Cycle, align-bottom-right , 80 , 15

# Internal comment:	v1.0 - initial
#
# Internal comment:	Author - Vladislav Osokin
import tde4

colors = [
    [1.0, 0.0, 0.0],  
    [0.0, 1.0, 0.0],  
    [0.0, 0.0, 1.0],  
    [1.0, 1.0, 0.0],  
    [1.0, 0.0, 1.0],  
    [0.0, 1.0, 1.0],  
    [1.0, 1.0, 1.0]   
]

def change_model_colors():
    pg_list = tde4.getPGroupList()
    pg = tde4.getCurrentPGroup()

    for p_group in pg_list:
        tde4.setCurrentPGroup(p_group)
        mlist = tde4.get3DModelList(p_group, 1)

        for m in mlist:
            if tde4.get3DModelSelectionFlag(p_group, m):
                current_color = tde4.get3DModelColor(p_group, m)
                
                current_color_rgb = current_color[:3]
                try:
                    current_color_index = colors.index(current_color_rgb)
                except ValueError:
                    current_color_index = -1
                
                next_color_index = (current_color_index + 1) % len(colors)
                new_color_rgb = colors[next_color_index]
                
                new_color = new_color_rgb + [current_color[3]]
                tde4.set3DModelColor(p_group, m, new_color[0], new_color[1], new_color[2], new_color[3])

    tde4.setCurrentPGroup(pg)

change_model_colors()
