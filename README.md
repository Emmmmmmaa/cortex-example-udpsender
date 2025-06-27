# Cortex Example UDP Sender

This is a fork of [Emotiv's cortex-example repository](https://github.com/Emotiv/cortex-example) with additional UDP sender functionality added to the Python directory.

## Overview
Example code for Cortex V2 & V3. So far we have the following languages:
* C++ (with Qt library https://www.qt.io)
* C#
* NodeJS
* Python (with UDP sender functionality)
* Unity

## New UDP Sender Feature

### Python UDP EEG Sender
The Python directory now includes `udp_eeg_sender.py` which allows you to:
- Subscribe to EEG data streams (band power and performance metrics)
- Send the received data via UDP to a specified host and port

#### Usage
1. Install dependencies: `pip install -r python/requirements.txt`
2. Update the UDP host and port in `udp_eeg_sender.py`
3. Configure your Emotiv client credentials
4. Run: `python python/udp_eeg_sender.py`

<!-- #### Features
- **Real-time Data Streaming**: Continuously receives and forwards EEG data
- **Combined Data Format**: Merges power data and performance metrics
- **UDP Communication**: Lightweight network transmission
- **Configurable Destination**: Easy to modify target host and port
- **Error Handling**: Robust error handling for network issues -->

## API Documentation
For Cortex V2 / V3 API documentations please check out: https://emotiv.gitbook.io/cortex-api/

