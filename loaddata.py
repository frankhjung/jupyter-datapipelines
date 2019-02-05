#!/usr/bin/env python3

# kaggle.com
#
# The Kaggle Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
#
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

import sys              # log to stdout
import logging          # use logging rather than prints
import pandas as pd     # data processing, CSV file I/O (e.g. pd.read_csv)

# other packages ...
# import numpy as np    # linear algebra
# import glob           # file globs

# setup logging
log = logging.getLogger(__name__)
logHandler = logging.StreamHandler(sys.stdout)
logHandler.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
log.addHandler(logHandler)
log.setLevel(logging.DEBUG)

# show versions of software used
log.debug(f"pandas version: {pd.__version__}")
log.debug(f"logging version: {logging.__version__}")

# declare URL to dataset
URL = 'https://data.gov.au/dataset/7f90d314-fa64-4bae-8609-2e26ff48f6fa/resource/05390642-bdeb-4174-9bd5-c1df6e6d1e9e/download/2018-australian-sdg-indicator-9-2-2v2.csv'

# load into dataframe and print
d = pd.read_csv(URL)
print(d)

