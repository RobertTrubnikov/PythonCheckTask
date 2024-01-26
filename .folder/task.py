import random
import pandas as pd
list = ['robot'] * 10
list += ['human'] * 10
random.shuffle(list)
data = pd.DataFrame({'whoAmI':list})
data.head()

one_hot_encoded = pd.concat([data, pd.get_dummies(data['whoAmI'], prefix='whoAmI')], axis=1)
one_hot_encoded.head()

print(one_hot_encoded.head())