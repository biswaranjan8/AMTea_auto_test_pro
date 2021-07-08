import configparser


def conf_ele_read(section, key):
    cnf = configparser.ConfigParser()
    cnf.read("C:\\Users\\Admin\\PycharmProjects\\data_driven_pom_excel\\Config\\sign_config.cfg")
    return cnf.get(section, key)


# print(conf_ele_read('section1','pass_by_name'))
