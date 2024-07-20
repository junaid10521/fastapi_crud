from dotenv import load_dotenv
import os
import uvicorn


def run_server():
    load_dotenv()

    host = os.getenv("HOST")
    port = int(os.getenv("PORT"))

    print(f"Starting server on {host}:{port}")
    uvicorn.run("src:app", host=host, port=port, reload=True)


if __name__ == "__main__":
    run_server()
