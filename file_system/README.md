#  File Systems (FMS) Comparison

A **File System** is the implementation of a File Management System (FMS).  
Different operating systems use different file systems to store, organize, and secure data.  

---

##  Common File Systems by OS

| Operating System | Default File System | Other Supported File Systems |
|------------------|---------------------|------------------------------|
| **Windows**      | NTFS                | FAT32, exFAT                 |
| **Linux**        | ext4                | Btrfs, XFS, ZFS              |
| **macOS**        | APFS                | HFS+                         |
| **Android**      | ext4 / F2FS         | exFAT (for SD cards)         |
| **iOS**          | APFS                | –                            |

---

##  File System Comparison Table

| File System | Used In        | Max File Size | Max Volume Size | Features | Limitations |
|-------------|---------------|---------------|----------------|----------|-------------|
| **NTFS**   | Windows        | 16 TB+        | 256 TB+        | Journaling, encryption, permissions, compression | Limited compatibility with Linux/macOS |
| **FAT32**  | Windows, USBs  | 4 GB          | 8 TB           | High compatibility, simple | No security, no journaling, 4 GB file limit |
| **exFAT**  | Windows, macOS, USBs | 16 EB | 128 PB | Good for external drives, no 4 GB limit | No journaling, weaker data recovery |
| **ext4**   | Linux          | 16 TB         | 1 EB           | Journaling, large file support, stable | Not natively supported on Windows/macOS |
| **Btrfs**  | Linux          | 16 EB         | 16 EB          | Snapshots, RAID, self-healing | Still considered experimental in some distros |
| **XFS**    | Linux          | 8 EB          | 8 EB           | High performance, journaling | No shrink support, complex recovery |
| **ZFS**    | Linux, FreeBSD | 16 EB+        | 16 EB+         | RAID, snapshots, checksums, self-healing | High memory usage, license issues |
| **APFS**   | macOS, iOS     | 8 EB          | 8 EB           | SSD-optimized, cloning, snapshots, encryption | Limited backward compatibility |
| **HFS+**   | Older macOS    | 8 EB          | 8 EB           | Journaling, metadata support | Slower than APFS, outdated |
| **F2FS**   | Android        | 16 TB+        | 16 TB+         | Flash-optimized (NAND/SSD), fast writes | Limited OS support |

---

##  Key Takeaways
- **Windows** prefers **NTFS** (secure, modern).  
- **Linux** mainly uses **ext4**, but advanced users also choose **Btrfs/ZFS**.  
- **macOS/iOS** rely on **APFS**, optimized for SSDs and mobile devices.  
- **Portable drives (USB/SD)** often use **FAT32 or exFAT** for compatibility.  

---

#  Conclusion
The choice of File System depends on:  
- **Device type** (SSD, HDD, USB, SD card)  
- **Operating System**  
- **Features needed** (security, speed, compatibility)  

A good File Management System ensures **reliability, security, and efficiency** of data storage.  
