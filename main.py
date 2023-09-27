from flask import Flask, request, jsonify  
import subprocess  
  
app = Flask(__name__)  
  
@app.route('/execute', methods=['POST'])  
def execute_command():  
    command = request.form.get('command')  
  
    if command:  
        try:  
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)  
            return jsonify({"output": result, "error": None})  
        except subprocess.CalledProcessError as e:  
            return jsonify({"output": None, "error": str(e.output)})  
    else:  
        return jsonify({"output": None, "error": "No command provided"})  
  
if __name__ == '__main__':  
    app.run(debug=True, host='0.0.0.0', port=8000)  
