# Industrial Knowledge AI API Guide

## Base URL

```
http://127.0.0.1:8000
```

---

## Health

GET /health

---

## Upload PDF

POST /upload

Form Data:

file : PDF

---

## Chat

POST /chat

Body:

{
    "question":"What is AI?"
}

---

## Clear Chat

POST /clear-chat

---

## Search

GET /search?query=factorial