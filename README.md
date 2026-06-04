# Network Host Discovery

A Python project that generates and tracks IP addresses within a specified host range.

## Features

- User-defined network input
- Starting and ending host selection
- Generates IP addresses within a range
- Stores discovered hosts
- Displays total hosts found

## Technologies Used

- Python 3
- Kali Linux

## Source Code

The main script for this project is:

- `host_discovery.py`

## Screenshots

### 1. Initial Script Development

The first version of the script accepted user input and generated network addresses.

![Initial Script](Screenshot%20(634).png)

---

### 2. Debugging and Troubleshooting

During development, several Python errors were identified and corrected, including NameError and IndentationError issues.

![Debugging](Screenshot%20(635).png)



---

### 3. Final Source Code

Completed version of the host discovery script showing user input handling, host generation, list storage, and host counting.

![Final Code](Screenshot%20(640).png)



---

### 4. Successful Script Execution

The script successfully generates hosts within a specified range and displays the total number of hosts found.

![Output](Screenshot%20(641).png)



---

### 5. Enhanced Host Discovery Output

Enhanced version displaying discovered hosts using status indicators and maintaining a generated host list.

![Enhanced Output](Screenshot%20(642).png)



---

## Example Usage

```bash
python3 host_discovery.py
```

Example:

```text
Enter network (Example: 192.168.1): 192.168.1
Enter starting host: 80
Enter ending host: 100
```

Output:

```text
192.168.1.80
192.168.1.81
...
192.168.1.100

Total Hosts: 21
```

## Future Improvements

- Add ICMP ping scanning
- Detect active hosts
- Export results to CSV
- Save results to a file
- Add multithreading for faster scanning

## Author

Mateen Mamou

Cybersecurity Student | Python Projects | Network Security<img width="649" height="618" alt="Screenshot 2026-06-03 232540" src="https://github.com/user-attachments/assets/c9a447b4-ee78-44bc-9ea9-e64c64304c8b" />
