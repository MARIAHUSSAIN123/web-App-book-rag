import os, json, time, httpx
from http.server import BaseHTTPRequestHandler

G = os.environ["GEMINI_API_KEY"]
QURL, QKEY = os.environ["QDRANT_URL"].rstrip("/"), os.environ["QDRANT_API_KEY"]
BASE = "https://generativelanguage.googleapis.com/v1beta/models"
# Pehla model busy ho to agla try hota hai. Vercel env GEMINI_MODEL mein comma se naam de sakte hain.
COLL = os.environ.get("QDRANT_COLLECTION", "webbook")  # AI-DS book ke collection se alag
MODELS = [m.strip() for m in os.environ.get("GEMINI_MODEL", "gemini-3.5-flash,gemini-3.1-flash-lite,gemini-2.5-flash").split(",") if m.strip()]

SYSTEM = """You are a friendly, expert web development mentor for students of a 12-month "Modern Web Application Development" course (HTML, CSS, Bootstrap, JavaScript, TypeScript, React, Redux, Next.js, Node.js, Express, MongoDB, PostgreSQL, GraphQL, Docker, CI/CD).
You receive BOOK CONTEXT (course outline excerpts) and the recent chat.

Rules:
1. If the topic is in the book context, say in one line which module it belongs to.
2. Then TEACH it properly with your own knowledge, like a patient teacher for a beginner: simple definition, why it matters, a real-life analogy, step-by-step explanation, a complete small working code example with comments, common mistakes, and one small practice task.
3. Reply in the student's language: English, or Roman Urdu (Urdu written in English letters) if they write Roman Urdu. If they ask for both, give English first, then Roman Urdu. Keep code and technical terms in English.
4. Follow-ups like "isky bary mein", "example do", "explain more" refer to the previous topic in the chat.
5. Format: plain text, **bold** for key terms, "- " bullets, code in triple-backtick fences. No markdown headers or tables.
6. For greetings, reply in one or two friendly lines and suggest a few course topics to start with.
7. If the question is not about programming or this course, politely steer back to the course."""


def generate(payload):
    """Busy/limit errors par retry aur backup models. (data, error) return karta hai."""
    start, last = time.time(), "unknown error"
    for model in MODELS:
        for attempt in range(2):
            if time.time() - start > 42:
                return None, last
            try:
                data = httpx.post(f"{BASE}/{model}:generateContent?key={G}", json=payload, timeout=25).json()
            except Exception as e:
                last = str(e)
                time.sleep(1)
                continue
            if "candidates" in data:
                return data, None
            err = data.get("error", {})
            last = err.get("message") or str(data.get("promptFeedback") or data)
            code = err.get("code")
            if code in (429, 500, 503, 504):
                time.sleep(1.2)
                continue          # dobara try, phir agla model
            if code == 404:
                break             # ye model nahi mila, agla try karo
            return None, last     # key ghalat / content blocked, retry ka faida nahi
    return None, last


def embed(text):
    r = httpx.post(f"{BASE}/gemini-embedding-001:embedContent?key={G}",
                   json={"content": {"parts": [{"text": text}]}, "outputDimensionality": 768}, timeout=30)
    return r.json()["embedding"]["values"]


class handler(BaseHTTPRequestHandler):
    def _send(self, code, obj):
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(obj).encode())

    def do_POST(self):
        try:
            body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
            q = body["question"]
            history = body.get("history", [])[-6:]

            # Follow-up sawalon ke liye search mein pichla user sawal bhi shamil
            prev_users = [h["text"] for h in history if h.get("role") == "user"][-2:]
            search_text = " ".join(prev_users + [q])[:1500]

            hits = httpx.post(f"{QURL}/collections/{COLL}/points/search",
                              headers={"api-key": QKEY},
                              json={"vector": embed(search_text), "limit": 6, "with_payload": True},
                              timeout=30).json().get("result", [])
            ctx = "\n\n".join(h["payload"]["text"] for h in hits) or "(nothing found)"
            chat = "\n".join(("User: " if h.get("role") == "user" else "Assistant: ") + h.get("text", "")[:600]
                             for h in history)
            prompt = f"BOOK CONTEXT:\n{ctx}\n\nRECENT CHAT:\n{chat or '(none)'}\n\nUSER'S LATEST MESSAGE: {q}"

            r, error = generate({"systemInstruction": {"parts": [{"text": SYSTEM}]},
                                 "contents": [{"role": "user", "parts": [{"text": prompt}]}],
                                 "generationConfig": {"maxOutputTokens": 2400, "temperature": 0.6}})
            if error:
                self._send(200, {"answer": "Abhi AI service busy hai, thori der baad dobara try karein. (" + error[:120] + ")"})
                return
            parts = r["candidates"][0].get("content", {}).get("parts", [])
            answer = "".join(p.get("text", "") for p in parts) or "Jawab nahi mila, dobara try karein."
            self._send(200, {"answer": answer})
        except Exception as e:
            self._send(500, {"answer": "Server error: " + str(e)})
