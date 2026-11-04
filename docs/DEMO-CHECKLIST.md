# Demo 素材拍摄清单

> 按截图原则1：先展示 Use Case，最好附上 GIF 或 Demo。
> README 里现在用 ASCII 代替了真实截图，下面是需要拍的素材清单。

---

## 必拍素材（按优先级排序）

### 1. Web UI 主截图（最重要）

- **拍什么**：`python app.py` 启动后的 Gradio 界面
- **问什么**：在输入框输入 "What is RAG?" 或 "How do I install Ollama?"
- **要展示的元素**：
  - 左侧对话区：用户提问 + 机器人回答 + Sources 标注
  - 右侧栏：Documents 列表 + Config 信息
- **保存为**：`docs/screenshot.jpg`（替换 README 里的 ASCII）
- **工具**：直接截图即可，建议用浅色主题
- **尺寸**：建议 1280px 宽以上，保持 UI 完整

### 2. CLI 模式 GIF 录屏

- **拍什么**：终端里运行 `python rag.py`，输入两个问题，展示回答和 sources
- **要展示的流程**：
  1. 启动 → "Indexed 12 chunks from 3 file(s)"
  2. 输入第一个问题 → 等待回答 → 显示 sources
  3. 输入第二个问题 → 显示回答
- **保存为**：`docs/cli-demo.gif`
- **工具推荐**：
  - Windows：[ScreenToGif](https://www.screentogif.com/)（免费）
  - 浏览器：[licecap](https://www.cockos.com/licecap/)
- **技巧**：
  - 终端字体调大一点（至少 14px）
  - 背景用深色主题，文字对比强
  - GIF 控制在 10 秒以内，文件大小 < 5MB
  - 可以加速打字和等待时间

### 3. 快速安装流程 GIF（可选但加分）

- **拍什么**：从 `git clone` 到第一次提问成功的完整流程
- **要展示的步骤**：
  1. `git clone ...`
  2. `pip install -r requirements.txt`
  3. `python rag.py`
  4. 第一个问题和回答
- **保存为**：`docs/quickstart.gif`
- **用途**：可以放在 README 的 Quick Start 区域，或者推 Twitter/X 用

---

## 拍摄建议

### 拍摄前准备

1. **先跑 demo 模式确认 UI 正常**：
   ```bash
   python app.py --demo
   ```
   这样不用真的装 Ollama 也能看到界面效果。

2. **准备好 sample 文档**：
   `docs/sample.txt` 里的内容要和你问的问题对应，这样回答才有说服力。

3. **清理终端环境**：
   拍之前先 `clear`，只保留必要的输出，不要有乱七八糟的历史记录。

### 拍摄技巧

- **截图比 GIF 优先级高**：先把 Web UI 截图拍好替换 README 里的 ASCII，这是最基本的
- **GIF 要短**：GitHub README 加载慢，GIF 控制在 5-10 秒，文件 < 5MB
- **加字幕或高亮**：如果录屏里打字太慢，可以后期在关键位置加箭头或标注
- **背景干净**：不要露出桌面其他窗口、通知栏等

---

## README 替换位置

拍完素材后，修改 `README.md` 里的这一段：

```markdown
> 📸 *Replace the ASCII above with a real screenshot/GIF once you've run it locally*
```

替换成类似：

```markdown
![Web UI Demo](docs/cli-demo.gif)

![Web UI Screenshot](docs/screenshot.jpg)
```

---

## 社交媒体配图

发 Reddit/HN/中文社区时，可以额外做一张：

- **对比图**：左边是"传统 RAG 教程需要装的东西"（LangChain + ChromaDB + OpenAI SDK + Docker + ...），右边是"本项目只需要 ollama + numpy"
- **工具**：Figma / 稿托 / 甚至 PPT 截图都行
- **用途**：作为帖子的配图（Reddit 和即刻都支持发图）
