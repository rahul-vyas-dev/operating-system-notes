# operating-system-notes
# Understanding Operating Systems

This repository is my personal knowledge base and hands-on notes as I explore the internal world of **Operating Systems** — the silent engine behind all computing.

> "Don't just write code — understand how your machine runs it."

---

#  Operating System Concepts – Deep Dive Notes

> Documenting what I learn as I dive into core OS topics — focused not just on usage, but deep understanding.

---

## Contents

- [Functionality of OS](#-what-does-an-operating-system-do)
- [Types of OS](#-types-of-operating-systems)
- [Process States](#-process-states-in-os)
- [Schedulers](#-schedulers-in-os)
- [Preemptive vs Non-Preemptive](#-preemptive-vs-non-preemptive-scheduling)
- [Developer Thoughts](#-my-thoughts)

---


##  What Does an Operating System Do?

An **Operating System (OS)** acts as an interface between the user and hardware. Its core roles:

- Managing CPU, memory, and I/O devices
- Handling processes, scheduling, and execution
- Providing user interaction (CLI/GUI)
- Ensuring file system and resource security


---

##  Types of Operating Systems

| Type                | Description |
|---------------------|-------------|
| **Batch OS**        | Groups jobs for execution without user interaction |
| **Time-Sharing OS** | Shares CPU among many users |
| **Distributed OS**  | Runs across multiple systems |
| **Real-Time OS**    | Executes tasks within time constraints |
| **Network OS**      | Manages networked computers |
| **Mobile OS**       | Built for portable smart devices |
| **Embedded OS**     | for dedicated devices |

---

## Process States in OS

A process transitions through:

- **New**
- **Ready**
- **Running**
- **Waiting/Blocked**
- **Terminated**


---

##  Schedulers in OS

### Long-Term Scheduler
- Selects jobs from disk to load into memory
- This brings all the jobs(which want to execute) into **Ready State Queue**

### Short-Term Scheduler
- Picks ready processes for CPU execution
- This brings all the jobs(which want to execute) into **Running State Queue**

---

## Preemptive vs Non-Preemptive Scheduling

| Type               | Description |
|--------------------|-------------|
| **Preemptive**     | CPU can be taken away mid-execution |
| **Non-Preemptive** | Process keeps CPU till it ends or blocks |


---

##  My Thoughts

> I explore **how and why** tools and systems work.  
> I believe understanding the **core concepts** leads to real growth.  
> I don’t chase trends or money — I build, break, and learn out of **passion**.  
>  
> Developers are everywhere — but I strive to be one who builds **with purpose**, explores deeply, and shares consistently.

---

##  Contributions

Feel free to fork, clone, and contribute if you're learning OS too!

---
