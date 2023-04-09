import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

dataframe = pd.read_csv('real_estate.csv')
# print(dataframe.to_markdown)
print(dataframe.isna().sum())

col_names = dataframe.columns.to_list()
col_nums = len(col_names)
f, axs = plt.subplots(1, col_nums - 1, figsize=(35, 8))
for i in range(1, col_nums):
    axs[i-1].set_title(col_names[i])
    axs[i-1].hist(dataframe[col_names[i]])
#sns.lineplot(data=dataframe[col_names[i]],ax= axs[i-1])
#     axs[i - 1].set_title(col_names[i])
#     axs[i - 1].plot(dataframe[col_names[i]])
plt.show()


