import re


def email_parse(email_address):
    parsed = re.findall(r"(^\w\S+)@((\w+)\.(\w{2,}))$", email_address)
    if not parsed:
        raise ValueError(f"wrong email: {email_address}")
    return dict(zip(["username", "domain"], parsed[0]))


print(email_parse("afanas.lg2@gmail.com"))
