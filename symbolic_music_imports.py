from miditok import REMI
# import miditok
import torch

from transformers import AutoModelForCausalLM, GenerationConfig, BitsAndBytesConfig
from tqdm import tqdm
import glob
import numpy as np
from pathlib import Path
from matplotlib import pyplot as plt
# import pandas as pd

import IPython.display as ipd
# import pretty_midi
import os
import random