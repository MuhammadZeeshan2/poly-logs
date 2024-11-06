#!/bin/bash
source venv/bin/activate
# uvicorn app:app --host 0.0.0.0 --port "${SERVER_PORT}" --reload
uvicorn app:app --host 127.0.0.1 --port 7000 --reload

