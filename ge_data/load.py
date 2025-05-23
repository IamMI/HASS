from datasets import load_dataset
import json

dataset = load_dataset("anon8231489123/ShareGPT_Vicuna_unfiltered", split="train")
dataset = dataset.select(range(68000))  # 只取前 68000 条

with open("/deltadisk/huangjiayi/dataset/eagle/sharegpt_68000.json", "w", encoding="utf-8") as f:
    for sample in dataset:
        f.write(json.dumps(sample, ensure_ascii=False) + "\n")