
```markdown
# Operating System – Cooperating Process
```

## **Definition**
- **Works with other processes** for a common goal  
- Shares **data and resources**  
- Requires **synchronization** to avoid conflicts  

---

## **Examples**
- Web server process + database process working together  
- Video streaming service (video decoding + buffering process)  

---

## **Gantt Chart Example**
### Cooperating Processes (Need Coordination)
```mermaid
gantt
    dateFormat  mm
    axisFormat  %M
    title Cooperating Processes
    section Cooperating
    Process P1 :a1, 00, 03m
    Process P2 :a2, 03, 03m
    Process P1 (Resume) :a3, 06, 03m
    Process P2 (Resume) :a4, 09, 03m
