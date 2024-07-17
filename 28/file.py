import pandas as pd

# 使用chunksize分块读取大文件
chunksize = 10 ** 6  # 一次读取1,000,000行
chunks = pd.read_csv('g_us_patent_citation.tsv', sep='\t', usecols=[0, 2, 3, 5], chunksize=chunksize)

# 合并块并保存
result_df = pd.concat(chunks)
result_df.to_csv('newfile.csv',index=False)


