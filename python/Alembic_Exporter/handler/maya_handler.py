import maya.cmds as cmds
import os, sys

from pprint import pprint

def shape_deform():
    shapedeform = cmds.ls("*ShapeDeformed")
    delSD = []
    for i in shapedeform:
        delSD.append(i.replace("ShapeDeformed", "Shape"))
    for i in range(len(shapedeform)):
        cmds.rename(shapedeform[i], delSD[i])
        print(f"renamed {shapedeform[i]} --> {delSD[i]}")

def config_maya_setting():
    cmds.loadPlugin('AbcExport.so')
    cmds.loadPlugin('atomImportExport.so')
    
    data_dict = dict()
    data_dict['current_scene'] = cmds.file(q=True, sn=True)
    data_dict['file_name'] = cmds.file(q=True, sn=True, shn=True)
    data_dict['row_name'], data_dict['extension'] = os.path.splitext(data_dict['file_name'])
    data_dict['alembic_output_dir_path'] = None
    data_dict['atom_output_dir_path'] = None
    data_dict['hostname'] = os.environ['USERNAME']
    
    if 'scenes' in data_dict['current_scene']:
        data_dict['alembic_output_dir_path'] = os.path.join(data_dict['current_scene'].split("scenes")[0], "alembic")
        data_dict['atom_output_dir_path'] = os.path.join(data_dict['current_scene'].split("scenes")[0], "data", 'atom')
    
    data_dict['frame_range'] = [int(cmds.playbackOptions(q=True, min=True)), int(cmds.playbackOptions(q=True, max=True))]
    data_dict['step'] = 1.00
    data_dict['blur_step'] = 0.25    
    data_dict['pre_roll'] = 5
    data_dict['post_roll'] = 3
    data_dict['start_frame'] = int(data_dict['frame_range'][0])
    data_dict['end_frame'] = int(data_dict['frame_range'][1])
    data_dict['alembic_option'] = "-uvWrite -writeUVSets -eulerFilter -worldSpace -writeVisibility"
    data_dict['priority'] = 100
    
    
    
    return data_dict     

def get_asset_model_from_current_scene():
    
    suffixes = ['__GEO', '__BLUR']
    atom_SET_name = "AniControlSet"
    
    def eth_num_sort(eth):
        """Split an ethernet device name between text and digit groups as int,
        allowing consistent sorting of interfaces.
        Usage: `sorted(if_list, key=ethkey)`
        get from: https://stackoverflow.com/questions/12658512/python-sorted-by-name
        :param eth: Value to sort
        :type eth: str
        :return: List of str's (even indexes) and int's (odd indexes) to compare
        :rtype: list
        """
        keys = []
        if not eth:
            # If eth is a string it's empty, just return blank list
            return keys
        # Start with the first character already in last
        last, eth = eth[0], eth[1:]
        # If last is int we start at offset 1
        if last.isdigit():
            keys.append('')
        for i in eth:
            if i.isdigit() is last.isdigit():
                # Keep accumulating same type chars
                last += i
            else:
                # Save and restart next round
                keys.append(int(last) if last.isdigit() else last)
                last = i
        # Save final round and return
        keys.append(int(last) if last.isdigit() else last)
        return keys    

    sel_list = cmds.ls("*__GEO", "*:*__GEO", "*__BLUR", "*:*__BLUR", tr=True)
    sel_list += cmds.ls(atom_SET_name, f"*:{atom_SET_name}", type='objectSet')

    selected_list = sel_list
    key_list = sorted(list(set([sel.split(":")[0] for sel in selected_list if ":" in sel and "__" in sel])))
    key_list.sort(key=eth_num_sort)

    tree_dict = {}
    for key in key_list:
        list_value = []
        for sel in selected_list:
            if sel.startswith(key + ":") and "__" in sel:
                list_value.append(sel)
            elif sel.startswith(key + ":") and cmds.objectType(sel, isType="objectSet") is True:
                list_value.append(sel)
        tree_dict[key] = list_value
        
    return tree_dict


def get_atom_full_path(selected_item, info_dict):
    
    check_is_set = cmds.objectType(selected_item, isType="objectSet")

    sel = selected_item
    if "|" in sel:
        sel = sel.rsplit("|", 1)[1]

    if ":" in sel:
        sel_r = sel.replace(":", "_")
        atom_name = sel_r + ".atom"

    else:
        atom_name = sel + ".abc"

    atom_output_folder = os.path.join(info_dict['atom_output_dir_path'], info_dict['row_name'])
    atom_full_path = os.path.join(atom_output_folder, atom_name)
    if os.path.exists(atom_output_folder) is False:
        os.makedirs(atom_output_folder)

    return atom_full_path

def get_alembic_full_path(selected_item, info_dict):
    
    sel = selected_item
    if "|" in sel:
        sel = sel.rsplit("|", 1)[1]

    if ":" in sel:
        sel_r = sel.replace(":", "_")
        abc_name = sel_r + ".abc"

    else:
        abc_name = sel + ".abc"

    alembic_output_folder = os.path.join(info_dict['alembic_output_dir_path'], info_dict['row_name'])
    alembic_full_path = os.path.join(alembic_output_folder, abc_name)
    if os.path.exists(alembic_output_folder) is False:
        os.makedirs(alembic_output_folder)

    return alembic_full_path

def make_item_dict(selected_obj, info_dict):
    """_summary_

    Args:
        selected_obj (str): export target object
        info_dict (_type_): curent scene info dict

    Returns:
        _type_: export alembic command dict
    """
    
    
    step = info_dict['step']
    sel_long = cmds.ls(selected_obj, long=1)[0]
    check_is_set = cmds.objectType(sel_long, isType="objectSet")
    if check_is_set is True:
        cache_type = "atom"
        alembic_full_path = None
        atom_full_path = get_atom_full_path(selected_obj, info_dict)
    else:
        cache_type = "alembic"
        sel_long = cmds.ls(sel_long, tr=1, long=1)[0]
        alembic_full_path = get_alembic_full_path(selected_obj, info_dict)
        atom_full_path = None        
        if "__BLUR" in selected_obj:
            step = info_dict['blur_step']

    item_dict = {"cache_type": cache_type,
                "start_frame": info_dict['start_frame'],
                "end_frame": info_dict['end_frame'],
                "step": step,
                "alembic_option": info_dict['alembic_option'],
                "sel_long": sel_long,
                "alembic_full_path": alembic_full_path,
                "atom_full_path": atom_full_path,
                # "version_num": self.version_num,

                # "project_name": self.project_name,
                "hostname": info_dict['hostname'],
                # "priority": self.priority,
                # "service_key": self.service_key,
                "current_scene_path": info_dict['current_scene'],
                # "tmp_current_scene_path": self.tmp_current_scene_path,
                # "pub_scene_path": self.pub_scene_path,
                # "service_color": self.service_color,
                "raw_name": info_dict['raw_name'],
                # "mov_version": self.sel_mov_version,
                # "description": self.rig_version_description_add(selected_obj),
                # "thumbnail": self.thumbnail,
                # "emails": self.emails,
                # "sender": self.sender,
                # "sgtk_context": self.get_sgtk_context_dict()
                }
    return item_dict