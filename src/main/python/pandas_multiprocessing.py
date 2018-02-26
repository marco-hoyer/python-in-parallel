import pandas as pd
import numpy as np
import seaborn as sns
from multiprocessing import Pool

import time

num_partitions = 10  # number of partitions to split dataframe
num_cores = 4  # number of cores on your machine

iris = pd.DataFrame(sns.load_dataset('iris'))


def parallelize_dataframe(df, func):
    df_split = np.array_split(df, num_partitions)
    pool = Pool(num_cores)
    df = pd.concat(pool.map(func, df_split))
    pool.close()
    pool.join()
    return df


def multiply_columns(data):
    print("executing multiply")
    data['length_of_word'] = data['species'].apply(lambda x: len(x))
    time.sleep(2)
    return data


iris = parallelize_dataframe(iris, multiply_columns)

print(iris)
