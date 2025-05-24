"""
Generated Data may be destroyed, so we should recognize and delete them.
"""

import torch
import os
from tqdm import tqdm

def check_and_clean_pt_files(data_dir):

    for index in range(4):
        corrupted_files = []
        total_files = 0
        deleted_files = 0
        for filename in tqdm(os.listdir(os.path.join(data_dir, f'{index}'))):
            if filename.endswith('.ckpt'):
                total_files += 1
                file_path = os.path.join(data_dir, f'{index}', filename)
                try:
                    torch.load(file_path)
                except Exception as e:
                    print(f"[Corrupt] {file_path} -> {e}")
                    corrupted_files.append(file_path)

        print("Now we have walk through all files and recognize which is destroyed.")
        for file_path in corrupted_files:
            try:
                os.remove(file_path)
                print(f"[Deleted] {file_path}")
                deleted_files += 1
            except Exception as e:
                print(f"[Failed to delete] {file_path} -> {e}")

        print(f"\nSummary: {deleted_files} / {total_files} files were corrupted and removed.")


check_and_clean_pt_files("/deltadisk/huangjiayi/dataset/eagle/sharegpt_0_67999_mufp16")
