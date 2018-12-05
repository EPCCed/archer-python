
"""A function to remove full stops and commas"""

def remove_punctuation(line):

    """Return a copy of line without full stops or commas"""

    newline = []

    for word in line.split():
        stripped = word.strip('.').strip(',')
        newline.append(stripped)


    return " ".join(newline)
