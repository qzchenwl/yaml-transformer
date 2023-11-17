# yaml-transformer

## Introduction

`yaml-transformer` is a powerful Python package designed to enhance YAML processing capabilities. It introduces advanced features like including other YAML files, executing JSONPath queries, applying JQ queries, and flattening lists within YAML files.

## Installation

To install `yaml-transformer`, run the following command:

```bash
pip install yaml-transformer
```

## Features
- `!include`: Include and merge other YAML files.
- `!jsonpath`: Perform JSONPath queries on YAML nodes.
- `!jq`: Apply JQ queries and modifications to YAML nodes.
- `!flatten`: Flatten nested lists into a single list.

## Usage

The `yaml-transformer` package enhances YAML processing with advanced features. Below are examples demonstrating its capabilities using a Transformers theme. These examples show how to include external YAML files, apply JSONPath queries, use JQ queries, and flatten lists, all within a YAML context.

### Including External YAML Files

#### Autobots YAML (autobots.yaml):

```yaml
- name: Optimus Prime
  role: Leader
- name: Bumblebee
  role: Scout
```

#### Decepticons YAML (decepticons.yaml):

```yaml
- name: Megatron
  role: Leader
- name: Starscream
  role: Fighter
```

#### Leaders YAML (leaders.yaml):

```yaml
autobots:
  - name: Optimus Prime
    role: Leader
```

#### Main YAML:

```yaml
autobots: &autobots !include autobots.yaml
decepticons: &decepticons !include decepticons.yaml
```

In this setup, `autobots.yaml` and `decepticons.yaml` are included and referenced in the main YAML file using YAML anchors (`&autobots` and `&decepticons`).

### Applying JQ Query

To find a specific Transformer leader (e.g., Optimus Prime) using JQ:

```yaml
leaders: &leaders !include leaders.yaml
leader: !jq { object: *leaders, filter: '[.autobots[] | select(.name == "Optimus Prime")]' }
```

This JQ query selects "Optimus Prime" from the included `leaders.yaml`.

### Combining JSONPath Queries with Flatten

Combining the names of all Transformers (both Autobots and Decepticons) into a single list:

```yaml
all_names: !flatten
  - !jsonpath { object: *autobots, path: '$[*].name', all: true }
  - !jsonpath { object: *decepticons, path: '$[*].name', all: true }
```

Here, `!jsonpath` queries are used to extract the names of all Autobots and Decepticons, and `!flatten` combines these names into a single list.

## Running Tests

To run tests, install the package with development dependencies:

```bash
pip install yaml-transformer[dev]
```

Then, execute the test suite using pytest:

```bash
pytest
```

## Contributing

Contributions to `yaml-transformer` are welcome!

## License
`yaml-transformer` is released under the [MIT License](LICENSE).
