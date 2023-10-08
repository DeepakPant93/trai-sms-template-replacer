"""
# traisms

Author: Deepak Pant<deepak.93p@gmail.com>

## Description

This module provides functionality for replacing TRAI SMS template placeholders with actual values. It enables you to format SMS messages according to the Telecom Regulatory Authority of India (TRAI) guidelines.

## Usage

To use this module, follow these steps:

1. Import the module:

   ```python
   import traisms
   ```
"""


import re


class SMSTemplate:
    def replace(template, values):
        """
            Replaces the placeholders inside a given SMS template with corresponding values.

            Parameters:
            - template (str): The SMS template string containing placeholders inside %%
            - values (list): A list of values to replace the placeholders in the template

            Returns:
            - str: The modified SMS template with placeholders replaced by corresponding values
    """
        # Define a regular expression pattern to match the placeholders inside %%
        pattern = r'%%(.*?)%%'

        # Find all matches of the pattern in the template
        matches = re.findall(pattern, template)
        counter = 0

        # Iterate through the matches and replace each %% %% with numbering
        for match in matches:
            if '{' in match and match.endswith('}'):

                data = eval(match[match.find('{'):])
                value = values[counter]

                input_type = data.get('inputtype', 'text')
                max_length = data.get('maxlength', '0')

                # Check the max length of the input value
                if len(value) > int(max_length):
                    raise Exception(
                        f'Can not replace {value} exceeding max length of {max_length}')

                # Check the input type of the input value ̰
                if 'number' == input_type and not value.isdigit():
                    raise Exception(
                        f'Can not replace {value} expecting numeric value')

                template = template.replace(f'%%{match}%%', value, 1)
            else:
                raise Exception(
                    f'Can not replace {match} as it is not a valid template')
            counter += 1

        return template
