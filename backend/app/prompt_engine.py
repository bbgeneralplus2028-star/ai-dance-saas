def build_prompt(data):
    return f"""
AI Dance Video Generation:

Style: {data.get('style')}
Expression: {data.get('expression')}
Background: {data.get('background')}
Camera: {data.get('camera')}
Effects: {data.get('effects')}

Rules:
- Keep identity consistent
- Smooth motion
- Cinematic lighting
- High realism
- Social media optimized vertical video
"""
