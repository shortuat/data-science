"""Core simulation logic (placeholder)
Implement the simulator here.
"""

import random

def run_simulation(num_intervals=5):
    print('Running demo simulation...')
    for i in range(num_intervals):
        count = random.randint(5, 15)
        avg_speed = round(random.uniform(30, 80), 2)
        print(f'Interval {i+1}: vehicles={count}, avg_speed={avg_speed} km/h')
