# 🚀 WAN-Studio for ComfyUI: Next-Gen Grok Prompt Engineering


**WAN-Studio** is an advanced ComfyUI plugin for AI video creators and prompt engineers. Tap into X.AI's Grok-3 model for cinematic, NSFW, realistic or experimental WAN 2.2 video prompts. Everything is automated—dynamic color coding, expert system guidance, and instant API integration.

---

## ✨ Features

- **Grok-3 Powered Prompts:** WAN-Studio talks directly to Grok via secure API for world-class video formulas— far more expressive than Claude or ChatGPT.
- **Live Node Color Coding:** Your workflow instantly signals SFW/NSFW status — blue for safe, red for bold.
- **WAN 2.2 Framework:** Auto-select basic, advanced, or cinematic formulas; granular control over style, motion, camera, lighting, color, shot, time, and temperature.
- **Masked API Key Entry:** Enter your X.AI API key privately (ComfyUI's input slot or widget).
- **Context-Aware Results:** Each output includes both the finished prompt and a human-readable breakdown plus detailed technical specifications.
- **Resilient Error Handling:** If Grok or your key fails, you get direct feedback, never silent errors.

---

## 📦 Installation

```bash
git clone https://github.com/YOUR-USERNAME/WAN-Studio.git
mv WAN-Studio /path/to/ComfyUI/custom_nodes/
```

Or manually move the folder.

1. Restart ComfyUI.
2. Drop "WAN 2.2 Prompt Studio" node onto your canvas!
3. Enter your X.AI (Grok) API key securely in the node.

---

## 🕹️ Usage

- Set your `user_idea` and all creative parameters.
- SFW/NSFW mode toggles colors and prompt explicitness.
- Connect API key via widget or input node, keeping your credentials private.
- Run the node: Outputs include:
  - **Optimized WAN 2.2 prompt** for Grok-powered video generation.
  - **Prompt breakdown:** expert analysis of content, choices, style.
  - **Technical notes:** temperature, model, shot, aesthetic, dynamic details.

---

## 🧑‍💻 Code Example

Python:
```python
response = requests.post(
"https://api.x.ai/v1/chat/completions",
headers={"Authorization": f"Bearer {api_key}"},
json=payload
)
result = response.json()
```

JavaScript color logic:
```javascript
const MODE_COLORS = { SFW: { color: "#2563eb" }, NSFW: { color: "#dc2626" }};
node.color = MODE_COLORS[mode].color;
```

---

## 🧠 Why Grok?

- Access to Grok means richer, more compositional, more creative results—especially for video and NSFW.
- Built for prompt engineers and artists who need technical control.

---

## 🏷️ Credits
Made by [Your Name]  
Powered by X.AI Grok, WAN 2.2, and ComfyUI.

---

## 📖 License

MIT — see [LICENSE](LICENSE).

---

## 🤝 Contributing

PRs, feature requests, and bug reports always welcome!
