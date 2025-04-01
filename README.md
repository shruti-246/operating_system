# Operating Systems - Course Assignments

This repository contains several assignments completed as part of an **Operating Systems** course. Each file demonstrates key OS concepts like process synchronization, memory management, and file system simulation, using a mix of **Python**, **C**, and **C++**.

These programs were built to understand low-level system behavior and algorithms that form the backbone of modern operating systems.

---

## 📂 File Overview

- **FSS.py**  
  Simulates a basic file system to demonstrate directory/file creation and file operations.

- **Simulated_OS.py**  
  Simulates an operating system environment with basic scheduling or memory tasks (depending on implementation).

- **Synchronized_Processes.c**  
  Demonstrates synchronization between multiple processes using mutex/semaphore logic.

- **producer.cpp & consumer.cpp**  
  Classic **Producer-Consumer Problem** using thread synchronization with a bounded buffer.

- **tlb.py**  
  Simulates a **Translation Lookaside Buffer (TLB)** mechanism for virtual memory management.

---

## 🔧 Technologies Used

- **Python 3.10+**
- **C (GCC)**
- **C++ (G++)**

---

## 🚀 How to Run

### 🐍 Python Files
Run any Python script using:
```bash
python filename.py

### C Files
Run any C script using:
```bash
gcc Synchronized_Processes.c -o sync
./sync

### C++ Files
Run any C++ script using:
```bash
g++ producer.cpp -o producer
g++ consumer.cpp -o consumer
./producer
./consumer
