import requests
from settings.repos import TEST_GET_REPO_BUG
from settings.credentials import GITHUB_API_USER
from settings.credentials import GITHUB_API_TOKEN

def test_get_repo_name_bug_scenario():
    # in settings/repos.py there is boolean variable TEST_GET_REPO_BUG defined
    # if it's value is False then do not execute test (test will show as Passed)
    # if it's value is True then test will be executed and will Fail
    if (TEST_GET_REPO_BUG == False):
        return

    # tuple with credentials to use in requests.get/delete
    authUserAndToken = (GITHUB_API_USER, GITHUB_API_TOKEN)

    ###### PRE-CONDITIONs ######
    # repos should not exist so let's delete them
    url = "https://api.github.com/repos/" + GITHUB_API_USER + "/test-get-repo-bug-A"
    # send DELETE but we are not interested in response
    response = requests.delete(url=url, auth=authUserAndToken)
    url = "https://api.github.com/repos/" + GITHUB_API_USER + "/test-get-repo-bug-B"
    response = requests.delete(url=url, auth=authUserAndToken)
    # so now we expect repos: 'test-get-repo-bug-A' and 'test-get-repo-bug-B' do NOT exists

    ###### STEP #1: create repo (A) ######
    url = "https://api.github.com/user/repos"
    dataToSend = {
        "name": "test-get-repo-bug-A",
        "private": True
    }
    response = requests.post(url=url, auth=authUserAndToken, json=dataToSend)
    # expecting code 201 (repo created)
    assert response.status_code == 201
    # store json object returned by server in 'jsonRepoInfo' variable
    jsonRepoInfo = response.json()
    assert jsonRepoInfo["name"] == "test-get-repo-bug-A"
    # store 'id' of created object (will be used in following steps)
    originalId = jsonRepoInfo["id"]

    ###### STEP #2: get repository (A) ######
    url = "https://api.github.com/repos/" + GITHUB_API_USER + "/test-get-repo-bug-A"
    # send GET request with credentials
    response = requests.get(url, auth=authUserAndToken)
    # expecting repo exists (as created in STEP#1) so expecting status code 200
    assert response.status_code == 200
    # store json object returned by server in 'jsonRepoInfo' variable (overwrite previous value from STEP#1)
    jsonRepoInfo = response.json()
    # validate 'name'
    assert jsonRepoInfo["name"] == "test-get-repo-bug-A"
    # validate 'id'
    assert jsonRepoInfo["id"] == originalId

    ###### STEP #3: Update repo name (A => B) ######
    url = "https://api.github.com/repos/" + GITHUB_API_USER + "/test-get-repo-bug-A"
    dataToSend = {
        "name": "test-get-repo-bug-B"
    }
    response = requests.patch(url=url, auth=authUserAndToken, json=dataToSend)
    # expecting 200 (updated)
    assert response.status_code == 200
    # store response with created object information
    jsonRepoInfo = response.json()
    # assert 'name' has changed
    assert jsonRepoInfo["name"] == "test-get-repo-bug-B"
    # assert 'id' has not changed
    assert jsonRepoInfo["id"] == originalId

    ###### STEP #4: get repository (with new name B) ######
    url = "https://api.github.com/repos/" + GITHUB_API_USER + "/test-get-repo-bug-B"
    # send GET request with credentials
    response = requests.get(url, auth=authUserAndToken)
    # expecting repo exists (as created in STEP#1) so expecting status code 200
    assert response.status_code == 200
    # store json object returned by server in 'jsonRepoInfo' variable (overwrite previous value from STEP#1)
    jsonRepoInfo = response.json()
    # validate 'name' is new name
    assert jsonRepoInfo["name"] == "test-get-repo-bug-B"
    # validate 'id'
    assert jsonRepoInfo["id"] == originalId

    ###### STEP #5: get repository (with old name A) ######
    url = "https://api.github.com/repos/" + GITHUB_API_USER + "/test-get-repo-bug-A"
    # send GET request with credentials
    response = requests.get(url, auth=authUserAndToken)
    ### VALIDATE - CURRENT BEHAVIOUR
    assert response.status_code == 200
    # store json object returned by server in 'jsonRepoInfo' variable (overwrite previous value from STEP#1)
    jsonRepoInfo = response.json()
    # validate 'name': github returns new name 'test-get-repo-bug-B' but we requested for repo 'test-get-repo-bug-A'
    assert jsonRepoInfo["name"] == "test-get-repo-bug-B"
    # validate 'id'
    assert jsonRepoInfo["id"] == originalId
    # VALIDATE - EXPECTED BEHAVIOUR:
    # as 'test-get-repo-bug-A' no longer exists expected status code should be 404
    assert response.status_code == 404  # THIS WILL FAIL
