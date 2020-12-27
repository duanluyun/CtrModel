import os

#使用的模型类型(deep/wide/wide_and_deep)
modelType="wide_and_type"



# 训练数据以及测试数据读取路径
workDir=os.getcwd()
trainData=workDir+r"\Data\adult.data"
testData=workDir+r"\Data\adult.test"

#列名
colNames=[ "age", "workclass", "fnlwgt", "education", "education_num",
            "marital_status", "occupation", "relationship", "race", "gender",
            "capital_gain", "capital_loss", "hours_per_week", "native_country",
            "income_bracket"]
# 标签列列名
label="label"
#原数据标签列
labelcol="income_bracket"
#训练数据标识列名
isTrain="is_train"
#需要分桶操作的数据列名
groupCols=["age"]
cutThreshold={"age": [0, 25, 65, 90]}

# columns for wide model
wide_cols = ['workclass', 'education', 'marital_status', 'occupation',
             'relationship', 'race', 'gender', 'native_country', 'age_group']
x_cols = [['education', 'occupation'], ['native_country', 'occupation']]

# columns for deep model
embedding_cols = ['workclass', 'education', 'marital_status', 'occupation',
                  'relationship', 'race', 'gender', 'native_country']
cont_cols = ['age', 'capital_gain', 'capital_loss', 'hours_per_week']