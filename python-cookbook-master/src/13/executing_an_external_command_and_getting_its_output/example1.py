import subprocess
try:
    out_bytes = subprocess.check_output(['ipconfig', '/all'])
    #out_bytes = subprocess.check_output(['netstat', '-a'])
    #out_bytes = subprocess.check_output('dir', shell=True)
    out_text = out_bytes.decode('utf-8')
    print(out_text)
except subprocess.CalledProcessError as e:
    print('It did not work. Reason:', e)
    print('Exitcode:', e.returncode)

