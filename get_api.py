import requests
import datetime


url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "6eca90170dmsh16bfae26d02197ap1a855cjsn4ea83c303c70"
}

data_header = ['Continent', 'Country', 'Population',
               "Time Day", 'New Case', 'Active Case ', 'Total Case', 'New Death',
               'Deaths 1M_pop', 'Total Death', 'Tests 1M_pop', 'Total Tests']


def get_data():
    r = requests.request("GET", url, headers=headers)
    if r.status_code in range(200, 300):
        data = r.json()
        data_resp = data['response']
        dict_data = {}
        # dict_data['header'] = data_header
        for cont in data_resp:
            list_d = []
            continent = cont["continent"]
            country = cont["country"]
            population = cont["population"]
            case_total = cont['cases']['total']
            case_active = cont['cases']['active']
            case_new = cont['cases']['new']
            deaths_new = cont['deaths']['new']
            deaths_1M_pop = cont['deaths']['1M_pop']
            deaths_total = cont['deaths']['total']
            tests_1M_pop = cont['tests']['1M_pop']
            tests_total = cont['tests']['total']
            time_day = datetime.datetime.now().strftime("%c")
            list_d.extend([continent, country, population,
                           time_day, case_new, case_active, case_total,
                           deaths_new, deaths_1M_pop, deaths_total,
                           tests_1M_pop, tests_total])
            dict_data[country] = list_d

        return dict_data
