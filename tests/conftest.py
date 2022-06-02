import pytest
from settings import testhelpers
import json


@pytest.fixture(scope="session")
def create_branch():
    testhelpers.create_new_branch()
    testhelpers.create_new_branch1()
    yield
    testhelpers.delete_new_branch()
    testhelpers.delete_test_branch1()







