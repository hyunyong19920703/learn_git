import maya.cmds as cmds


def get_cam_items():
    
    sll = cmds.ls(type='camera')
    
    row_datas = list()
    
    for slo in sll:
        name = slo
        cam_type = 'default_camera'
        
        data_dict = dict()
        data_dict['name'] = name
        data_dict['type'] = cam_type
        
        row_datas.append(data_dict)
    
    return row_datas