# Data Recovery Software for NTFS File System
### Data Recovery Project - Software Development - IT Carlow

**Keywords:** MFT, NTFS, Data Recovery, Flask, Socket.IO, Python, AngularJS, AngularMaterial

Application written in Python performing data recovery on NTFS file systems by analysing records from Master File Table(MFT).

Software consists of three parts
1. Background service written in Python, running in its own thread that iterates over each record in MFT searching for ones that can be recovered.
2. Web UI written in HTML5, CSS3 and Javascript with AngularJS framework and Angular Material library.
3. Flask server that passes messages between AngularJS web interface and a background service using Socket.IO.




