# Waiting (Blocked) State

In the **Waiting** state, a process cannot continue until a specific event occurs.

## Key Points
- Waiting for I/O completion or a signal.
- Does not use CPU time while waiting.
- Moves to ready state once event occurs.

## Example
A program waiting for data from disk.

## Transition
- **Waiting** → **Ready**: After I/O completion.
