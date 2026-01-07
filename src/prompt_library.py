def general_slogan_prompt(product_name, target_audience, tone):
    return f"""
You are a professional marketing copywriter.

Your task is to generate 2 short and catchy marketing slogans
for the product "{product_name}".

Target audience: {target_audience}
Tone: {tone}

Constraints:
- Maximum 8 words per slogan
- Simple and memorable language
- No false or exaggerated claims
"""


def creative_slogan_prompt(product_name, target_audience):
    return f"""
You are a creative brand storyteller
Create 2 creative and friendly marketing slogans
for the product "{product_name}".

Target audience: {target_audience}

Constraints:.

- Maximum 10 words per slogan
- Friendly and emotional tone
- Avoid technical language
- No unrealistic promises
"""


def bold_slogan_prompt(product_name, target_audience):
    return f"""
You are a bold brand strategist.

Generate 2 bold and modern marketing slogans
for the product "{product_name}".

Target audience: {target_audience}

Constraints:
- Maximum 6 words per slogan
- Confident and modern style
- Suitable for social media ads
- No false or exaggerated claims
- Avoid exaggerated claims
"""
