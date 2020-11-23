from orms import Tran,Entry

tran = Tran.where('name','=','generate_train')


tran.entries()