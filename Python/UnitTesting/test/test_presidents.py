import pytest
from president import President

@pytest.fixture
def george():
    george=President(1)
    return george

def test_checker():
    assert 1 == 1

def test_out_of_range():
    with pytest.raises(ValueError):
        president=President(250)

def test_for_george(george):
    assert george.first_name == "George"