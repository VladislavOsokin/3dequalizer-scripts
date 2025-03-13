#
# 3DE4.script.name: Toggle Hide/Show Selected (Points & Models)
# 3DE4.script.version: v1.0
# 3DE4.script.gui: Main Window::Shortcuts
# 3DE4.script.comment: Toggles hide or show state of selected points or 3D models.
#   If both are selected, asks the user which to hide/show.
# Author - https://t.me/vlad_osokin
#

def toggle_selected_points(pg):
    # Get selected points
    pl = tde4.getPointList(pg, 1)
    if pl is not None:
        for p in pl:
            hide_flag = tde4.getPointHideFlag(pg, p)
            tde4.setPointHideFlag(pg, p, 1 - hide_flag)


def toggle_selected_models_across_all_pgroups():
    pg_list = tde4.getPGroupList()
    current_pg = tde4.getCurrentPGroup()
    for p_group in pg_list:
        tde4.setCurrentPGroup(p_group)
        mlist = tde4.get3DModelList(p_group, 1) 
        if mlist:
            for m in mlist:
                visible_flag = tde4.get3DModelVisibleFlag(p_group, m)
                tde4.set3DModelVisibleFlag(p_group, m, 1 - visible_flag)
    tde4.setCurrentPGroup(current_pg)


# ------------------ Main Script Logic ------------------ #

pg = tde4.getCurrentPGroup()
if pg is None:
    tde4.postQuestionRequester(
        "Hide/Show Selected",
        "Error: There is no current Point Group.",
        "Ok"
    )
else:
    selected_points = tde4.getPointList(pg, 1)
    if selected_points is None:
        selected_points = []
    num_points = len(selected_points)


    pg_list = tde4.getPGroupList()
    all_selected_models = []
    for p_group in pg_list:
        mlist = tde4.get3DModelList(p_group, 1)
        if mlist:
            all_selected_models.extend(mlist)
    num_models = len(all_selected_models)

    if num_points > 0 and num_models == 0:
        toggle_selected_points(pg)

    elif num_points == 0 and num_models > 0:
        toggle_selected_models_across_all_pgroups()

    elif num_points > 0 and num_models > 0:
        answer = tde4.postQuestionRequester(
            "Hide/Show Selected",
            "You have selected Points AND 3D Models. What do you want to hide/show?",
            "Points", "Models", "Cancel"
        )
        if answer == 1:
            toggle_selected_points(pg)
        elif answer == 2:
            toggle_selected_models_across_all_pgroups()
        else:
            pass

    else:
        tde4.postQuestionRequester(
            "Hide/Show Selected",
            "No Points or 3D Models are currently selected.",
            "Ok"
        )
