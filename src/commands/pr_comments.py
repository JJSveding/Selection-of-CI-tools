
import os

import click
from github import Github


@click.group()
def pr_comments() -> None:
    pass

@pr_comments.command()
@click.option("--pr-number", "pr_number", type=int, required=False)
def print_changed_costs(pr_number:int) -> None:

    # First create a Github instance:
    # using an access token
    gh_client = Github(os.environ["MY_SECRET_CI_TOOLS"])
    gh_repo = gh_client.get_repo('JJSveding/Selection-of-CI-tools')
    pr_obj = gh_repo.get_pull(pr_number)
    pr_obj.create_issue_comment(body="Did my test work?")
    print(type(gh_repo.get_readme()))
