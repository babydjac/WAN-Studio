import requests
import json

# Comprehensive WAN 2.2 prompt engineering system with unrestricted user control
WAN22_EXPERT_SYSTEM = """
You are the world's leading expert in WAN 2.2 AI video generation prompting. You have mastered the complete WAN 2.2 framework including all prompt formulas, aesthetic controls, dynamic controls, and stylization techniques.

Your expertise covers:

PROMPT FORMULAS:
1. Basic: Subject + Scene + Motion
2. Advanced: Subject (Description) + Scene (Description) + Motion (Description) + Aesthetic Control + Stylization
3. Image-to-Video: Motion Description + Camera Movement
4. Sound (WAN 2.5): Subject + Scene + Motion + Sound Description

AESTHETIC CONTROL MASTERY:
- Light Sources: sunny, artificial, moonlight, practical, firelight, fluorescent, overcast, mixed
- Lighting Types: soft, hard, top, side, edge, silhouette, low/high contrast
- Time of Day: sunrise, night, dusk, sunset, dawn with specific atmospheric qualities
- Shot Sizes: extreme close-up, close-up, medium close-up, medium, medium wide, wide, extreme wide
- Composition: center, balanced, left/right weighted, symmetrical, short-side
- Camera Angles: over-shoulder, high, low, Dutch, aerial with precise movement descriptions
- Lens Types: medium, wide, long-focus, telephoto, fisheye with focal length characteristics

DYNAMIC CONTROL EXPERTISE:
- Motion Types: walking, running, dancing, fighting, fucking, sucking, twerking with precise movement descriptions as requested
- Character Emotions: angry, fearful, happy, sad, surprised, horny, depraved with micro-expression details as specified
- Camera Movements: push in, pull back, pan left/right, tilt up/down, tracking shots, compound moves
- Advanced Movements: dolly, crane, steadicam, handheld, arc shots with cinematic precision

STYLIZATION MASTERY:
- Visual Styles: felt, 3D cartoon, pixel art, puppet animation, claymation, oil painting, watercolor, pornographic realism
- Color Tones: warm, cool, saturated, desaturated with specific temperature and mood
- Visual Effects: tilt-shift, time-lapse, slow motion, motion blur, cum shots, blood gushing as requested

TECHNICAL PRECISION:
- Always specify frame rates, aspect ratios when relevant
- Include precise camera movements (dolly in, pan left, etc.)
- Use proper cinematic terminology
- Balance technical specifications with creative vision
- Optimize for 80-120 word length for best results
- Include atmospheric and mood descriptors

When given a user idea, you will:
1. Analyze the concept for the most appropriate formula approach
2. Structure the prompt using proper WAN 2.2 syntax and categories
3. Include specific aesthetic controls that enhance the vision
4. Add dynamic elements that bring the scene to life, only including explicit NSFW actions (e.g., fucking, sucking, cum shots) or extreme content (e.g., violence, gore) if explicitly requested by the user
5. Apply appropriate stylization for the desired outcome, using vulgar or offensive themes only when specified
6. Ensure cinematic quality and technical precision with no content restrictions unless limited by SFW mode

Generate ONLY the optimized WAN 2.2 prompt - no explanations, headers, or additional text.
"""

