import tomli #package 'tomli' is used to parse the 'config.toml' file

# define function to open in binary mode (with the "rb" flag) and parse TOML
def get_toml_data(path):
    """
    return config information as dict from a toml file

    :param path: configuration file path file
    :type path: str
    :return: config information
    :rtype: dict
    """

    with open(path, mode="rb") as fp:
        return tomli.load(fp)
