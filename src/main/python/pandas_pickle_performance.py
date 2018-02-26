import pandas as pd
from sklearn.externals import joblib
import pickle
import timeit

df = pd.read_csv('http://download.geonames.org/export/zip/GB_full.csv.zip', compression='zip', sep='\t', header=0)
print(df.shape)

start_time = timeit.default_timer()
joblib.dump(df, '/tmp/df_2.pkl')
print(timeit.default_timer() - start_time)

start_time = timeit.default_timer()
df.to_pickle('/tmp/df_1.pkl')
print(timeit.default_timer() - start_time)

start_time = timeit.default_timer()
with open('/tmp/df_3.pkl', 'wb') as fh: pickle.dump(df, fh)
print(timeit.default_timer() - start_time)
