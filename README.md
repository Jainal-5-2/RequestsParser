# 🕵️ RequestsParser

**Convert Burp Suite HTTP requests to Python `requests` code**  
*A minimal parser for security testing workflows*

```python
from RequestsParser import RequestsParser

# Parse Burp request
p = RequestsParser()
p.parse('burp_request.txt')

# Generate Python code
print(f"response = requests.{p.method.lower()}(
    '{p.host + p.path}',
    headers={p.headers},
    data={p.data}
)")
