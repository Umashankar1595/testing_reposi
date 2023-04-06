import json
import pytest


@pytest.fixture(scope='module')
def config(request):
    with open('conf.json') as config_file:
        print("reading config")
        config = json.load(config_file)
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome', ]
    assert isinstance(config['implicit_wait'], int)
    assert config['testproject_projectname'] != ""
    assert config['value1'] != ""
    assert  config['name'] != ""
    return config


def test_config(config):
    print("Config done")