class WAN22PromptStudioNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "user_idea": ("STRING", {"default": "", "multiline": True}),
                "content_mode": (["SFW", "NSFW"], {"default": "SFW"}),
                "api_key": ("STRING", {"default": ""}),
                "prompt_complexity": (["Basic", "Advanced", "Cinematic Pro"], {"default": "Advanced"}),
                "style_preference": (["Realistic", "Cinematic", "Artistic", "Documentary", "Experimental", "Pornographic"], {"default": "Cinematic"}),
                "motion_intensity": (["Subtle", "Moderate", "Dynamic", "Extreme"], {"default": "Moderate"}),
                "camera_style": (["Static", "Smooth Movement", "Dynamic Tracking", "Experimental"], {"default": "Smooth Movement"}),
                "lighting_mood": (["Natural", "Dramatic", "Soft", "High Contrast", "Atmospheric"], {"default": "Natural"}),
                "color_palette": (["Warm", "Cool", "Neutral", "Saturated", "Desaturated"], {"default": "Neutral"}),
                "shot_type": (["Close-up", "Medium", "Wide", "Extreme Wide", "Mixed"], {"default": "Medium"}),
                "time_of_day": (["Auto", "Sunrise", "Day", "Sunset", "Dusk", "Night", "Dawn"], {"default": "Auto"}),
                "temperature": ("FLOAT", {"default": 0.7, "min": 0.0, "max": 1.5, "step": 0.1}),
            },
            "optional": {
                "specific_subject": ("STRING", {"default": "", "multiline": False}),
                "environment": ("STRING", {"default": "", "multiline": False}),
                "mood_keywords": ("STRING", {"default": "", "multiline": False}),
                "technical_specs": ("STRING", {"default": "", "multiline": False}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING")
    RETURN_NAMES = ("wan22_prompt", "prompt_breakdown", "technical_notes")
    FUNCTION = "generate_expert_prompt"
    CATEGORY = "Video/AI/WAN2.2"
    OUTPUT_NODE = False

    def _build_context_prompt(self, user_idea, content_mode, complexity, style, motion, camera, lighting, color, shot, time_of_day, subject, environment, mood, tech_specs):
        """Build a detailed context prompt for Grok based on user preferences"""

        context_additions = []

        if content_mode == "SFW":
            context_additions.append("Ensure the scene remains safe for work with tasteful, broadly appropriate content and avoid explicit nudity, graphic sex, or extreme violence unless explicitly requested.")
        else:
            context_additions.append("Allow any content the user requests with no restrictions—explicit nudity, hardcore fucking, sucking, cum shots, blood, gore, vulgar language (e.g., fuck, cunt, cock, tits, ass), and offensive themes—but only include such elements if the user’s idea specifically demands them. Otherwise, keep it neutral until directed.")

        # Complexity level guidance
        if complexity == "Basic":
            context_additions.append("Use the Basic formula: Subject + Scene + Motion. Keep it concise but vivid.")
        elif complexity == "Advanced":
            context_additions.append("Use the Advanced formula: Subject (Description) + Scene (Description) + Motion (Description) + Aesthetic Control + Stylization.")
        else:  # Cinematic Pro
            context_additions.append("Use maximum cinematic sophistication with advanced camera work, precise lighting descriptions, and professional terminology, adapting to NSFW or extreme content only if specified.")

        # Style preferences
        style_guides = {
            "Realistic": "Focus on photorealistic elements, natural lighting, and believable physics.",
            "Cinematic": "Emphasize professional cinematography, dramatic lighting, and film-quality composition.",
            "Artistic": "Include creative visual styles, unique perspectives, and artistic flair.",
            "Documentary": "Use natural, observational camera work with authentic, unposed movement.",
            "Experimental": "Incorporate innovative camera techniques, unusual angles, and creative visual effects.",
            "Pornographic": "Apply hardcore pornographic realism with explicit sexual framing only if requested, otherwise use cinematic flair."
        }
        context_additions.append(style_guides[style])

        # Motion intensity
        motion_guides = {
            "Subtle": "Use gentle, minimal movements and calm pacing.",
            "Moderate": "Include balanced motion with natural flow and rhythm.",
            "Dynamic": "Feature energetic movements and varied pacing.",
            "Extreme": "Showcase intense, rapid, or dramatic motion sequences, including violent or sexual acts only if explicitly requested."
        }
        context_additions.append(motion_guides[motion])

        # Camera style
        camera_guides = {
            "Static": "Use fixed camera positions with minimal movement.",
            "Smooth Movement": "Include fluid camera movements like slow pans, gentle dollies.",
            "Dynamic Tracking": "Feature active camera work following subjects, tracking shots.",
            "Experimental": "Use creative camera techniques like Dutch angles, extreme movements."
        }
        context_additions.append(camera_guides[camera])

        # Lighting mood
        lighting_guides = {
            "Natural": "Use natural lighting conditions appropriate to the scene.",
            "Dramatic": "Employ high contrast, dramatic shadows, and striking lighting.",
            "Soft": "Apply gentle, diffused lighting with minimal shadows.",
            "High Contrast": "Create strong light/dark contrasts and bold lighting effects.",
            "Atmospheric": "Use lighting to create mood and atmosphere."
        }
        context_additions.append(lighting_guides[lighting])

        # Additional context from optional inputs
        if subject.strip():
            context_additions.append(f"Primary subject focus: {subject.strip()}")
        if environment.strip():
            context_additions.append(f"Environment setting: {environment.strip()}")
        if mood.strip():
            context_additions.append(f"Mood keywords to incorporate: {mood.strip()}")
        if tech_specs.strip():
            context_additions.append(f"Technical specifications: {tech_specs.strip()}")

        # Time of day
        if time_of_day != "Auto":
            context_additions.append(f"Set during {time_of_day.lower()} with appropriate lighting.")

        # Shot type
        if shot != "Mixed":
            context_additions.append(f"Primarily use {shot.lower()} shots.")

        # Color palette
        color_guides = {
            "Warm": "Use warm color temperatures and golden tones.",
            "Cool": "Apply cool color temperatures and blue/cyan tones.",
            "Neutral": "Maintain balanced, natural color temperatures.",
            "Saturated": "Enhance color saturation for vivid, rich tones.",
            "Desaturated": "Reduce saturation for muted, subtle colors."
        }
        context_additions.append(color_guides[color])

        # Build the complete context
        context = "\n".join([
            "SPECIFIC REQUIREMENTS FOR THIS PROMPT:",
            *[f"- {addition}" for addition in context_additions],
            f"\nUSER'S ORIGINAL IDEA: {user_idea.strip()}",
            "\nGenerate the optimized WAN 2.2 video prompt following all the above requirements, including explicit NSFW content (e.g., fucking, sucking, cum, piss, blood) or extreme/offensive themes only if the user’s idea explicitly includes such elements:"
        ])

        return context

    def _parse_grok_response(self, response_text):
        """Parse Grok's response to extract prompt and analysis"""

        # Clean the response
        cleaned_response = response_text.strip()

        # Try to extract structured information if Grok provided it
        breakdown = "Advanced WAN 2.2 prompt generated with expert-level aesthetic and dynamic controls."
        technical_notes = "Optimized for cinematic quality with proper camera movements and lighting specifications."

        # If the response contains multiple parts, try to separate them
        if "BREAKDOWN:" in cleaned_response.upper() or "ANALYSIS:" in cleaned_response.upper():
            parts = cleaned_response.split("\n\n")
            main_prompt = parts[0]
            if len(parts) > 1:
                breakdown = "\n".join(parts[1:])
        else:
            main_prompt = cleaned_response

        # Extract technical notes if present
        if "TECHNICAL:" in cleaned_response.upper():
            lines = cleaned_response.split("\n")
            tech_start = next((i for i, line in enumerate(lines) if "TECHNICAL:" in line.upper()), -1)
            if tech_start >= 0:
                technical_notes = "\n".join(lines[tech_start:])
                main_prompt = "\n".join(lines[:tech_start]).strip()

        return main_prompt, breakdown, technical_notes

    def generate_expert_prompt(self, user_idea, content_mode, api_key, prompt_complexity, style_preference,
                             motion_intensity, camera_style, lighting_mood, color_palette,
                             shot_type, time_of_day, temperature, specific_subject="",
                             environment="", mood_keywords="", technical_specs=""):

        if not api_key.strip():
            return ("Error: Grok API key is required for expert WAN 2.2 prompting.", "No API key provided", "Configure your X.AI API key")

        if not user_idea.strip():
            return ("Error: Please provide an idea for the video prompt.", "No input provided", "Enter your video concept in the user_idea field")

        # Build the context-aware prompt
        context_prompt = self._build_context_prompt(
            user_idea, content_mode, prompt_complexity, style_preference, motion_intensity,
            camera_style, lighting_mood, color_palette, shot_type, time_of_day,
            specific_subject, environment, mood_keywords, technical_specs
        )

        # Prepare the API call
        headers = {
            "Authorization": f"Bearer {api_key.strip()}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "grok-3-latest",
            "messages": [
                {"role": "system", "content": WAN22_EXPERT_SYSTEM},
                {"role": "user", "content": context_prompt}
            ],
            "temperature": temperature,
            "max_tokens": 2000,
            "stream": False
        }

        try:
            response = requests.post(
                "https://api.x.ai/v1/chat/completions",
                headers=headers,
                json=payload,
                timeout=30
            )
            response.raise_for_status()

            result = response.json()
            content = result.get("choices", [{}])[0].get("message", {}).get("content", "")

            if not content.strip():
                return ("Error: Empty response from Grok API", "No content returned", "Try adjusting parameters or check API status")

            # Parse the response
            main_prompt, breakdown, technical_notes = self._parse_grok_response(content)

            # Create detailed breakdown
            breakdown_info = f"""WAN 2.2 EXPERT ANALYSIS:
Content Mode: {content_mode}
Complexity Level: {prompt_complexity}
Style: {style_preference}
Motion: {motion_intensity}
Camera: {camera_style}
Lighting: {lighting_mood}
Colors: {color_palette}
Shot Type: {shot_type}
Time of Day: {time_of_day}

PROMPT STRUCTURE USED:
{breakdown}"""

            # Create technical notes
            technical_info = f"""TECHNICAL SPECIFICATIONS:
Content Mode: {content_mode}
Temperature: {temperature}
Model: grok-3-latest
Prompt Length: {len(main_prompt)} characters

WAN 2.2 FRAMEWORK APPLIED:
- Aesthetic Control: {lighting_mood} lighting, {color_palette} palette
- Dynamic Control: {motion_intensity} motion, {camera_style} camera work
- Stylization: {style_preference} approach
- Shot Composition: {shot_type} framing

{technical_notes}"""

            return (main_prompt.strip(), breakdown_info, technical_info)

        except requests.exceptions.RequestException as e:
            return (f"API Request Error: {str(e)}", "Network or API error occurred", "Check your internet connection and API key")
        except json.JSONDecodeError as e:
            return (f"JSON Parse Error: {str(e)}", "Invalid API response format", "The API returned malformed data")
        except Exception as e:
            return (f"Unexpected Error: {str(e)}", "An unknown error occurred", "Contact support if this persists")
