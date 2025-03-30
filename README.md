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
uv pip install -e .
```
### Run example
```
python vector_add.py
```

### Check Nsight Compute
```
ncu -set full vector_add.py
```
