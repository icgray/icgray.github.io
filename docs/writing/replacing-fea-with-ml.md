# Replacing FEA With ML, Carefully

There is a bad version of "AI for engineering" that pretends learned models can replace first-principles methods everywhere. I am not interested in that version.

The useful version is narrower and better: use machine learning to make early iteration cheaper. In the shot peening project, that means predicting likely deformation outcomes quickly enough to compare recipes and narrow the search space before spending time on full simulation.

## Where a surrogate earns its place

A finite-element run is authoritative but slow, and most of an engineer's day is not spent needing the final authoritative answer. It is spent screening: which of these twenty parameter sets are even worth simulating? That screening step is where a fast approximation pays off.

So the model lives in front of the expensive layer, not in place of it:

- generate training data from simulations you already trust,
- learn the rough deformation response,
- use the prediction to rank and prune candidates,
- send only the survivors to full FEA.

The win is throughput. You explore more of the design space per week because you are not paying full simulation cost for every dead-end idea.

## Keeping it honest

The failure mode is treating the surrogate as ground truth. A learned model extrapolates badly outside its training distribution, and it will happily return a confident number for a recipe it has never seen anything like. So the discipline matters: state the validity range, keep FEA in the loop as the checker, and never let a prediction be the last word on a part that actually gets manufactured.

Used that way, ML becomes an accelerator for engineering judgment instead of a substitute for it. The model is not the authority. It is the fast layer in front of the expensive one, and knowing the difference is the whole point.
