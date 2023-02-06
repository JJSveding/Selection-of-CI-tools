#from unittest.mock import patch

import pandas as pd

from src.helpers import read_json_to_dataframe

#import pytest



def test_read_json_to_dataframe():
    df = read_json_to_dataframe('data/costs.json')
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 4
    assert set(df.columns) == {'bimonthly_period', 'cost_category', 'cost_value', 'country_code', 'sales_channel', 'store_number'}
    assert df.loc[0, 'cost_value'] == 8000.00
    assert df.loc[1, 'cost_category'] == 'Operating Costs'
    assert df.loc[2, 'sales_channel'] == 'Online'
