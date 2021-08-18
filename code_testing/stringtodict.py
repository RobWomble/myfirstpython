"""
Author: Rob Womble
testing dict method
"""

sample_dict = {}
sample_string_a = str("sample_dict['first level'] = {}; "
                     "sample_dict['first level']"
                     "['second level'] = {}; "
                     "sample_dict['first level']"
                     "['second level']['a'] = 'inner data'"
                   )

print(sample_string_a)

sample_string_b = str("sample_dict['first level'] = {}; "
                     "sample_dict['first level']"
                     "['second level'] = {}; "
                     "sample_dict['first level']"
                     "['second level']['b'] = 'inner data'"
                   )

print(sample_string_b)
try:
    exec(sample_string_a)
    exec(sample_string_b)
except Exception:
    pass

print(sample_dict)
print("\n", sample_dict['first level']['second level'].keys())
