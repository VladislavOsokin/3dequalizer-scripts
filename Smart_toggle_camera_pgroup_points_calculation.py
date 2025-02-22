#
# 3DE4.script.name:	Smart toggle Camera/Pgroup/points calculation
#
# 3DE4.script.version:	v1.0
#
# 3DE4.script.gui:		Manual Tracking Controls::View
# 3DE4.script.gui:	Main Window::Shortcuts
#
# Internal comment:	v1.0 - initial
#
# Internal comment:	Author - Vlad Osokin
#

import tde4

def main():

    all_pgroups = tde4.getPGroupList()
    all_cameras = tde4.getCameraList()  
    
    if not all_pgroups and not all_cameras:
        tde4.postQuestionRequester(
            "Toggle PGroups, Points or Cameras",
            "There are no groups or cameras in the scene.",
            "OK"
        )
        return


    selected_pgroups = []
    if all_pgroups:
        for pg in all_pgroups:
            if tde4.getPGroupSelectionFlag(pg) == 1:
                selected_pgroups.append(pg)


    selected_points = []
    if all_pgroups:
        for pg in all_pgroups:
            pts = tde4.getPointList(pg, 1)
            if pts:
                for p in pts:
                    selected_points.append((pg, p))


    selected_cameras = []
    if all_cameras:
        for cam in all_cameras:
            if tde4.getCameraSelectionFlag(cam) == 1:
                selected_cameras.append(cam)


    if selected_points and selected_pgroups and selected_cameras:
        for (pg, p) in selected_points:
            tde4.setPointSelectionFlag(pg, p, 0)
        for pg in selected_pgroups:
            tde4.setPGroupSelectionFlag(pg, 0)
        for cam in selected_cameras:
            tde4.setCameraSelectionFlag(cam, 0)
        return


    if selected_points:
        for (pg, p) in selected_points:
            current_mode = tde4.getPointCalcMode(pg, p)
            if current_mode == "CALC_ACTIVE":
                tde4.setPointCalcMode(pg, p, "CALC_OFF")
                tde4.setPointColor2D(pg, p, 2)
            else:
                tde4.setPointCalcMode(pg, p, "CALC_ACTIVE")
                tde4.setPointColor2D(pg, p, 0)
    elif selected_cameras:
        for cam in selected_cameras:
            current_flag = tde4.getCameraEnabledFlag(cam)
            tde4.setCameraEnabledFlag(cam, 1 - current_flag)
    elif selected_pgroups:
        for pg in selected_pgroups:
            current_flag = tde4.getPGroupEnabledFlag(pg)
            tde4.setPGroupEnabledFlag(pg, 1 - current_flag)
    else:
        tde4.postQuestionRequester(
            "Toggle PGroups, Points or Cameras",
            "Neither groups, points nor cameras are selected.",
            "OK"
        )

main()
