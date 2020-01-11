from flask import Flask, render_template, send_file, request

app = Flask(__name__)

@app.route('/')
def main():
    return send_file("templates/index.html")
    
    
@app.route('/searchQuery')
def searchQuery():
    if request.method == 'GET':
        query = request.args.get('query')
        print(query)
        
        return "kappa"
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080", use_debugger=True)