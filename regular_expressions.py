

def regex_basic_email_validator(string):
    if re.match(r"^([A-Za-z0-9_\.-]+)@([A-Za-z0-9_\.-]+)\.([a-zA-Z]{2,6})$", string):
        return True
    else:
        return False


def regex_password_validator(string): #does not include special chars
    if re.match(r"^[A-Za-z0-9]{8,}$", string):
        return True
    else:
        return False

def regex_url_validator(string):
    if re.match(r"^[\\\:A-Za-z0-9_-]+\.[A-Za-z0-9]{2,3}", string):
        return True
    else:
        return False


def regex_phone_validator(phone_number): #American phone numbers
    if re.match(r'^\+?d{1,3}?[- .]?\(?(?:\d{2,3})\)?[- .]?\d\d\d[- .]?\d\d\d\d$')
        return True
    else:
        return False

def regex_find_html_tag(dom, tag):
    pattern = r"<" + re.escape(tag) +">"
    if re.match(pattern, dom):
        return re.search(pattern, dom)
    else:
        return False


if __name__ == "__main__":
    print("Regular expression functions are available")