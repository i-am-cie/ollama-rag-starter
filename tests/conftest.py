import os
import sys
import types

# 把仓库根目录加入导入路径，便于直接 import rag
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

# 测试环境通常不安装 ollama，这里注入占位模块，使导入 rag 不依赖网络/第三方包。
# 真正的 embed/chat 调用在测试中通过 patch rag.ollama.embed / rag.ollama.chat 打桩。
try:
    import ollama  # noqa: F401
except ImportError:
    ollama_mod = types.ModuleType("ollama")
    ollama_mod.embed = None
    ollama_mod.chat = None
    sys.modules["ollama"] = ollama_mod
