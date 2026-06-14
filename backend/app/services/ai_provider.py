import os

def generate_video(prompt: str):
    provider = os.getenv("AI_PROVIDER", "mock")

    # 🔥 MOCK MODE (safe default)
    if provider == "mock":
        return {
            "video_url": "https://demo-video.com/fake.mp4",
            "status": "mock_success",
            "prompt": prompt
        }

    # 🔌 RUNWAY / PIKA READY HOOK
    if provider == "runway":
        # Replace with real API call
        return {
            "video_url": "https://runway.fake/video.mp4",
            "status": "runway_called",
            "prompt": prompt
        }

    return {"error": "Invalid AI provider"}
