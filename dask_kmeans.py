import matplotlib.pyplot as plt

from dask.distributed import Client
from dask_ml.cluster import KMeans
from dask_ml import datasets


# Scale up: connect to your own cluster with more resources
# see http://dask.pydata.org/en/latest/setup.html
client = Client(processes=False, threads_per_worker=4, n_workers=1, memory_limit="2GB")
print(f"Type du client --> {type(client)}")
# Scale up: increase n_samples or n_features
print(f"Loading large dataset --> 1000000 rows")
X, y = datasets.make_blobs(n_samples=1000000, chunks=100000, random_state=0, centers=3)
X = X.persist()
print(f"Training Kmeans=3 on large dataset --> 1000000 rows")
km = KMeans(n_clusters=3, init_max_iter=2, oversampling_factor=10)
km.fit(X)
print(f"Plotting centroid")
fig, ax = plt.subplots()
ax.scatter(
    X[::1000, 0],
    X[::1000, 1],
    marker=".",
    c=km.labels_[::1000],
    cmap="viridis",
    alpha=0.25,
)
plt.savefig("plots/clusters.png")
