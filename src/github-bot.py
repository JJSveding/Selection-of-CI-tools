# #from github import Github, GithubIntegration
# #from github.ContentFile import ContentFile
# from base64 import b64decode
# import os
# import click

# # def _get_github_client() -> Github:
# #     # Get the Github App
# #     app = GithubIntegration(
# #         integration_id=os.environ["GITHUB_APP_ID"],
# #         private_key=b64decode(os.environ["GITHUB_APP_PRIVATE_KEY"]).decode(),
# #     )
# #     # Get the Github App installation on our repo
# #     owner, repo = os.environ["GITHUB_REPOSITORY"].split("/")
# #     installation = app.get_installation(owner=owner, repo=repo)
# #     return Github(login_or_token=app.get_access_token(installation.id).token)


# @click.command()
# #@click.option("--pr-number", "pr_number", type=int, required=False)
# def print_changed_costs() -> None:
#     # gh_client = _get_github_client()
#     # gh_repo = gh_client.get_repo(os.environ["GITHUB_REPOSITORY"])
#     # pr_obj = gh_repo.get_pull(pr_number)
#     click.echo("Hello world")
