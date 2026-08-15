from src.retry_queue import RetryQueue


def test_first_retry_delay_is_one_second():
    queue = RetryQueue()
    assert queue.schedule_retry("job-1") == {"job_id": "job-1", "delay": 1}


def test_retry_delay_uses_exponential_backoff():
    queue = RetryQueue()
    queue.schedule_retry("job-1")
    queue.pop_next()
    assert queue.schedule_retry("job-1")["delay"] == 2
    queue.pop_next()
    assert queue.schedule_retry("job-1")["delay"] == 4
    queue.pop_next()
    assert queue.schedule_retry("job-1")["delay"] == 8


def test_retry_delay_is_capped_at_sixty_seconds():
    queue = RetryQueue()
    for _ in range(7):
        queue.schedule_retry("job-1")
        queue.pop_next()
    assert queue.schedule_retry("job-1")["delay"] == 60


def test_duplicate_pending_job_is_not_enqueued_twice():
    queue = RetryQueue()
    first = queue.schedule_retry("job-1")
    second = queue.schedule_retry("job-1")
    assert second == first
    assert queue.pending() == [first]


def test_job_can_be_scheduled_again_after_pop():
    queue = RetryQueue()
    queue.schedule_retry("job-1")
    queue.pop_next()
    item = queue.schedule_retry("job-1")
    assert item == {"job_id": "job-1", "delay": 2}
    assert queue.pending() == [item]


def test_pop_empty_queue_returns_none():
    queue = RetryQueue()
    assert queue.pop_next() is None
