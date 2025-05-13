from agno.playground import serve_playground_app
from agno_playground.app import app

if __name__ == "__main__":
    # Note: The path to the app is now 'agno_playground.app:app'
    # if you run this main.py directly.
    # If you use a command like `python -m uvicorn main:app --reload`,
    # ensure your PYTHONPATH is set up correctly or run from the `agno` directory.
    # For simplicity with `serve_playground_app`, it expects a module path.
    serve_playground_app("agno_playground.app:app", reload=True)
