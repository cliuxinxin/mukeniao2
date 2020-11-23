orator migrate:rollback -f
orator migrate -f
python data_in.py 
python generate_labels.py
python generate_train.py