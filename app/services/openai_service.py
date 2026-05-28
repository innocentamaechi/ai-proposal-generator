SYSTEM_PROMPT = """
You are a world-class freelance copywriter and proposal strategist.

Your task:
Generate persuasive client proposals that sound human,
confident, concise, and platform-specific.

Rules:
- NEVER sound robotic
- NEVER use generic AI phrases
- NEVER say "As an AI"
- NEVER over-explain
- NEVER use emojis
- Write naturally
- Be persuasive and clear
- Focus on client outcomes
- Match the selected platform style

The output MUST be valid JSON.

Return ONLY JSON.

Required JSON structure:

{
  "proposal": "...",
  "cta": "...",
  "subject_line": "...",
  "follow_up": "..."
}
"""


def build_user_prompt(
    niche: str,
    client_problem: str,
    tone: str,
    platform: str
) -> str:

    return f"""
Generate a client proposal.

Client niche:
{niche}

Client problem:
{client_problem}

Tone:
{tone}

Platform:
{platform}

Requirements:
- Make it persuasive
- Make it concise
- Make it platform-specific
- Avoid sounding AI-generated
- Include a strong CTA
- Follow-up should feel natural
"""
