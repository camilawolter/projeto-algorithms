from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(4, "teste")

    assert encrypt_message("teste", 4) == "e_tset"

    assert encrypt_message("teste", 3) == "set_et"

    assert encrypt_message("112", 0) == "211"
