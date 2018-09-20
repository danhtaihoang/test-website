Model
==================

To demonstrate the interdependence between variables in stochastic 
systems, we use a kinetic model in which the state of variable :math:`i`
at the time point :math:`t+1`, :math:`\sigma_i(t+1)` :math:`(i = 1,N)`,
depend on the state of itself and other variables at the previous time
point :math:`t`, :math:`\vec{\sigma}(t)`, as the following conditional
probability

.. math::

   P[\sigma_i(t+1)|\vec{\sigma}(t)] = \frac{\exp [ \sigma_i(t+1) H_i(t)]}{\mathcal{N}}

where :math:`H_i(t) = \sum_j W_{ij} \sigma_j(t)` represents the local
field, and
:math:`\mathcal{N} = \sum_{\sigma_i(t+1)} \exp[\sigma_i(t+1) H_i(t)]`
normalizing factor. Intuitively, the state :math:`\sigma_i(t+1)` tends
to the same direction with local field :math:`H_i(t)`. 

Our goal is to infer the coupling strength between variables :math:`W_{ij}` from time series of variable states :math:`\vec{\sigma}`.
