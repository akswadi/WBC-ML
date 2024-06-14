import yaml

data = {
    'train': 'dataset/images/train',
    'val': 'dataset/images/val',
    'test': 'dataset/images/test',  # Optional
    'nc': 1,
    'names': ['wbc']
}

with open('dataset/data.yaml', 'w') as file:
    yaml.dump(data, file, default_flow_style=False)