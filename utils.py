from collections import OrderedDict
from collections import namedtuple
from itertools import product

class RunBuilder():
    @staticmethod
    def get_runs(params):

        Run = namedtuple('Run', params.keys())

        runs = []
        for v in product(*params.values()):
            runs.append(Run(*v))

        return runs


if __name__ == '__main__':
    params = OrderedDict(
        lr = [.01, .001]
        ,batch_size = [1000, 10000]
    )

    runs = RunBuilder.get_runs(params)
    for run in runs:
        for k,v in run._asdict().items():
            print("{}:{}".format(k,v))