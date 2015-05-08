#!/usr/bin/env python
import yaml
import pprint

with open('project.yaml') as f:
    x = yaml.load(f)
    pprint.pprint(x)

with open('project.requiredfields.yaml') as f:
    x = yaml.load(f)
    pprint.pprint(x)
