# Process vs Thread

| Feature              | Process                          | Thread                       |
|----------------------|----------------------------------|------------------------------|
| Memory Space         | Separate                        | Shared within the process    |
| Creation Overhead    | High                            | Low                          |
| Communication        | Inter-Process Communication     | Shared memory                |
| Isolation            | Strong                          | Weak                         |
| Context Switching    | Slower                          | Faster                       |
| Example              | Chrome app, VS Code             | Chrome tabs, VS Code plugins |

## Summary
- **Processes**: Independent programs, heavier, isolated.
- **Threads**: Lighter, share resources, faster but less isolated.
