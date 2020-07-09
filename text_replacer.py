'''
=============
Text Replacer : Replace Text in text file with one command
=============

[ USAGE ]

    + For replacing Text

        $ python3 text_replacer.py <file_name.txt> <text_to_be_replaced> <replacement>

    + For replacing Text with Spaces

        $ python3 text_replacer.py <file_name.txt> "<text_to_be_replaced>" "<replacement>"

    + For removing Text with or without spaces

        $ python3 text_replacer.py <file_name.txt> "<text_to_be_removed>" ""

    Note: Use Inverted Comma (") for replacing text with spaces

[ Example ]

        $ python3 text_replacer.py README.md @gagan_gulyani @GaganGulyani

=====================
Author: @GaganGulyani
=====================
'''

from sys import argv


def print_border(func):
    """
        This Decorator function prints a border above and below the
        function being passed.

        Args:
            func()                  Function

        Returns:
            None

        Output:
            Prints Border above and below the function being called
    """
    def wrap():
        print('=' * 40, end="\n\n")
        func()
        print('\n' + '=' * 40)

    return wrap


def replacer(file_name, text_to_be_replaced, replacement):
    """
        This function replaces Text in a text file

        Args:
            file_name:              File Name
            text_to_be_replaced:    Text to be Replaced
            replacement:            Replacement Text

        Returns:
            None

        Output:
            Displays the number of Texts Replaced replaced
    """
    with open(file_name, 'r+') as f:
        # Read the content of the file
        content = f.read()

        # Store Number of Texts to be replaced to display them at last
        old_count = content.count(text_to_be_replaced)

        # replace the Text to be replaced with replacement
        content = content.replace(text_to_be_replaced, replacement)

        # removes the content of the file
        f.seek(0) # Go to the beginning of the file
        f.truncate() # Remove the content of the file

        # writes the updated content to the file
        f.write(content)

        if old_count:
            print(old_count, 'Text(s) replaced Successfully!')
        else:
            print('Text Not Found! Please check the spelling and Try again.')


@print_border
def main():
    """
        This function executes the whole script

        Args:
            None

        Returns:
            None

        Output:
            Documentation of this script and the Execution Messages
    """

    # Number of Arguments
    num_args = len(argv)

    if num_args != 4:
        # Display Documentation of this Script File
        print(__doc__)

        # If all arguments aren't given
        print('=' * 15)
        print("[ Error ] Invalid Number of Arguments")
        print('=' * 15)
        exit()

    file_name = argv[1]  # Filename is at Second Index
    text_to_be_replaced = argv[2]  # Text to be replaced at Third Index
    replacement = argv[3]  # Replacement is at Forth Index

    # Call the replacer function
    replacer(file_name, text_to_be_replaced, replacement)


if __name__ == '__main__':
    main()
