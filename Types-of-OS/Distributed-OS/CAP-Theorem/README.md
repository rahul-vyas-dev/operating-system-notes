# CAP Theorem in Distributed Systems  

Distributed systems are everywhere — from cloud databases to microservices. But they come with trade-offs that developers must understand. That’s where the **CAP Theorem** comes in.  

---

## 🔑 What is CAP Theorem?  
CAP stands for:  
- **C – Consistency**: Every read receives the most recent write.  
- **A – Availability**: Every request gets a response (success/failure).  
- **P – Partition Tolerance**: The system continues working even if parts of the network fail.  

👉 The theorem states that **a distributed system can only guarantee two of the three properties at the same time**.  

---

## ⚡ CAP Triangle (Visualization)  

### ASCII Representation:
           Consistency
               /\
              /  \
             /    \
            /      \
           /        \
Availability----Partition Tolerance


### Image Representation:
![CAP Theorem Triangle](https://upload.wikimedia.org/wikipedia/commons/5/5a/CAP_Theorem.png)

---

## ⚡ The Trade-offs  
- **CA (Consistency + Availability)**  
  Works well until a network partition occurs. Rare in large real-world systems.  

- **CP (Consistency + Partition Tolerance)**  
  Prioritizes correctness of data. Example: **MongoDB** (when configured for strong consistency).  

- **AP (Availability + Partition Tolerance)**  
  Keeps services running even if some data is stale. Example: **Cassandra**, **DynamoDB**.  

---

## 🛠 Example  
Imagine a distributed database spread across multiple servers.  
If the network splits (partition):  
- Choosing **Consistency** → some requests fail, but data stays correct.  
- Choosing **Availability** → all requests succeed, but some data may be outdated.  

---

## 🚀 Why It Matters?  
Whenever you design a **database, cache, or API at scale**, you’ll face CAP trade-offs.  
Understanding it helps you pick the right architecture for your project.  

---
