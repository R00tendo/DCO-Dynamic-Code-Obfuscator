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

## Example usage:
```
python3 DCO.py -i Document.exe -f binary --os windows --out Document.py
python3 DCO.py -i im_bad_at_naming.py --os windows --out install_ram.py
```

## Supported formats:
* ### python (executed in memory)
* ### bash (executed in memory) UNDER WORK
* ### binary (written to disk and executed) LINUX UNDER WORK

#### Donate monero: 48ZrWwcf1gpG9VCe7agYru36SJhKwDDyGCgGw4TvkAG92Exd9pN7GBvL23SkwrMMbgdFa7BnFX2k6cD49SzV7pv42B4JDQE
