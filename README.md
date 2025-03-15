# Diffusion models tutorial 

A while ago [Stable Diffusion Public Release](https://stability.ai/blog/stable-diffusion-public-release) made available to everyone one of the most powerful deep learning models for image generation. 

This repository contains:

- Tutorials on the theory behind diffusion models and the software libraries used to implement them.
- A step-by-step guide on how to implement a diffusion model from scratch.
- A collection of scripts and notebooks that can be used to generate images with Stable Diffusion.
- A basic guide to prompt engineering.
- A list of resources to dig deeper into the world of diffusion models.

## 1. 🚀 Quick start

### 🧱 Learn the basics

Check these [slides](https://docs.google.com/presentation/d/1jUO9jZLtUGoK7kgg0kurBgDwDsNOLybrYKU-O2y98xM/edit?usp=sharing) for a short introduction about the basic idea behind diffusion models and stable diffusion.

### 💻 Play with notebooks

> [!WARNING] 
> Since the libraries used in the notebooks below are often updated, the notebooks might stop working at some point. Please, open an issue if you encounter problems and bugs.

Try out **Stable Diffusion** by running one of the Colab notebooks below.

- Text to image [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1MyESLsR8D5l_EBqumwxL0eMzNmd3uqs6?usp=sharing)
- Image to image [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1zjr9n60q3G8Qd87WG3ZnjDgI-D1YBCbG?usp=sharing)

To try out **Stable Diffusion 2**, run one of the Colab notebooks below.
- Text to image [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1e8MV75aD66It0WXo5-ddUEjfvhVG8URv?usp=sharing)
- Impainting [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1JuTzAY0NzojvSU-rB4BNI9F8z3tcv9iX?usp=sharing)
- Super-resolution [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1qnKCWs4IB-n1xfCjeNgbaSu-mFwp7bLv?usp=sharing)
- Depth-to-image [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1dS9E8lBJywuoCmZiZAVXo6IaGw4Te5B0?usp=sharing)

### 🤓 Understand the theory and learn to build pipelines

- Understand the theory behind stable diffusion models and learn how to code a simple diffusion model from scratch in [this notebook](https://nbviewer.org/github/FilippoMB/Diffusion_models_tutorial/blob/main/diffusion_from_scratch.ipynb).
- Become familiar with the stable diffusion pipeline and the diffusers 🧨 library  in [this notebook](https://nbviewer.org/github/FilippoMB/Diffusion_models_tutorial/blob/main/Diffusers_library.ipynb).

To run the notebooks you need to have several libraries installed. You can do that by installing Anaconda (or [Miniconda](https://docs.anaconda.com/free/miniconda/miniconda-install/)) and then creating the environment using the provided env files.

First, try to create the environment using [environment.yml](https://github.com/FilippoMB/Diffusion_models_tutorial/blob/main/environment.yml):

````bash
conda env create -f environment.yml
````

If that doesn't work, try with [env_flex.yml](https://github.com/FilippoMB/Diffusion_models_tutorial/blob/main/env_flex.yml) that allows for a more flexible installation. 

````bash
conda env create -f env_flex.yml
````

The risk here is that it will install more recent versions of the software packages and the notebooks might give some errors.
You might need to this more flexible install also if you are on Windows.
If you are on MacOS, instead, use [env_mac.yml](https://github.com/FilippoMB/Diffusion_models_tutorial/blob/main/env_mac.yml):

````bash
conda env create -f env_flex.yml
````

## 2. 👷🏻 Prompt engineering guide
Let's say you want to draw an image of ``lion``. The raw prompt, ``lion`` will give you images that are usually a bit chaotic or of worse quality.


<div>
<img src="./img/lion_short.png" width="250"/>
</div>

To obtain better results, the prompt should be engineered. A basic recipe is the following:

``raw prompt`` + ``style`` + ``artist`` + ``details``

- Examples of ``style`` are: *Portrait*, *Realistic*, *Oil painting*, *Pencil drawing*, *Concept art*
- Examples of ``artist`` are: Jan van Eyck (when ``style`` = *Portrait*), *Vincent Van Gogh* (when ``style`` = *Oil painting*), *Leonardo Da Vinci* (when ``style`` = *Pencil drawing*), and so on. Note that you can also mix artists, to get original results.
- Examples of ``details`` are *Unreal Engine* if you want to add realistic lightining, *8 k* if you want to add more details, *artstation* if you want to make your image more artistic, and so on.

Example of elaborated prompts: 

*"Professional photograph of a lion with a black mane, high quality, highly detailed, award-winning, hd, 8k, awe-inspirin"*

<div>
<img src="./img/lion_long1.png" width="600"/>
</div>


*"retrofuturistic portrait of a lion in astro suit, space graphics art in background, close up, wlop, dan mumford, artgerm, liam brazier, peter mohrbacher, raw, featured in artstation, octane render, cinematic, elegant, intricate, 8 k"*

<div>
<img src="./img/lion_long.png" width="600"/>
</div>

To see more examples of prompts and get inspirations, check [here](https://lexica.art/). To find a prompt for a specific image, you can use [this](https://colab.research.google.com/github/pharmapsychotic/clip-interrogator/blob/main/clip_interrogator.ipynb?authuser=0&pli=1#scrollTo=rbDEMDGJrJEo) image classifier notebook. 


## 3. 📚 Resources

**Repositories**
- A web interface with tons of advanced features that runs locally - [WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui).
- A WebUI extension to generate videos - [Deforum WebUI](https://github.com/deforum-art/sd-webui-deforum)

> [!WARNING] 
> Since the libraries used in the notebooks below are often updated, the notebooks might stop working at some point. Please, open an issue if you encounter problems and bugs.

**Colab notebooks (demo)**
- text2img and img2img with advanced features [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1AfAmwLMd_Vx33O9IwY2TmO9wKZ8ABRRa)
- Generate video animations [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/deforum/stable-diffusion/blob/main/Deforum_Stable_Diffusion.ipynb) (you need to download the weights from [here](https://huggingface.co/CompVis/stable-diffusion-v-1-4-original) and upload them to your Google Drive)
- Find prompts with the interrogator [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pharmapsychotic/clip-interrogator/blob/main/clip_interrogator.ipynb?authuser=0&pli=1#scrollTo=rbDEMDGJrJEo)
- Stable Diffusion in Tensorflow/Keras [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1zVTa4mLeM_w44WaFwl7utTaa6JcaH1zK)
- Image2Image pipeline for Stable Diffusion [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/patil-suraj/Notebooks/blob/master/image_2_image_using_diffusers.ipynb)

**Colab notebooks (tutorials)**
- Introduction to diffusers 🧨, the Hugging Face 🤗 library for diffusion models [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/diffusers_intro.ipynb)
- Introduction to Stable Diffusion with diffusers 🧨 [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/stable_diffusion.ipynb)
- Training a diffusion model with diffusers 🧨 [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/gist/anton-l/f3a8206dae4125b93f05b1f5f703191d/diffusers_training_example.ipynb#scrollTo=smJeP67bF0yj)
- Denoising Diffusion Implicit Models in Tensorflow/Keras [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/keras-team/keras-io/blob/master/examples/generative/ipynb/ddim.ipynb)


**Blogs**
- [What are Diffusion Models?](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/#nice) introduction to Diffusion models and mathematical derivations.
- [The Annotated Diffusion Model](https://huggingface.co/blog/annotated-diffusion) step-by-step tutorial for building a Diffusion model from scratch in PyTorch.
- [Generative Modeling by Estimating Gradients of the Data Distribution](https://yang-song.net/blog/2021/score/) Introduction to score-based generative models.

**Papers**
- [[1](https://openaccess.thecvf.com/content/CVPR2022/papers/Rombach_High-Resolution_Image_Synthesis_With_Latent_Diffusion_Models_CVPR_2022_paper.pdf)] Rombach, Robin, et al. "High-resolution image synthesis with latent diffusion models." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2022.
- [[2](https://arxiv.org/abs/2006.11239)] Ho, Jonathan, Ajay Jain, and Pieter Abbeel. "Denoising diffusion probabilistic models." Advances in Neural Information Processing Systems, 2020.
- [[3](https://arxiv.org/abs/1907.05600)] Song, Yang, and Stefano Ermon. "Generative modeling by estimating gradients of the data distribution." Advances in Neural Information Processing Systems, 2019.
