from orms import Entry,Tran
from tqdm import tqdm

tran = Tran.first_or_create(name='generate_test',type='dataset')

entries = Entry.all().every(100)

for entry in tqdm(entries):
    dataset_type = entry.location.split('/')[1].split('_')[1]
    entry.trans().attach(tran,{'result':dataset_type})