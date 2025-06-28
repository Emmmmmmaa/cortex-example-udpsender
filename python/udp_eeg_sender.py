import socket
import json
from sub_data import Subcribe

class UDPEEGSender(Subcribe):
    def __init__(self, app_client_id, app_client_secret, udp_host='192.168.3.4', udp_port=5000, **kwargs): #127.0.0.1，修改这里为自己电脑的host(在GH中查看)
        super().__init__(app_client_id, app_client_secret, **kwargs)
        self.udp_host = udp_host
        self.udp_port = udp_port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.latest_pow_data = None
        self.latest_met_data = None
        
    def send_combined_data(self):
        """
        Send combined power and performance metric data via UDP
        """
        combined_data = {
            'timestamp': self.latest_pow_data['time'] if self.latest_pow_data else None,
            'power_data': self.latest_pow_data['pow'] if self.latest_pow_data else None,
            'performance_metric': self.latest_met_data['met'] if self.latest_met_data else None
        }
        
        print("Sending combined data:")
        print(f"Timestamp: {combined_data['timestamp']}")
        print(f"Power values: {combined_data['power_data']}")
        print(f"Performance metric: {combined_data['performance_metric']}")
        
        try:
            self.sock.sendto(json.dumps(combined_data).encode(), (self.udp_host, self.udp_port))
            print("Combined data sent via UDP successfully")
        except Exception as e:
            print(f"Error sending UDP data: {e}")
    
    def on_new_pow_data(self, *args, **kwargs):
        """
        Handle band power data
        """
        data = kwargs.get('data')
        self.latest_pow_data = data
        print(f"Received power data at {data['time']}")
        print(f"Current met data available: {self.latest_met_data is not None}")
        self.send_combined_data()
    
    def on_new_met_data(self, *args, **kwargs):
        """
        Handle performance metric data
        """
        data = kwargs.get('data')
        self.latest_met_data = data
        print(f"Received performance metric data at {data['time']}")
        print(f"Current pow data available: {self.latest_pow_data is not None}")
        self.send_combined_data()
    
    def __del__(self):
        """
        Clean up UDP socket when object is destroyed
        """
        if hasattr(self, 'sock'):
            self.sock.close()

def main():
    # Please fill your application clientId and clientSecret before running script
    your_app_client_id = 'db0pAmkP8iNeDCA8OZYgiwOt44toxKq6IlhxGibv' #尝试一下这个在别人电脑上run行不行
    your_app_client_secret = 'JVL32zX4GMO0ojc0MMOFrNI2p4BCY3LEOOHOeIYfoZ6k7XmsKqXuzVxXhxvqWkV4JZIrjkiLZ3izrm7EBzj2kirtTSP8oQ9NDinkvemIhQ2ElQfPoydgfT8TCvZaTbaC'
    

    # Create UDP sender instance
    sender = UDPEEGSender(your_app_client_id, your_app_client_secret)
    
    # Subscribe to power data stream
    streams = ['pow', 'met']
    sender.start(streams)

if __name__ == '__main__':
    main() 