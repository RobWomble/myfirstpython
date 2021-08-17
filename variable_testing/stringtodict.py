"""
Author: Rob Womble
testing dict method
"""

sample_dict = {}
sample_string = str("sample_dict['first level'] = {};\
                     sample_dict['first level']\
                     ['second level'] = {};\
                     sample_dict['first level']\
                     ['second level']['third level'] = 'inner data'"
                   )

print(sample_string)

try:
    exec(sample_string)
except Exception:
    pass

print(sample_dict)
