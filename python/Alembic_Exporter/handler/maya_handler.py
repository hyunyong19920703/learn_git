import maya.cmds as cmds


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