
---

### 10. `setup.sh`

```bash
#!/bin/bash
echo "🔧 Setting up environment..."
uv venv
source .venv/bin/activate
uv pip install fastapi uvicorn pydantic pytest httpx
echo "✅ Done. To run the app: uvicorn app.main:app --reload"
