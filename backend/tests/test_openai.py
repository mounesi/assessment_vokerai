import openai
from backend.config import OPENAI_API_KEY

def test_openai_connection():
    assert OPENAI_API_KEY is not None, "OPENAI_API_KEY is not set"
    
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",  # Or "gpt-3.5-turbo"
            messages=[{"role": "user", "content": "Say hello"}]
        )
        
        assert response is not None
        assert len(response.choices) > 0
        
        message = response.choices[0].message
        assert message is not None
        assert message.content is not None
        assert "hello" in message.content.lower()

    except Exception as e:
        assert False, f"OpenAI call failed with error: {e}"
