""""
GitHub Configuration
"""
GITHUB_REST_USER = "TatZhuk"
GITHUB_REST_REPO = "Test-version"
GITHUB_REST_REPO_URL = "https://api.github.com/repos/TatZhuk/Test-version"
GITHUB_REST_URL_BRANCHES = GITHUB_REST_REPO_URL + "/branches"
GITHUB_REST_URL_REF = GITHUB_REST_REPO_URL + "/git/refs"
GITHUB_REST_URL_BRANCH1 = GITHUB_REST_URL_BRANCHES + "/test-branch"
GITHUB_REST_URL_BRANCH2 = GITHUB_REST_URL_BRANCHES + "/test-branch1"
GITHUB_REST_URL_PROTECTION = GITHUB_REST_URL_BRANCH1 + "/protection"
GITHUB_REST_SEARCH = "https://api.github.com/search/repositories?q=user:TatZhuk&sort=update&per_page=10"

