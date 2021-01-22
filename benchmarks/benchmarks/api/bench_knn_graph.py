import time
import dgl
import torch
import numpy as np

from .. import utils


@utils.benchmark('time', timeout=60)
@utils.parametrize('k', [3, 5, 10])
@utils.parametrize('size', [50, 200, ])
@utils.parametrize('dim', [16, 64, 128])
def track_time(size, dim, k):
    device = utils.get_bench_device()
    features = np.random.randn(size, dim)
    feat = torch.tensor(features, dtype=torch.float, device=device)
    # dry run
    dgl.knn_graph(feat, k)
    # timing
    t0 = time.time()
    for i in range(10):
        dgl.knn_graph(feat, k)
    t1 = time.time()

    return (t1 - t0) / 10
