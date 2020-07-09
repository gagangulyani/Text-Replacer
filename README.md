# Text Replacer

Replace Text in a text file with one command

## Script File

[text_replacer.py](text_replacer.py)

## Requirements

- Python 3.x.x

## Usage

### For replacing Text

```bash
python3 text_replacer.py <file_name.txt> <text_to_be_replaced> <replacement>
```

### For replacing Text with spaces

```bash
python3 text_replacer.py <file_name.txt> "<text_to_be_replaced>" "<replacement>"
```

### For removing Text with or without Spaces

```bash
python3 text_replacer.py <file_name.txt> "<text_to_be_removed>" ""
```

## Example

```bash
python3 text_replacer.py README.md @gagan_gulyani @GaganGulyani
```

## Note

- Use Inverted Comma (") or (') for replacing text with spaces
- You can use ex1.txt in Example folder for testing this script
