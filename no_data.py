import os
env = 'AWS_STEP_SIM_PRJ'
base_path = os.env[env]
file_path = os.path.join(base_path,
                         'no_data.config' )

with open(file_path, 'r') as fr:
    word = fr.readline()
    #Search word is not in the env folder
    if is_word(env,word):
        