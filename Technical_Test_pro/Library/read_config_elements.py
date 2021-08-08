import configparser


def conf_ele_read(section, key):
    cnf = configparser.ConfigParser()
    cnf.read("../Config/config_element.cfg")
    return cnf.get(section,key)




