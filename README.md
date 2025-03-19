# burppro-keygen

BurpSuite Pro - License Generator

## How to use 

```bash
git clone
cd burppro-keygen
```

Then you have so setup the Gemini API Key of one of your Google account.\
Retrieve it [here](https://aistudio.google.com/app/apikey) and put it inside
```bash
mv .env.template .env
nano .env
```

Install the necessaries dependencies

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Finally

```bash
python3 generator.py
```