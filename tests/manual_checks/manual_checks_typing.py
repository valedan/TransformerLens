# Adapted from [HookedTransformer_Demo.ipynb]. Useful for testing that all the typing mechanisms work
# out.

# %%

from jaxtyping import Float, install_import_hook
hook = install_import_hook("transformer_lens", ("typeguard", "typechecked"))

import torch as t
from transformer_lens import HookedTransformer, HookedTransformerConfig

DEVICE = "cuda" if t.cuda.is_available() else "cpu"
MODEL = "gpt2"

# %%
model = HookedTransformer.from_pretrained(MODEL)
model.to(DEVICE)

# %%

prompt = "Hello World!"
tokens = model.to_tokens(prompt, prepend_bos=False)
logits_tokens = model(tokens)
logits_text: Float[t.Tensor, "1 n_tokens d_vocab"] = model(prompt, prepend_bos=False)

# %%

logits_text.shape
# %%
hook.uninstall()