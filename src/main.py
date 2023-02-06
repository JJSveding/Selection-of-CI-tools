#from calculate import calculate_net_income
#from filters import Filters
from helpers import read_json_to_dataframe

if __name__ == '__main__':
   # costs = load_data('data/costs.json', 'costs')
    #sales = load_data('data/sales.json', 'sales')
    costs = read_json_to_dataframe('data/costs.json')
    print(costs)

    #filter = Filters(country_code='DK')

    #income_statement = calculate_net_income(costs, sales, filter)
