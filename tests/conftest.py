import pytest
from settings import testhelpers


@pytest.fixture(scope="session")
def branch_sha():
    """"
    get branch sha for creating a branch tests
    """
    yield testhelpers.get_branch_sha()


@pytest.fixture(scope="session")
def create_branch():
    """"
    create one branch and delete it after
    """
    testhelpers.create_new_branch("test-branch")
    yield
    testhelpers.delete_new_branch("test-branch")


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
def create_branch_delete_all():
    """"
    create a branch then delete protection rule then delete the branch
    """
    testhelpers.create_new_branch("test-branch")
    yield
    testhelpers.delete_branch_protection("test-branch")
    testhelpers.delete_new_branch("test-branch")


@pytest.fixture(scope="session")
def update_protection():
    """"
    add and update branch protection rule and delete branch
    """
    testhelpers.create_new_branch("test-branch")
    testhelpers.update_branch_protection("test-branch")
    yield
    testhelpers.delete_new_branch("test-branch")


@pytest.fixture(scope="session")
def update_protection_delete_all():
    """"
    add and update branch protection rule and delete branch
    """
    testhelpers.create_new_branch("test-branch")
    testhelpers.update_branch_protection("test-branch")
    yield
    testhelpers.delete_branch_protection("test-branch")
    testhelpers.delete_new_branch("test-branch")


@pytest.fixture(scope="session")
def signatures_protection_create():
    """"
    add and update branch protection rule then delete protection rule and the branch
    """
    testhelpers.create_new_branch("test-branch")
    testhelpers.update_branch_protection("test-branch")
    testhelpers.create_required_signatures("test-branch")
    yield
    testhelpers.delete_required_signatures("test-branch")
    testhelpers.delete_branch_protection("test-branch")
    testhelpers.delete_new_branch("test-branch")


@pytest.fixture(scope="session")
def signatures_protection_delete_all():
    """"
    add and update branch protection rule then delete protection rule and the branch
    """
    testhelpers.create_new_branch("test-branch")
    testhelpers.update_branch_protection("test-branch")
    yield
    testhelpers.delete_branch_protection("test-branch")
    testhelpers.delete_new_branch("test-branch")


@pytest.fixture(scope="session")
def pull_requests_protection_create():
    """"
    add and update branch protection rule then delete protection rule and the branch
    """
    testhelpers.create_new_branch("test-branch")
    testhelpers.update_branch_protection("test-branch")
    testhelpers.create_pull_request_reviews("test-branch")
    yield
    testhelpers.delete_branch_protection("test-branch")
    testhelpers.delete_new_branch("test-branch")
