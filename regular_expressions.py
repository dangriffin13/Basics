

def regex_basic_email_validator(string):
    if re.match(r"[A-Za-z0-9_-]+@[A-Za-z0-9]+\.[a-zA-Z]{1,3}$", string):
        return True
    else:
        return False


def regex_password_validator(string):
    if re.match(r"[A-Za-z0-9]{8,}", string):
        return True
    else:
        return False

def regex_url_validator(string):
    pass


def regex_find_html_tag(string):
    pass


if __name__ == "__main__":
    print("Regular expression functions are available")