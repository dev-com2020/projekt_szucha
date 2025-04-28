class InvalidCharacterNameError(Exception):
    pass

class InvalidClassNameError(Exception):
    pass

class Character:
    pass

VALID_CLASSES = ['warrior','sorcerer']

def create_character(name: str, class_name: str) -> Character:

    if not name:
        raise InvalidCharacterNameError("brak imienia!")
    if class_name not in VALID_CLASSES:
        msg = f"Nieprawidłowa klasa: {class_name}"
        raise InvalidClassNameError
