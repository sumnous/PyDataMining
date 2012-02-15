#!/usr/bin python
#encoding: utf-8

def user_install_record_to_dict(fobject,training=False):
    dict = {}

    for x in fobject:
        x = x[:-1].split('\t')
        if not dict.has_key(x[0]):
            dict[x[0]] = {}
        dict[x[0]][x[1]] = int(x[2])

    if training:
        import pickle
        with file('../inter_data/user_items_rating.dict','w') as f:
            pickle.dump(dict,f)
            
    return dict


if __name__ == '__main__':
    fobject = file('../input/user_install_record')

    print user_install_record_to_dict(fobject)
