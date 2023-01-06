# DOC (Dynamic Code Obfuscator)
![rem_back-removebg-preview](https://user-images.githubusercontent.com/72181445/183062380-e6321c88-42e4-4f7a-877e-d39d7d019edb.png)

## Description
### DCO Takes in code (python,binary,bash), base64 encodes the payload, reverses encoded text and randomly generates an unique python template to launch the original payload in memory (binary is written to disk).

## Installation
```
git clone https://github.com/R00tendo/DCO-Dynamic-Code-Obfuscator
cd DCO-Dynamic-Code-Obfuscator
python3 -m pip install -r requirements.txt
python3 DCO.py -h
```


## Usage
```
  -h, --help            show this help message and exit
  -o OBFUSCATE, --obfuscate OBFUSCATE
                        File to obfuscate.
  -p PRE_SCRIPT, --pre-script PRE_SCRIPT
                        Python script to run before executing the main virus
                        (to for example disable windows av).
  -f FORMAT, --format FORMAT
                        What format is the target file (binary,python,bash)
  --os OS               Target operating system.
  --out OUT             Output obfuscated code to.

```
<a href="https://asciinema.org/a/512853" target="_blank"><img src="https://asciinema.org/a/512853.svg" width=500 heigth=500/></a>

## Example usage:
```
python3 DCO.py -o reverse_shell.sh -f bash --out reverse_obf.py
python3 DCO.py -o Document.exe -f binary -p disable_av.py --os windows --out Document.py
python3 DCO.py -o im_bad_at_naming.py -p wipe_logs.py --out install_ram.py
```

## Supported formats:
* ### python (executed in memory)
* ### bash (executed in memory)
* ### binary (written to disk and executed)

#### Donate monero: 48ZrWwcf1gpG9VCe7agYru36SJhKwDDyGCgGw4TvkAG92Exd9pN7GBvL23SkwrMMbgdFa7BnFX2k6cD49SzV7pv42B4JDQE
