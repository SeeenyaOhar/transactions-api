import re


class Validator():
    def validate(self, obj) -> bool:
        pass


class EmailValidator(Validator):
    regex = re.compile(
        r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")

    def validate(self, obj: str) -> bool:
        assert re.fullmatch(self.regex, obj) is not None
        return obj


class NameValidator(Validator):
    regex = re.compile(
        r'^[A-Z][a-z]*$'
    )

    def validate(self, obj: str) -> bool:
        assert re.fullmatch(self.regex, obj) is not None
        return obj
