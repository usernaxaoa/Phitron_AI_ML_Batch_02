# %%

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import MinMaxScaler


from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

# %%

df = pd.read_csv('/home/nafiz/Downloads/bangladesh_student_performance_updated.csv')

# %%
df.describe()

# %%
df.info()
# %%
df.isnull().sum()
# %%
df['Pstatus'].unique()
# %%
df.columns
# %%
df.duplicated()
# %%
df.hist(bins=15, figsize=(10,6))
plt.suptitle('distribution of numerical features')
# %%
num_col = ['age', 'tuition_fee', 'ssc_result', 'hsc_result']
df[num_col].corr()
# %%
plt.figure(figsize=(10, 6))
sns.heatmap(
    df[num_col].corr(),
    annot=True,
    cmap='coolwarm'
)
plt.title('correlation with heatmap')
plt.show()
# %%
sns.boxplot(data=df, x=df['tuition_fee'])
# %%
df.sample(10)
# %%
nominal_cat = ['gender', 'address', 'famsize', 'Pstatus', 'relationship', 'smoker', 'F_Job','time_friends' ]
ordinal_cat = ['M_Edu', 'F_Edu', 'M_Job']

m_edu = ['0', '1', '2', '3', '4']
f_edu = ['0', '1', '2', '3', '4']

time_order = ['5', '4', '3', '2', '1']

numerical_col = ['age', 'tuition_fee', 'ssc_result']


# %%
numerical_transformer_pipe = Pipeline(
    steps=[
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ]
)
numerical_transformer_pipe
# %%
nominal_transform_pipe = Pipeline(
    steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('encoding',OneHotEncoder(sparse_output=False, handle_unknown='ignore') )
    ]
)

nominal_transform_pipe

ordinal_transform_pipe = Pipeline(
    steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('encoding',OrdinalEncoder(categories=['M_edu_order, F_edu_order, time_friends_order']) ),
        ('scaler', MinMaxScaler())
    ]
)

ordinal_transform_pipe
# %%
