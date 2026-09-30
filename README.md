# Modern Web Application Development Book (English + Roman Urdu)
Created by Maria Hussain.

## Local
    npm install
    npm run build && npm run serve   # dono languages, dropdown ke sath
    npm start                        # English (edit karte waqt)

## Chatbot (AI tutor)
Vercel env variables: GEMINI_API_KEY, QDRANT_URL, QDRANT_API_KEY
(optional) QDRANT_COLLECTION - default "webbook", AI-DS book ke collection se alag hai.
Local par wahi variables set karke:  pip install httpx  &&  python scripts/ingest.py

## Content
English: docs/   |   Roman Urdu: i18n/ur-Latn/docusaurus-plugin-content-docs/current/
scripts/gen_content.py sirf draft banata hai, dobara chalane se edits overwrite hongi.
