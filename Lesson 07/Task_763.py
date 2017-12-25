"""
Lazy thief
"""

rates = {'Sberbank': 55.8, 'VTB24': 53.91}
reverse_rates = dict(zip(rates.values(), rates.keys()))
good_level = min(reverse_rates.items())
print(f'{good_level[1]} -> {good_level[0]}')