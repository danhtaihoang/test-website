Method
==================

| A detail description of our method, namely Free Energy Minimization
  (FEM), can be found in our paper (Ref). Briefly, we define a free
  energy of data, and show that minimizing this free energy leads to
  an effective estimation of interactions. The algorithm of our method
  contains the following steps:
| (i) Initialize :math:`W_{ij}` at random;
| (ii) Compute local field :math:`H_i(t) = \sum_j W_{ij} \sigma_j (t)`;
| (iii) Compute data energy
  :math:`E_i(t) =  \frac{\sigma_i(t+1)}{\langle  \sigma(t+1) \rangle_{\text{model}}}  H_i(t),`
  where :math:`\langle  \sigma(t+1) \rangle_{\text{model}}` represents
  model expectation;
| (iv) Extract coupling
  :math:`W_{ij}^\text{new}= \sum_k \langle \delta E_i \delta \sigma_k  \rangle [C^{-1}]_{kj},`
  where :math:`\langle \cdot \rangle` represents sample mean,
  :math:`\delta f \equiv f -\langle f\rangle` and
  :math:`C_{jk} \equiv \langle \delta\sigma_j\delta\sigma_k\rangle;`
| (v) Repeat (ii)-(iv) until the discrepancy between observed
  :math:`\sigma_i(t+1)` and model expectation
  :math:`\langle  \sigma(t+1)  \rangle_{\text{model}}`,
  :math:`D_i(W)\equiv\sum_{t} \big[ \sigma_i(t+1) - \langle \sigma_i(t+1) \rangle_{\text{model}} \big]^2`
  starts to increase;
| (vi) Compute (ii)-(iv) in parallel for every variable index
  :math:`i \in \{1, 2, \cdots, N\}`.
