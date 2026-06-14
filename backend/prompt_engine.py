def build_prompt(req):
    return f"""
Animate the uploaded subject into a {req.style} dance video.

Facial expression: {req.expression}
Background: {req.background}
Camera movement: {req.camera}
Aspect ratio: {req.aspect_ratio}
Effects: {", ".join(req.effects)}

Requirements:
- smooth full body motion
- realistic physics
- cinematic lighting
- ultra detailed 4K output
- synchronized dance performance
"""
