# Process States in Operating Systems

In an Operating System, a **process** changes its state during its lifetime.  
The OS manages these states to ensure efficient execution.

This section covers:
1. [New](New-state) – Process creation
2. [Ready](Ready-state) – Waiting for CPU allocation
3. [Running](Running-state) – Executing on CPU
4. [Waiting](Waiting-state) – Waiting for I/O or event
5. [Terminated](Terminated-state) – Process completed
6. [Suspended](Suspended-state) – Process completed

 See each file for detailed explanations and examples.

## Visual Diagram
See [Process State Diagram](process-states-diagram.md) for a visual representation.

# Process State Diagram

```mermaid
stateDiagram-v2
    [*] --> New
    New --> Ready
    Ready --> Running
    Running --> Waiting
    Waiting --> Ready
    Running --> Terminated
