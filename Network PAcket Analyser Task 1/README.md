# 🌐 Network Packet Analyzer

A real-time network packet analysis tool built with Flask and Scapy. This application captures live network traffic and displays it in an interactive, visually appealing web interface with live updates.

## Features

- **Real-time Packet Capture**: Live capture and analysis of network traffic
- **Protocol Detection**: Automatic identification of TCP, UDP, ICMP, and other protocols
- **Live Updates**: Web interface automatically refreshes every 2 seconds to show latest packets
- **Elegant UI**: Dark-themed interface with glowing effects and smooth animations
- **Fallback Mode**: Automatically falls back to demo data if packet capture is unavailable
- **Payload Preview**: Inspect packet payloads with hover-to-expand functionality
- **Protocol Highlighting**: Color-coded protocol badges for quick visual identification

## System Requirements

- Python 3.7+
- Windows, macOS, or Linux
- (Optional) Administrator/Root privileges for live packet capture
- (Optional) WinPcap or Npcap on Windows for real packet capture

## Installation

### 1. Clone or Download Repository

```bash
git clone <repository-url>
cd "Task 1"
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Required packages:

- **Flask** - Web framework for the backend
- **Scapy** - Network packet manipulation library

## Usage

### Running the Application

**Windows (PowerShell):**

```powershell
python app.py
```

**macOS/Linux:**

```bash
python3 app.py
```

Or use the provided PowerShell script on Windows:

```powershell
.\run.ps1
```

### Accessing the Web Interface

1. Start the application using the commands above
2. Open your browser and navigate to: **http://127.0.0.1:5000**
3. You'll see real-time network traffic displayed in the table

## Architecture

### Backend (Flask)

- **Main Endpoint**: `/` - Serves the HTML interface
- **API Endpoint**: `/packets` - Returns JSON array of captured packets
- **Packet Structure**:
  ```json
  {
    "src": "192.168.1.100",
    "dst": "8.8.8.8",
    "protocol": "TCP",
    "payload": "..."
  }
  ```

### Frontend (HTML/CSS/JavaScript)

- **Polling**: Fetches packet data every 2 seconds
- **Dynamic Rendering**: Real-time table updates using JavaScript
- **Responsive Design**: Mobile-friendly layout with smooth animations
- **Interactive Elements**: Hover effects and expandable payload preview

## Important Notes

### For Real Packet Capture

- **Windows**: Run as Administrator and ensure WinPcap/Npcap is installed

  ```bash
  # For Npcap installation
  # Download from: https://nmap.org/npcap/
  ```

- **Linux**: May require root privileges or proper capabilities:

  ```bash
  sudo python3 app.py
  ```

- **macOS**: Generally works without special privileges

### Fallback Mode

If packet capture is not available or fails:

- The app automatically switches to **demo mode**
- Generates realistic sample packet data
- UI continues to function normally for testing/demonstration

## File Structure

```
├── app.py                 # Flask backend application
├── requirements.txt       # Python dependencies
├── run.ps1               # Windows PowerShell launch script
├── templates/
│   └── index.html        # Web interface
└── README.md             # This file
```

## Troubleshooting

### "Permission denied" error

- Run as Administrator (Windows) or with `sudo` (Linux/macOS)
- Check that WinPcap/Npcap is installed on Windows

### No packets appearing

- The app automatically uses demo mode if capture fails
- Verify network connectivity
- Check firewall settings

### Port 5000 already in use

- Modify the Flask port in `app.py`:
  ```python
  app.run(port=5001, debug=True)
  ```

## Performance

- **Packet Buffer**: Maintains up to 1000 packets in memory
- **Auto-cleanup**: Keeps last 500 packets when limit is reached
- **Refresh Rate**: Web interface updates every 2 seconds
- **Lightweight**: Minimal CPU/memory footprint

## API Response Example

```json
[
  {
    "src": "192.168.1.10",
    "dst": "142.250.185.46",
    "protocol": "TCP",
    "payload": "b'GET / HTTP/1.1\\r\\nHost: example.com\\r\\n...'"
  },
  {
    "src": "8.8.8.8",
    "dst": "192.168.1.10",
    "protocol": "UDP",
    "payload": "b'DNS Response...'"
  }
]
```

## Future Enhancements

- [ ] Filter by protocol, IP, or port
- [ ] Export captured packets to PCAP format
- [ ] Advanced protocol analysis and statistics
- [ ] Packet payload decoding
- [ ] Persistent logging to database

## License

This project is provided as-is for educational and network analysis purposes.

## Support

For issues or questions, please check the application logs or ensure:

1. Python and all dependencies are properly installed
2. Network interface is active
3. Application has necessary privileges to capture packets

---

**Last Updated**: February 2026
