# TRAI SMS Template Replacer

Replace content in the TRAI SMS template with ease using this Python package. This library is designed to simplify the process of replacing placeholders in a TRAI SMS template with actual values. It's particularly useful for bulk SMS generation where you need to personalize messages based on dynamic data.

## Installation

You can install the `traisms` library using pip: 

```bash
pip install traisms
```

## Usage

To get started, import the library and create an instance of the `SMSTemplate` class:

```python
from traisms import SMSTemplate

template = 'Hi, %%|name^{"inputtype" : "text", "maxlength" : "8"}%% has checked out at %%|time^{"inputtype" : "number", "maxlength" : "6"}%% PM from %%|place^{"inputtype" : "text", "maxlength" : "64"}%%'
values = ["Alice", "2", "Taj Hotel"]

```

Then, simply replace the placeholders in the template with the provided values using the `replace` method:

```python
try:
    result = SMSTemplate.replace(template, values)
    print(result)
except Exception as e:
    print(e)
```

The `replace` method will return the updated template with the values substituted in place of the placeholders. If there are any validation errors, the library will raise relevant exceptions:

- **Invalid Template Error**: This error is raised if a placeholder in the template is not valid.

- **Invalid Number Found**: This error is raised if a placeholder expects a numeric value but a non-numeric value is provided.

- **Exceeded Max Length**: This error is raised if a placeholder value exceeds its specified maximum length.

Example Error Handling:

```python
# Output:
# Invalid Number Found: Can not replace "1233" expecting numeric value

# or

# Output:
# Exceeded Max Length: Can not replace "Alice" exceeding max length of 8
```

## Template Syntax

The template follows a specific syntax for placeholders, which are enclosed within double percentage signs (e.g., `%%`). Each placeholder should have the following format:

```
%%|name^{"inputtype" : "text", "maxlength" : "8"}%%
```

- `name`: Placeholder ID
- `{"inputtype" : "text", "maxlength" : "8"}`: Placeholder attributes (optional)

You can customize the placeholder attributes as needed.

## Features

- Easy replacement of placeholders in TRAI SMS templates.
- Support for dynamic values provided in a list.
- Customizable placeholder attributes for flexibility.
- Validation and error handling for template placeholders.
- Suitable for bulk SMS generation and personalization.

## License

This library is provided under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

## Contributions

Contributions and feedback are welcome! If you encounter any issues or have suggestions for improvements, please [open an issue](https://github.com/DeepakPant93/trai-sms-template-replacer/issues) or submit a pull request.

---

**Note**: This library is not affiliated with TRAI (Telecom Regulatory Authority of India) but is designed to assist in formatting SMS messages according to TRAI guidelines.

Happy SMS templating! 📱✉️
