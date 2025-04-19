# Get Started
## Clone the project
```
git clone https://github.com/Tcc0403/glows-workshop.git ~/glows-workshop
cd ~/glows-workshop
```
### Setup a venv
```
pip install uv
uv venv
source .venv/bin/activate
```
### Install dependencies
```
uv lock
uv sync
```

### FAQ
Q: Notebooks failed, e.g., benchmarking blocks pop errors.
A: The notebooks didn't fetch the corrct environment. Setup venv and install dependecies step by step before running any notebooks. 
Or you can just install the required package in the default anaconda environment. If only benchmark blocks are not working, it's most likely because of outdated triton version.
Try `pip install triton==3.0.0`.