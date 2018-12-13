import argparse
from pathlib import Path
import main
from argparse import Namespace
from stroke import constants
import numpy as np
p_default = 10
s_default = 1000


if __name__ == '__main__':

    hospital_path = str(Path('data/hospitals/Demo.csv'))
    times_path = str(Path('data/travel_times/Demo.csv'))

    sex = constants.Sex.MALE
    upper = 1
    for age in range(30,85+upper,5): # 30 to 85
        for race in range(0,9+upper,1): # 0 to 9
            for time_since_symptoms in range(10,100+upper,10): # 10 to 100
                args = Namespace(patients=1,
                                simulations=s_default,
                                multicore=True,
                                hospital_file=str(hospital_path),
                                times_file=str(times_path),
                                sex=sex,
                                age=age,
                                race=race,
                                time_since_symptoms=time_since_symptoms)
                main.main(args)
