import pytest
import yaml
from yaml_transformer import TransformerLoader


@pytest.fixture
def transformer_data():
    with open('testdata/transformers.yaml', 'r') as file:
        return yaml.load(file, Loader=TransformerLoader)


def test_transformer_loader(transformer_data):
    assert 'Optimus Prime' in [bot['name'] for bot in transformer_data['autobots']]
    assert 'Megatron' in [con['name'] for con in transformer_data['decepticons']]
    assert transformer_data['leader'][0]['name'] == 'Optimus Prime'
    assert 'Optimus Prime' in transformer_data['all_names']
    assert 'Megatron' in transformer_data['all_names']
