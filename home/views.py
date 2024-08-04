from django.shortcuts import render

# Create your views here.

from miditok import REMI
# import miditok
import torch
from transformers import AutoModelForCausalLM, GenerationConfig, BitsAndBytesConfig
# from tqdm import tqdm
# import glob
import numpy as np
from pathlib import Path
# from matplotlib import pyplot as plt
# import pandas as pd

# import IPython.display as ipd
# import pretty_midi
import os
import random
from util.generation import generate_comparison_song
from util.mid_to_audio import play_midi

model_name = "finetuning_16.0epochs"
model = AutoModelForCausalLM.from_pretrained("theglassofwater/"+model_name)
tokenizer = REMI.from_pretrained("theglassofwater/remi_12500")
generate_comparison_song(model, tokenizer, [1,], 200)

def play_audio(request):
    play_midi("personal_website\music\midi\holder.mid")

def index(request):
    return render(request, 'home/index.html')