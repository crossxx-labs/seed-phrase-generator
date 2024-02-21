import subprocess
import os


def run(exe_path, params):

    # Call the executable with parameters and capture stdout, stderr, and exit status
    try:
        process = subprocess.Popen(" ".join([exe_path] + params), stdout=subprocess.PIPE, 
                                   stderr=subprocess.PIPE, shell=True)
        stdout, stderr = process.communicate()
        exit_status = process.wait()
        
        return exit_status, stdout.decode('utf-8'), stderr.decode('utf-8')
    except subprocess.CalledProcessError as e:
        raise Exception(f"Error executing command: {exe_path}, params {params}, exception: {e}")
    
def aes_decode(encrypted_str):
    exe = os.environ.get('CRYPTO_EXE_PATH')
    aes_key = os.environ.get('aeskey')
    if not exe or not aes_key:
        raise Exception("CRYPTO_EXE_PATH or aes_key not found")
    code, stdout, stderr = run(exe, ["--dec", "--source",
                    f"{encrypted_str}", "--key", f"{aes_key}"])
    if code == 0:
        stdout = stdout.split('\n')[2]
    return code, stdout, stderr