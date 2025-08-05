# Independent Process

## **Definition**
- **Does not interact** with other processes  
- No **data sharing**  
- Execution result of one process does **not affect** another  

---

## **Examples**
- Calculator app running alongside a music player  
- Text editor running while downloading a file in the background  

---

## **Gantt Chart Example**
### Independent Processes (Run in Parallel, No Communication)
```mermaid
gantt
    dateFormat  mm
    axisFormat  %M
    title Independent Processes
    section Independent
    Process P1 :a1, 00, 10m
    Process P2 :a2, 00, 10m
