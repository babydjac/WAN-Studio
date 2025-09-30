# WAN 2.2 Prompt Studio

An expert WAN 2.2 video prompt generator that wraps the Grok API with deep aesthetic controls, live safety mode switching, and UI feedback inside ComfyUI. This package breaks the original node out of the BossSuperPack so you can install and maintain it independently.

## Highlights
- **Precision WAN 2.2 prompting** – Ships the full expert system prompt engineered around the official WAN 2.2 playbooks for text-to-video and image-to-video generation.
- **Instant SFW/NSFW selector** – A dedicated `content_mode` widget dials in safe-for-work or mature instructions. The node injects the correct guidance into the Grok context automatically.
- **Visual safety feedback** – The client extension recolors the node while you work: SFW = blue, NSFW = red. Reloads, queued runs, and workflow loads all keep the right palette.
- **Rich configuration surface** – Choose complexity tiers, cinematic styles, camera motion, lighting, palette, shot type, time of day, temperature, and optional subject/environment/mood/specs text.
- **Structured outputs** – Returns (1) the optimized WAN 2.2 prompt, (2) a breakdown summary including every dial you touched, and (3) technical notes with runtime metadata.
- **Standalone dependency list** – Ships a `requirements.txt` declaring `requests` to secure the Grok HTTP calls on fresh installs.

## Installation
1. Copy the `WAN22PromptStudio` folder into `ComfyUI/custom_nodes/`.
2. Install Python requirements for your ComfyUI environment:
   ```bash
   cd ComfyUI
   pip install -r custom_nodes/WAN22PromptStudio/requirements.txt
   ```
3. Restart ComfyUI so it discovers the new node and Web UI extension.

## Node Inputs
| Name | Type | Notes |
| ---- | ---- | ----- |
| `user_idea` | `STRING` (multiline) | Your raw concept for the WAN video. Required. |
| `content_mode` | `ENUM` (`SFW` / `NSFW`) | Governs safety guidance and node color. Default SFW. |
| `api_key` | `STRING` | X.AI Grok API key. Required. |
| `prompt_complexity` | `ENUM` | Switches between Basic, Advanced, and Cinematic Pro prompt structures. |
| `style_preference` | `ENUM` | Photorealistic ↔ experimental styling hints. |
| `motion_intensity` | `ENUM` | Motion pacing descriptors from subtle to extreme. |
| `camera_style` | `ENUM` | Camera language (static, smooth, tracking, experimental). |
| `lighting_mood` | `ENUM` | Lighting moods (natural, dramatic, etc.). |
| `color_palette` | `ENUM` | Warm/cool/neutral/saturated/desaturated color schemes. |
| `shot_type` | `ENUM` | Dominant framing choice (close-up → extreme wide). |
| `time_of_day` | `ENUM` | Auto or named time-of-day context. |
| `temperature` | `FLOAT` | Grok temperature knob (0.0 – 1.5). |
| `specific_subject` | `STRING` | Optional subject emphasis. |
| `environment` | `STRING` | Optional environment/location guidance. |
| `mood_keywords` | `STRING` | Emotion and vibe keywords. |
| `technical_specs` | `STRING` | Free-form technical directives (fps, aspect ratios, etc.). |

## Outputs
1. `wan22_prompt` – The fully composed WAN 2.2 prompt ready for WAN’s generator.
2. `prompt_breakdown` – Plain-text summary of every configuration choice plus the prompt structure applied.
3. `technical_notes` – Technical metadata (content mode, temperature, prompt length) with Grok-facing diagnostics.

## Safety Modes & Color Coding
- The `content_mode` toggle writes explicit safety or mature guidance into the Grok system prompt before generation.
- The web extension (`web/ui.js`) watches the widget and calls `node.setDirtyCanvas(true, true)` to repaint.
  - `SFW` → text + border color `#2563eb`, background `#0f172a`.
  - `NSFW` → text + border color `#dc2626`, background `#450a0a`.
- Colors persist across graph loads and after execution thanks to `serialize_widgets = true` and configure hooks.

## API Flow
1. The node builds a context prompt containing:
   - Safety mode clause.
   - Complexity/style/motion/camera/lighting/color guidance.
   - Optional subject/environment/mood/spec strings.
   - User idea and explicit instruction to output WAN 2.2 syntax only.
2. Sends a `POST` to `https://api.x.ai/v1/chat/completions` with `model="grok-3-latest"`, user/system messages, and the selected temperature.
3. Parses the first choice, extracting the main prompt and optionally separating breakdown/technical sections.
4. Returns user-facing breakdown and tech notes even if Grok does not provide extra metadata.

### Error Handling
- Missing API key → returns an error string guiding you to configure your key.
- Blank idea → prompts for a concept.
- HTTP, JSON, or unexpected exceptions bubble up as friendly `STRING` outputs with actionable advice.

## Workflow Tips
- Chain the prompt output directly into WAN loader nodes, a text logger, or save-to-file nodes—`OUTPUT_NODE` is `False` so sockets stay active.
- Use the `prompt_breakdown` output to display guidance in UI notes or workforce dashboards.
- Automate multiple variations by pairing with list iterators and the ComfyUI `Prompt Scheduler`—each run can flip content mode or style for A/B testing.

## Extending
- UI tweaks: edit `web/ui.js` to change colors, add badges, or emit notifications when switching modes.
- Prompt logic: adjust `_build_context_prompt` to include custom clause templates or integrate mood banks.
- Additional outputs: return quality scores or workflow tags by augmenting `RETURN_TYPES` and the Grok parser.

## Troubleshooting
- **Node stays gray**: Ensure ComfyUI restarted after install; the web extension only loads on startup.
- **Missing `requests`**: Run the pip install command above in the same Python environment that runs ComfyUI.
- **Grok rejects requests**: Verify your API key and account permissions; rate-limit errors surface inside the first output string.

---
Maintained by the WAN 2.2 Prompt Studio team. Contributions welcome—fork, patch, and submit PRs with improvements to prompt templates, UI feedback, or provider support.
