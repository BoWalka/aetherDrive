#!/usr/bin/env python3

from huggingface_hub import snapshot_download
import os

MODELS_DIR = "../ai-brain"

# Model A: Classifier - Input = first 16 MB + file magic + entropy → outputs OS + version
MODEL_A = "microsoft/DialoGPT-medium"  # Example, replace with suitable model

# Model B: Boot Config Generator - Input = OS identification → outputs exact boot stanza
MODEL_B = "gpt2"  # Text generation model

# Model C: Filesystem Recommender - Recommends best FS based on detected OS
MODEL_C = "distilbert-base-uncased-finetuned-sst-2-english"  # Example classifier

def download_model(model_id, local_dir):
    print(f"Downloading {model_id} to {local_dir}...")
    snapshot_download(repo_id=model_id, local_dir=local_dir)

def main():
    os.makedirs(MODELS_DIR, exist_ok=True)

    # Download Model A
    download_model(MODEL_A, os.path.join(MODELS_DIR, "model_a"))

    # Download Model B
    download_model(MODEL_B, os.path.join(MODELS_DIR, "model_b"))

    # Download Model C
    download_model(MODEL_C, os.path.join(MODELS_DIR, "model_c"))

    print("All models downloaded.")

if __name__ == "__main__":
    main()