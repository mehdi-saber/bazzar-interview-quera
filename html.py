import re


def html():
    in_str = input()
    out_str = []
    tags = []
    i = 0
    tags_re = re.compile("^<(|/)((?:down)|(?:up))>")
    while i < len(in_str):
        char = in_str[i]
        if char == '<':
            tag_match = tags_re.findall(in_str[i:i+10])[0]
            is_start = tag_match[0] != "/"
            tag = tag_match[1]
            if is_start:
                tags.append(tag)
            else:
                if len(tags) <= 0:
                    return None
                if tags[-1] != tag:
                    return None
                tags.pop()
            i += len(tag) + 2 + (0 if is_start else 1)
        else:
            if len(tags) > 0:
                if tags[-1] == 'up':
                    out_str.append(str.upper(char))
                elif tags[-1] == 'down':
                    out_str.append(str.lower(char))
            else:
                out_str.append(char)
            i += 1
    if len(tags) > 0:
        return None
    else:
        return ''.join(out_str)


if __name__ == '__main__':
    result = html()
    if result:
        print("Valid")
        print(result)
    else:
        print("Invalid")