import yaml

global info_dic

generic_data = yaml.load(open("../properties.yml"))


def before_all(context):
    print("+++++++++hello+++++++++++")
    print(str(generic_data))


def before_feature(context, feature):
    if 'try' in feature.tags:
        print("--------------FEATURE TAGS------------------")
    if 'Test' in feature.name:
        print("--------------FEATURE NAME----------")


def before_step(context, step):
    print("STEP", step.name)
    print("STEP KEYWORD", step.keyword)
    print("STEP STATUS", step.status)


def after_all(context):
    print("+++++++++++++++finish++++++++++++++++++")
