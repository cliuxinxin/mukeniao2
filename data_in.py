import os 
from tqdm import tqdm
from orms import Entry

# 遍历文件
def all_files_in(base):
    files  = []
    for root, ds, fs in os.walk(base):
        for f in fs:
            if f != '.DS_Store':
                fullname = os.path.join(root, f)
                files.append(fullname)
    return files

files = all_files_in('data_test')

# 存储数据
for file in tqdm(files):
    Entry.first_or_create(location=file)

print('end')