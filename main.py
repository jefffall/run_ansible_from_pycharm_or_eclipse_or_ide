import subprocess

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #run_ansible()
    try:
        #output = subprocess.check_output(['cat', '/Users/jfall/.ssh/id_rsa'])
        #output = subprocess.check_output(['sshpass', '-p','riveria','ssh', '-i', '/Users/jfall/.ssh/id_rsa', 'jfall@192.168.1.59', 'ansible-playbook', '-i',  '~/ansible/hosts.txt', '~/ansible/myplaybook.yaml'])
        output = subprocess.check_output(['ansible-playbook', '-i', '/Users/jfall/PycharmProjects/pythonProject1/hosts.txt', '--extra-vars', 'source=stmp-cars-dev-app-03 destinations=stmp-cars-dev-app-02', '/Users/jfall/PycharmProjects/pythonProject1/myplaybook.yaml'])
    except subprocess.CalledProcessError as e:
        print(e.output)
    else:
        print (output)