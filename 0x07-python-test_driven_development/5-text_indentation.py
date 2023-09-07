#!/usr/bin/python3

def text_indentation(text):
    """
    Print the input text with two new lines after each '.', '?', and ':' characters.
    
    :param text: A string to be processed.
    :type text: str
    :raises TypeError: If the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    lines = text.split("\n")

    for line in lines:
        line = line.strip() 
        if line:  
            result = ""
            newline = True 

            for char in line:
                if char in ".?:":
                    result += char + "\n\n" 
                    newline = True
                elif char != ' ' and newline: 
                    result += char
                    newline = False
                elif char != ' ':
                    result += char

            print(result)

text = "This is a test. Another test? Yes: it works."
text_indentation(text)
