from API import *
metrics = {
    '1' : 'metric',
    '2' : 'imperial'
}

metrics = input(f'which metrics? {metrics}\n')
city = input('insert city\n')

try:
    api = Api(CITY= city, METRICS= metrics)
except:
    api = Api()