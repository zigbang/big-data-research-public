import subprocess
import base64 
# Define a function to add or update a key-value pair in the secret object
def add_secret_key_value(key, value):
    secret_name = 'bdr-secret'
    # To update an existing secret object with a new key-value pair:
    encoded_value = base64.b64encode(value.encode('utf-8')).decode('utf-8')

    command = f'kubectl patch secret {secret_name} -p '
    command += f'{{"data":{{"{key}":"{encoded_value}"}}}}'  
    #print(command)
    subprocess.run(command.split(' '))

# Define a function to get the value of a key from the secret object
def get_secret_key_value(key): 
    # Get the current secret object
    secret_name = 'bdr-secret'
    # To get the value of a key from a secret object:  
    command = f'kubectl get secret {secret_name} -o '
    command += f"jsonpath={{.data.{key}}}"
    #print(command)
    result = subprocess.run(command.split(' '), stdout=subprocess.PIPE)
    value = base64.b64decode(result.stdout).decode('utf-8')
    #print(f'Value of key {key} is {value}')
    return value

# Example usage: add or update a key-value pair in the secret object
# add_secret_key_value('my-key2', 'my-value2')

# Example usage: get the value of a key from the secret object
# get_secret_key_value('my-key')
