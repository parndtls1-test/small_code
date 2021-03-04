# pytest
# pip install pytest

# begin with test_ or end with _test.py
import pytest

##def test_is_palindrome_empty_string():
##    assert is_palindrome("")
##
##def test_is_palindrome_single_character():
##    assert is_palindrome("a")
##
##def test_is_palindrome_mixed_casing():
##    assert is_palindrome("Bob")
# use parametrize instead

def is_palindrome(s):
    return s == s[::-1]

@pytest.mark.parametrize("palindrome", [
    "",
    "a",
    "Bob"
])
def test_is_palindrome(palindrome):
    assert is_palindrome(palindrome)
