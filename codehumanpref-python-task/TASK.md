# Coding Task: Fix RetryQueue backoff and duplicate scheduling

The current `RetryQueue` implementation has two behavioral defects:

1. Retry delays do not follow the required exponential backoff sequence.
2. The same job can be scheduled more than once at the same time.

## Acceptance criteria

- The first retry delay is 1 second.
- Each subsequent retry doubles the delay: 1, 2, 4, 8, ...
- Delay is capped at 60 seconds.
- Calling `schedule_retry(job_id)` repeatedly before the job is popped must not create duplicate queued entries.
- Once a job is popped, it may be scheduled again.
- Existing public method names and return shapes must remain unchanged.
- Add or update tests as needed.
- Run the full test suite and report what was verified.

Keep the change focused on this behavior; do not add unrelated features or refactor unrelated code.
