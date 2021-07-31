# 6

- PCA
  - `PCA(n_components)`
    - `.fit_transform(X)`
    - `.explained_variance_ratio_` : eigenvalue 크기 비율
- LDA
  - `LinearDiscriminantAnalysis(n_components)`
    - `.fit(X, y)`
- SVD
  - `np.linalg.svd(matrix)`
    - return `U, Sigma, Vt`
      - `Sigma` : 대각 성분만 있는 array
  - `scipy.sparse.linalg.svd(matrix, full_matrices=False)`
    - return `U, Sigma, Vt`
    - `full_matrices=False` : U와 Vt가 nxn, mxm이 아닌 nxk, kxm으로 나옴, k=min(n, m)
  - `scipy.linalg.svds(matrix, k)`
    - `k` : component 수
    - return `U, Sigma, Vt`
    - numpy svd와 마찬가지로 `Sigma`는 대각 성분만 있는 array
- NMF
  - `NMF(n_components)`

