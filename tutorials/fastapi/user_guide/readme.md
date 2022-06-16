### Start
```bash
uvicorn main:app --reload
```

- `main`: the file `main.py` (the Python "module").
- `app`: the object created inside of `main.py` with the line `app = FastAPI()`
- `--reload`: make the server restart after code changes. Only use for development.

### API Documentation
`127.0.0.1:8000/docs` opens interactive API documentation by Swagger UI or `http://127.0.0.1:8000/redoc` for alternative documentation via ReDoc.

### Operators
Common:
- `@app.post()`
- `@app.put()`
- `@app.delete()`

Others:
- `@app.options()`
- `@app.head()`
- `@app.patch()`
- `@app.trace()`
