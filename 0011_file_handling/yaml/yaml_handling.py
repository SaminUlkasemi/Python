# ---------------------------------------------------------------------------- #
#                                 yaml handling                                #
# ---------------------------------------------------------------------------- #
# Ref: Learn YAML structure -> https://www.youtube.com/watch?v=0fbnyS_lHW4&ab_channel=VincentLab
# Ref: https://www.youtube.com/watch?v=nFl6EXfcvLI&ab_channel=NeuralNine
# Ref: https://pyyaml.org/wiki/PyYAMLDocumentation

import yaml
import os

print(os.chdir('0011_file_handling/yaml'))

with open("example.yaml", "r") as f:
    data = yaml.safe_load(f)
    
print(data)

myData = {
    "name" : "hasan",
    "age" : 25,
    "language" : ["Bangla", "English", "Malay"],
    "address" : {
        "city" : "Khulna",
        "ZIP" : 234,
        "Country" : "Bangladesh"
    }
}

with open("myyaml.yaml", "w") as f:
    yaml.dump(myData, f, default_flow_style=False)