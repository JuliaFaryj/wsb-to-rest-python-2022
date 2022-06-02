import pytest
from settings import testhelpers


@pytest.fixture(scope="session")
def create_branches():
    """"
    create two branches and delete them after
    """
    testhelpers.create_new_branch("test-branch")
    testhelpers.create_new_branch("test-branch1")
    yield
    testhelpers.delete_new_branch("test-branch")
    testhelpers.delete_new_branch("test-branch1")


@pytest.fixture(scope="session")
def create_branch():
    """"
    create one branch and delete it after
    """
    testhelpers.create_new_branch("test-branch")
    yield
    testhelpers.delete_new_branch("test-branch")


@pytest.fixture(scope="session")
def create_branch_no_delete():
    """"
    create a branch without deleting it after
    """
    testhelpers.create_new_branch("test-branch")
    yield


@pytest.fixture(scope="session")
def delete_branch():
    """"
    delete a branch after a test
    """
    yield
    testhelpers.delete_new_branch("test-branch")






