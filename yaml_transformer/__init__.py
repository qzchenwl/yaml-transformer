import os
from os.path import join, abspath
from typing import Any

import jq
import requests
import yaml
from jsonpath_ng.ext import parse


class TransformerLoader(yaml.SafeLoader):
    def __init__(self, stream):
        super().__init__(stream)
        self.deep_construct = True
        try:
            self._root = os.path.split(stream.name)[0]
        except AttributeError:
            self._root = os.path.curdir


def construct_include(loader: TransformerLoader, node: yaml.ScalarNode) -> Any:
    path = loader.construct_scalar(node)
    if path.startswith('http://') or path.startswith('https://'):
        content = requests.get(path).text
    else:
        with open(abspath(join(loader._root, path))) as f:
            content = f.read()
    return yaml.load(content, TransformerLoader)


def construct_jsonpath(loader: yaml.Loader, node: yaml.MappingNode) -> Any:
    params = loader.construct_mapping(node)
    object = params['object']
    path = params['path']
    all = params.get('all', False)
    if all:
        value = [match.value for match in parse(path).find(object)]
    else:
        value = parse(path).find(object)[0].value
    return value


def construct_jq(loader: yaml.Loader, node: yaml.MappingNode) -> Any:
    params = loader.construct_mapping(node)
    object = params['object']
    filter = params['filter']
    all = params.get('all', False)
    if all:
        value = jq.all(filter, object)
    else:
        value = jq.first(filter, object)
    return value


def construct_flatten(loader: yaml.Loader, node: yaml.SequenceNode) -> Any:
    result = []
    value = loader.construct_sequence(node)
    for item in value:
        result.extend(item)
    return result


TransformerLoader.add_constructor('!include', construct_include)
TransformerLoader.add_constructor('!jsonpath', construct_jsonpath)
TransformerLoader.add_constructor('!jq', construct_jq)
TransformerLoader.add_constructor('!flatten', construct_flatten)
