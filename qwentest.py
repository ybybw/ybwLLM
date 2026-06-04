# test.py
import requests
import json
# Ollama API 地址
OLLAMA_URL = "http://localhost:11434/api/generate"

def ask_qwen3(question):
    """向 Qwen3 模型提问"""
    data = {
        "model": "qwen3:0.6b",      # 模型名称
        "prompt": question,          # 你的问题
        "stream": False              # 不流式输出，等完整回答
    }
    
    try:
        response = requests.post(OLLAMA_URL, json=data)
        result = response.json()
        print(result)
        return result["response"]
    except Exception as e:
        return f"出错了: {e}"

# 主程序
if __name__ == "__main__":
    print("=" * 50)
    print("Qwen3 模型测试")
    print("=" * 50)
    
    # 输入问题
    question = input("\n请输入你的问题: ")
    
    print("\nAI 思考中...")
    
    # 获取回答
    answer = ask_qwen3(question)
    
    print(f"\n回答: {answer}")
    print("\n" + "=" * 50)