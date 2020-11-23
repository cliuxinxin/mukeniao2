from orms import Entry,Tran
from tqdm import tqdm

tran = Tran.first_or_create(name='generate_train',type='dataset')

entries = Entry.all()

for entry in tqdm(entries):
    dataset_type = entry.location.split('/')[1].split('_')[1]
    entry.trans().attach(tran,{'result':dataset_type})