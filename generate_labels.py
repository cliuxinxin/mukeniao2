from orms import Entry,Tran
from tqdm import tqdm

tran = Tran.first_or_create(name='generate_default_label',type='generate')

entries = Entry.all()

for entry in tqdm(entries):
    label = entry.location.split('/')[2]
    entry.label = label
    entry.save()
    entry.trans().attach(tran,{'result':label})