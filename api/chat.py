from http.server import BaseHTTPRequestHandler
import json
import re

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = json.loads(self.rfile.read(content_length))
        
        user_input = post_data.get("input", "")
        prompt = post_data.get("prompt", "")
        
        # 原分析逻辑
        try:
            pattern = r'(.+?)(?:（(\d{4}年\d{1,2}月(?:\d{1,2}日)?)）)?氡含量(\d+(?:\.\d+)?)Bq/L（历史(\d+(?:\.\d+)?)）水位(\d+(?:\.\d+)?)m（历史(\d+(?:\.\d+)?)）'
            match = re.match(pattern, user_input)
            if not match:
                raise ValueError("输入格式错误")

            # ...（原 analyze_groundwater 函数逻辑）...
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
            
        except Exception as e:
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())