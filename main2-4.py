#컴퓨터의 외부 및 내부 IP 확인하기
#내부, 외부 IP 한 번에 출력하는 코드 만들고 실행
import socket
import requests
import re


in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr.connect(("www.google.co.kr", 443))
print("내부 IP: ", in_addr.getsockname()[0])

req = requests.get("http://ipconfig.kr")
out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]
print("외부 IP: ", out_addr)
