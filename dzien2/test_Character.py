import pytest

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

def test_empty_name():
    with pytest.raises(InvalidCharacterNameError):
        create_character(name="",class_name="warrior")

def test_invalid_class():
    with pytest.raises(InvalidClassNameError):
        create_character(name="obiwan",class_name="mage")

