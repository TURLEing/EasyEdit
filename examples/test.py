from transformers import AutoTokenizer

# 使用模型名称加载 tokenizer
model_name = "/mnt/16t/share/chatglm4-9b"  # 替换为你想要查看的模型
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
print(tokenizer.mergeable_ranks)
