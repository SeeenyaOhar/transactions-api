import bcrypt


class BcryptManager:
    def __init__(self, rounds: int = 10):
        self.rounds = rounds

    def hash(self, password: str) -> str:
        return bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt(self.rounds)
        ).decode()

    def validate(self, validate_password: str, original_password: str) -> bool:
        return bcrypt.checkpw(validate_password.encode("utf-8"), original_password.encode("utf-8"))
