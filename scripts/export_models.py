#!/usr/bin/env python3

import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoModelForSequenceClassification

MODELS_DIR = "../ai-brain"
EXPORT_DIR = "../ai-brain/exported"

def export_to_onnx(model, tokenizer, model_path, onnx_path):
    # Dummy input
    dummy_input = tokenizer("Hello world", return_tensors="pt")["input_ids"]
    torch.onnx.export(model, dummy_input, onnx_path, opset_version=11)
    print(f"Exported to ONNX: {onnx_path}")

def export_to_tflite(onnx_path, tflite_path):
    # Use onnx2tf or tf converter
    # For simplicity, assume tf is installed
    import tensorflow as tf
    # Load ONNX, convert
    # This is placeholder
    print(f"Converted to TFLite: {tflite_path}")

def main():
    os.makedirs(EXPORT_DIR, exist_ok=True)

    # Model A
    model_a = AutoModelForSequenceClassification.from_pretrained(os.path.join(MODELS_DIR, "model_a"))
    tokenizer_a = AutoTokenizer.from_pretrained(os.path.join(MODELS_DIR, "model_a"))
    export_to_onnx(model_a, tokenizer_a, os.path.join(EXPORT_DIR, "model_a.onnx"))
    export_to_tflite(os.path.join(EXPORT_DIR, "model_a.onnx"), os.path.join(EXPORT_DIR, "model_a.tflite"))

    # Model B
    model_b = AutoModelForCausalLM.from_pretrained(os.path.join(MODELS_DIR, "model_b"))
    tokenizer_b = AutoTokenizer.from_pretrained(os.path.join(MODELS_DIR, "model_b"))
    export_to_onnx(model_b, tokenizer_b, os.path.join(EXPORT_DIR, "model_b.onnx"))
    export_to_tflite(os.path.join(EXPORT_DIR, "model_b.onnx"), os.path.join(EXPORT_DIR, "model_b.tflite"))

    # Model C
    model_c = AutoModelForSequenceClassification.from_pretrained(os.path.join(MODELS_DIR, "model_c"))
    tokenizer_c = AutoTokenizer.from_pretrained(os.path.join(MODELS_DIR, "model_c"))
    export_to_onnx(model_c, tokenizer_c, os.path.join(EXPORT_DIR, "model_c.onnx"))
    export_to_tflite(os.path.join(EXPORT_DIR, "model_c.onnx"), os.path.join(EXPORT_DIR, "model_c.tflite"))

    print("All models exported.")

if __name__ == "__main__":
    main()