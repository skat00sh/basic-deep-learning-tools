import yaml

def load_config_from_yml(path: str):
    with open(path, 'r') as file:
        config_list = yaml.load(file, Loader=yaml.FullLoader)
    return config_list['config']

if __name__ == '__main__':
    load_config_from_yml('/home/skatoosh/project/fraunhofer/basic-deep-learning-tools/config.yml')