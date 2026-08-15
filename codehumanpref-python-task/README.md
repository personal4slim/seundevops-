# Retry Queue Task

A small Python project used to exercise code review, debugging, testing, and implementation behavior.

## What it does

`RetryQueue` stores jobs that may be retried after failures. Each retry should be scheduled using exponential backoff and jobs must not be duplicated in the queue.

## Run tests

```bash
python -m pytest -q
```

## Project layout

- `src/retry_queue.py` — queue implementation
- `tests/test_retry_queue.py` — behavioral tests
- `TASK.md` — requested coding task and acceptance criteria

Python 3.11+ is recommended.
