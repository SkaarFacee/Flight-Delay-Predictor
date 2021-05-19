# Flight Delay Predictor



A simple flight delay predictor that can predict whether a flight is delayed or not based on nine inputs. This is a machine learning project.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
You need to have `python3` with a virtual environment and Flask framework.

### Installation Steps
1. First of all you need to setup your virtual environment. (setup and activate)
```
pyvenv-3.6 chtenv
```
Install the python virtual environment setup using this command `sudo apt install python3.6-venv`
```
source chtenv/bin/activate
```
2. Install all the dependencies, python modules 
```
pip3 install -r requirements
```

3. Make the model by running the `build_model.py` file. This would build the model in your local machine
```
python3 build_model.py
```
4. Run the python app
```
python3 app.py
```
Now, the app should be running on the localhost, browse to to the link where your app is running. (most probably, http://127.0.0.1:5000/)


## Contributing Help
If you are really interested in contributing you can always contact the maintainer or even send a PR!

