
import os

import click
import numpy as np
import pandas as pd
from github import Github
from tabulate import tabulate


@click.group()
def pr_comments() -> None:
    pass

@pr_comments.command()
@click.option("--pr-number", "pr_number", type=int, required=False)
def print_changed_costs(pr_number:int) -> None:

    # First create a Github instance:
    # using an access token
    gh_client = Github(os.environ["credentials"])
    gh_repo = gh_client.get_repo('JJSveding/Selection-of-CI-tools')
    pr_obj = gh_repo.get_pull(pr_number)

    # Create random dataframe with data
    d = {'previous_costs': np.random.randint(0,100,size=6), 'new_costs': np.random.randint(0,100,size=6)}
    df = pd.DataFrame(data=d)
    df['difference'] = ((df['new_costs'] - df['previous_costs']) / df['previous_costs']) * 100

    # Transform to markdown
    table_str = tabulate(tabular_data=df, headers="keys", tablefmt="github", showindex=False)

    # Create comment
    pr_body_str = _create_pr_body(table_str)

    #Post comment
    pr_obj.create_issue_comment(body=pr_body_str)


def _create_pr_body(table_markdown: str) -> str:
    content = "# PR change overview"
    content += "<details>"
    content += "<summary><strong> Costs that has changed </strong>"
    content += "(click to show details)</summary>\n\n"
    content += f"{table_markdown}\n</details>\n\n"
    content += "\n\n **🚨 Significant changes detected. Investigate if they are expected.**"
    content += (
        "\n### Tasks\n- [ ] Tick here to confirm that you have "
        "investigated and approved the above cost model results."
    )
    return content
