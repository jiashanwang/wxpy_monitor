# 创建一个用于将对象转化成json(字典)的类,让每个模型继承这个方法

def to_json(obj):
    fields = obj.__dict__
    if "_sa_instance_state" in fields:
        del fields["_sa_instance_state"]

    return fields

def cls_to_dict(cls_list):
    '''
    将数据库查询出来的实例对象列表进行统一的转换
    :param cls_list: 待转换的class 实例对象列表
    :return: 字典列表
    '''
    dict_list = []
    for item in cls_list:
        dict_list.append(item.to_json())
    return dict_list
