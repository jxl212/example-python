from flask import Flask
import os,socket

app = Flask(__name__)

@app.route('/')
def hello_world():
	ret_str_list = []
	try:
		login_name=os.getlogin()
	except:
		login_name="NA"
	finally:
		ret_str_list.append("<b>name</b>: <pre>"+login_name+"</pre>")
	try:
		host_name=socket.getfqdn()
	except:
		host_name="NA"
	finally:
		ret_str_list.append("<b>hostname</b>: <pre>" +host_name+"</pre>" )



	for k in os.environ:
		v=os.getenv(k)
		ret_str_list.append(f"<b>{k}</b>:<pre>{v}</pre>")
	ret_str= "\n".join([f"<p>{i}</p>" for i in ret_str_list])
	return  ret_str

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
