# 📝 Web-Task-Tracker (Python HTTP + SQLite — No External Packages)

Build a fully working backend for a To-Do List app using **only built-in Python modules** — no frameworks, no pip install, no shortcuts. You’ll use `http.server` for routing, `sqlite3` for data, and `json/urllib` for request/response handling.

**Frontend**: Simple HTML/CSS interface to interact with the API.

---

## 📦 Stack Requirements

| Tool           | Use                            |
| -------------- | ------------------------------ |
| Python         | Core language                  |
| `http.server`  | Handling HTTP requests         |
| `sqlite3`      | Embedded database (no server)  |
| `json`         | Reading and writing JSON       |
| `urllib.parse` | Parsing URLs and query strings |

✅ No Flask. No Django. No FastAPI. No ORM. Just **pure code**.

---

## 📁 Project Structure

```Structure

Web-Task-Tracker/
├── server.py
├── db.py
├── README.md
├── static
│   ├── index.html
│   └── style.css
└── utils.py

```

---

## Installation & Run Instructions

```bash
git clone git@github.com:Abdalr7man-ctrl/To-Do-List.git
cd ./To-Do-List/Web-Task-Tracker
python server.py
```

---

## 🧪 Sample API Test Cases

### ✅ Create Task

```bash
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Do homework"}'
```

### 📄 List All Tasks

```bash
curl http://localhost:8000/tasks
```

### 🔍 Filter Completed Tasks

```bash
curl "http://localhost:8000/tasks?completed=true"
```

### 🔧 Update Task (mark as complete)

```bash
curl -X PUT http://localhost:8000/tasks/1
```

### 🗑️ Delete Task

```bash
curl -X DELETE http://localhost:8000/tasks/1
```

---
