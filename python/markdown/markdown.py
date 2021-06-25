import re

def heading_parse(line:str):
    numberOfHash = 0 # keeps a count of the number of hashes at the beginning of a line
    # # # The following `For` loop counts the number of hashes at the beginning of the `line`.
    # # # if we have any character other than space following the hashes we turn the line into a regular paragraph
    # # # Eg: '###2## Line' --> '<p>###2## Line</p>'
    edit = parse_bold_once(parse_italics_once(line))
    for char in line:
        if char == '#':
            numberOfHash += 1
        elif char.isspace():
            break
        else:
            return f"<p>{edit}</p>"
    if numberOfHash < 6:  # if we have less than 6 hashes it is turned into the appropriate heading level
        return f"<h{numberOfHash}>{edit[numberOfHash+1:]}</h{numberOfHash}>"
    else: # if we have greater than equals 6 hashes it is turned into heading level 6
        return f"<h6>{line[numberOfHash+1:]}</h6>"

def unordered_list_parser(line:str, in_list:bool):
    line = parse_bold_once(line)
    line = parse_italics_once(line)
    if not in_list:
        return f"<ul><li>{line}</li>", True
    else:
        return f"<li>{line}</li>", True

def parse_bold_once(line:str):
    match = re.match('(.*)__(.*)__(.*)', line)
    if match:
        return f"{match.group(1)}<strong>{match.group(2)}</strong>{match.group(3)}"
    else:
        return line


def parse_italics_once(line: str):
    match = re.match('(.*)_(.*)_(.*)', line)
    if match:
        return f"{match.group(1)}<em>{match.group(2)}</em>{match.group(3)}"
    else:
        return line

def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    # in_list_append = False
    for i in lines:
        # if re.match('###### (.*)', i) is not None:
        #     i = '<h6>' + i[7:] + '</h6>'
        # elif re.match('## (.*)', i) is not None:
        #     i = '<h2>' + i[3:] + '</h2>'
        # elif re.match('# (.*)', i) is not None:
        #     i = '<h1>' + i[2:] + '</h1>'
        # # # replace the above code with heading_parser
        if i.startswith('#'):
            i = heading_parse(i)
            if in_list:
                i = f"</ul>{i}"
                in_list = False
        elif bool(re.match(r'\* (.*)', i)):
            # # # the re.match here checks `i` for starting with '*' followed by any space character (other than newline)
            i, in_list = unordered_list_parser(
                re.match(r'\* (.*)', i).group(1), in_list)
        else:
            i = parse_bold_once(i)
            i = parse_italics_once(i)
            i = f"<p>{i}</p>"
            if in_list:
                i = f"</ul>{i}"
                in_list = False
        res += i
    if in_list:
        res += '</ul>'
    return res
