# Kokoro Serve

A lightweight Text-to-Speech server powered by **[Kokoro TTS](https://huggingface.co/hexgrad/Kokoro-82M)**.

## Usage

### Run with `uv`

```bash
uv run -m uvicorn main:app --host 0.0.0.0 --port 8000
```

### Run with Docker

```bash
docker build -t kokoro-serve .
docker run -p 8000:8000 kokoro-serve
```

## API

```bash
GET /voices

POST /generate
    body:
        {
            "text": "string"
            "voice": "string"
        }
```

### Examples

```bash
# get available voices
curl -XGET http://localhost:8000/voices
```

```bash
# run synthesis
curl -XPOST http://localhost:8000/generate \
    -H "Content-Type: application/json" \
    -d '{"text":"Hello from Kokoro Serve!", "voice": "af_heart"}' \
    -o hello.wav
```

