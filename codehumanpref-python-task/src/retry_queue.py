from collections import deque


class RetryQueue:
    """Queue jobs for retry with a simple delay value."""

    def __init__(self) -> None:
        self._queue = deque()
        self._attempts: dict[str, int] = {}

    def schedule_retry(self, job_id: str) -> dict[str, int | str]:
        attempt = self._attempts.get(job_id, 0) + 1
        self._attempts[job_id] = attempt

        # BUG: delay grows linearly instead of exponentially.
        delay = min(attempt, 60)

        item = {"job_id": job_id, "delay": delay}
        # BUG: duplicate entries for the same job can be queued.
        self._queue.append(item)
        return item

    def pop_next(self) -> dict[str, int | str] | None:
        if not self._queue:
            return None
        return self._queue.popleft()

    def pending(self) -> list[dict[str, int | str]]:
        return list(self._queue)
