from transformers import AutoTokenizer

# 使用模型名称加载 tokenizer
model_name = "/mnt/16t/share/chatglm4-9b"  # 替换为你想要查看的模型
tokenizer = AutoTokenizer.from_pretrained(model_name)

# 查看特殊 token ID
unk_token_id = tokenizer.unk_token_id
pad_token_id = tokenizer.pad_token_id
cls_token_id = tokenizer.cls_token_id
sep_token_id = tokenizer.sep_token_id
mask_token_id = tokenizer.mask_token_id

# 打印这些 token ID
print(f"unk_token_id: {unk_token_id}")
print(f"pad_token_id: {pad_token_id}")
print(f"cls_token_id: {cls_token_id}")
print(f"sep_token_id: {sep_token_id}")
print(f"mask_token_id: {mask_token_id}")
