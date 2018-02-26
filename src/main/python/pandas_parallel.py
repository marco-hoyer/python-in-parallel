import pandas as pd
from joblib import Parallel, delayed
import multiprocessing


def temp_func(df):
    df['c'] = df.a + df.b
    return df


def apply_parallel(df, func):
    result = Parallel(n_jobs=multiprocessing.cpu_count())(delayed(func)(group) for name, group in df)
    return pd.concat(result)


if __name__ == '__main__':
    df = pd.DataFrame({'a': [6, 2, 2], 'b': [4, 5, 6]}, index=['g1', 'g1', 'g2'])
    print('parallel version: ')
    print(apply_parallel(df.groupby(df.index), temp_func))
