## Prompt engineering guide
Let's say you want to draw an image of ``lion``. The raw promt, ``lion`` will give you images that are usually chaotic or of bad quality.

To obtain better results, the prompt should be egineered. A basic recipe is the following:

``raw prompt`` + ``style`` + ``artist`` + ``details``

- Examples of ``style`` are: *Portrait*, *Realistic*, *Oil painting*, *Pencil drawing*, *Concept art*
- Examples of ``artist`` are: Jan van Eyck (when ``style`` = *Portrait*), *Vincent Van Gogh* (when ``style`` = *Oil painting*), *Leonardo Da Vinci* (when ``style`` = *Pencil drawing*), and so on. Note that you can also mix artists, to get original results.
- Examples of ``details`` are *Unreal Engine* if you want to add realistic lightining, *8 k* if you want to add more details, *artstation* if you want to make your image more artistic, and so on.

Example prompt: 

*"retrofuturistic portrait of a lion in astro suit, space graphics art in background, close up, wlop, dan mumford, artgerm, liam brazier, peter mohrbacher, 8 k, raw, featured in artstation, octane render, cinematic, elegant, intricate, 8 k"*

To see more examples of prompts and get inspirations, check [here](https://lexica.art/).


## Resources

**Colab notebooks**
- Introduction to diffusers 🧨, the Hugging Face 🤗 library for diffusion models [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/diffusers_intro.ipynb)
- Introduction to Stable Diffusion with diffusers 🧨 [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/stable_diffusion.ipynb)
- Image2Image pipeline for Stabel Diffusion using diffusers 🧨 [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/patil-suraj/Notebooks/blob/master/image_2_image_using_diffusers.ipynb)
- Denoising Diffusion Implicit Models in Tensorflow [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/keras-team/keras-io/blob/master/examples/generative/ipynb/ddim.ipynb)

**Blogs**
- [What are Diffusion Models?](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/#nice) introduction to Diffusion models and mathematical derivations.
- [The Annotated Diffusion Model](https://huggingface.co/blog/annotated-diffusion) step-by-step tutorial for building a Diffusion model from scratch in Pytorch
- [Generative Modeling by Estimating Gradients of the Data Distribution](https://yang-song.net/blog/2021/score/) Introduction to score-based generative models.
