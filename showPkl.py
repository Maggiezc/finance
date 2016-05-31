import csv
import datetime
import re

import pandas as pd
import requests
import os
import pdb

def main():
	filename = "data/DATA.pkl"
	data0 = pd.read_pickle(filename)
	data0 = data0[-700:]
	for i in range(len(data0.index)):
		print data0[i:i+1]

if __name__ == "__main__":
    main()