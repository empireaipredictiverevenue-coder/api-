from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            # 1. READ THE SIZE OF THE PACKAGE
            content_length = int(self.headers['Content-Length'])
            
            # 2. OPEN THE PACKAGE
            post_data = self.rfile.read(content_length)
            payload = json.loads(post_data.decode('utf-8'))
            
            # 3. EXTRACT THE GOLD
            lead_data = payload.get("content", "No data found")
            print(f"LEAD SECURED: {lead_data}")
            
            # 4. SEND THE RECEIPT
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "Lead Caught"}).encode())
            
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(e).encode())
