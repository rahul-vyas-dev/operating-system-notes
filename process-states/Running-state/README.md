# Running State

A process in the **Running** state is actively using the CPU.

## Key Points
- Only one process per CPU core can be running at a time.
- All CPU instructions are being executed for this process.
- Process can switch to waiting or ready state depending on events.

## Example
When a text editor is responding to your typing, it’s in the running state.

## Transition
- **Running** → **Waiting**: If the process requests I/O.
- **Running** → **Ready**: If CPU is taken away by scheduler.
