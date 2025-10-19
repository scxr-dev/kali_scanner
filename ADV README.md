# **Localhost Port Scanner for Penetration Testers**

A foundational, high-performance TCP port scanner written in Python, optimized for local reconnaissance on a Kali Linux environment. This project serves as an educational tool to demonstrate the core principles of network scanning and system enumeration in a controlled, safe-to-operate manner.

## **Table of Contents**

1. [About The Project](https://www.google.com/search?q=%23about-the-project)  
2. [Core Functionality](https://www.google.com/search?q=%23core-functionality)  
3. [Getting Started](https://www.google.com/search?q=%23getting-started)  
4. [How to Use and Test the Tool](https://www.google.com/search?q=%23how-to-use-and-test-the-tool)  
5. [Troubleshooting](https://www.google.com/search?q=%23troubleshooting)  
6. [License](https://www.google.com/search?q=%23license)  
7. [Creator](https://www.google.com/search?q=%23creator)

### **About The Project**

In penetration testing, the initial phase of reconnaissance is critical. Understanding the attack surface of a target begins with identifying open ports and running services. This project provides a simple yet effective script to perform this fundamental task on the local machine (127.0.0.1), allowing aspiring security professionals to understand the mechanics of a port scan without legal or ethical risks.

The script leverages Python's native socket library to attempt connections on a specified range of TCP ports, reporting back which ports are in a LISTENING state.

### **Core Functionality**

* **Socket Programming:** Utilizes low-level TCP sockets to perform connection checks.  
* **Target-Locked:** Hardcoded to scan 127.0.0.1 to prevent unintentional scanning of external networks.  
* **Configurable Port Range:** The port range can be easily modified within the script for targeted scans.  
* **Clear & Verbose Output:** Provides real-time feedback on the scanning process and clearly indicates open ports.

### **Getting Started**

To get a local copy up and running, follow these simple steps.

#### **Prerequisites**

* An operational Kali Linux environment (or other modern Linux distribution).  
* Python 3.x installed.

#### **Installation**

1. Clone the repository to your local machine using Git.  
   git clone \[https://github.com/scxr-dev/kali\_scanner.git\](https://github.com/scxr-dev/kali\_scanner.git)

2. Navigate into the newly created project directory.  
   cd kali\_scanner

### **How to Use and Test the Tool**

#### **Step 1: Run the Scanner**

Execute the script directly from your terminal using Python 3\.

python3 kali\_scanner\_v2.py

On a default, secure Kali machine, the scanner will likely report that no ports are open. This is normal.

#### **Step 2: Test the Scanner's Accuracy**

To verify the scanner is working correctly, you must give it an open port to find.

1. **Open a second, separate terminal window.** Do not close the first one.  
2. In this **new terminal**, start a simple web server on port 8000\. This command creates a live, open port for testing.  
   python3 \-m http.server 8000

3. Go back to your **first terminal** and run the scanner again.  
   python3 kali\_scanner\_v2.py

   This time, the scanner will successfully find and report: \[+\] Port 8000 is OPEN.  
4. When you are finished testing, go to the second terminal (the one running the server) and press Ctrl \+ C to close the port.

### **Troubleshooting**

A common issue is the OSError: \[Errno 98\] Address already in use. This indicates that the port you are trying to use for the test server is already occupied by another process.

**Resolution Workflow:**

1. **Identify the occupying process** using netstat and grep. This command will filter the output to show only the process on port 8000\.  
   sudo netstat \-tulnp | grep ':8000'

2. **Note the Process ID (PID)** from the output (e.g., 12345/python3).  
3. **Terminate the process.** Use the kill command to stop the process.  
   kill 12345

### **License**

This project is licensed under the MIT License. See the LICENSE file in the repository for the full text.

### **Creator**

This tool was created and is maintained by:

**R H A Ashan Imalka**

* GitHub: [scxr-dev](https://www.google.com/search?q=https://github.com/scxr-dev)