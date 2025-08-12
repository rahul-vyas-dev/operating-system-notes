# Deadlock Ignorance

**Idea:**  
Ignore the problem entirely, assuming deadlocks are rare.

---

## Example: UNIX
Many general-purpose OS like UNIX and Windows take this approach for certain resources because:
- Deadlocks are rare in typical usage.
- Overhead of prevention/avoidance is high.

---

## Drawback
If a deadlock occurs, the only recovery might be:
- Restarting the application.
- Restarting the system.

---

### Analogy
Like not carrying an umbrella because it "almost never rains"—works fine until it does rain.
