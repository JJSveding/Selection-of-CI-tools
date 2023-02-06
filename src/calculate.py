import pandas as pd

from filters import Filters


def calculate_net_income(costs: pd.DataFrame, sales: pd.DataFrame, filters: Filters):
    print(costs)
    print(sales)
    print(filters)
    # matching_costs = costs.query("store_number==1")
    # print(matching_costs)
