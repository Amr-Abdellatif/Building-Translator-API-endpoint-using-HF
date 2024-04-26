# Language Translation

This project includes the development of API endpoint and the model used for English-french translation, i've attached a model and a requirements.txt file for running everything in a virtualenv 

## Usage

1. `pip install -r requirements.txt`

2. Run `main.py` this will run uvicorn server with the endpoints.

3. Open browser and navigate to the follwoing localhost for swagger ui `http://127.0.0.1:8000/docs`.

4. Test use cases :
    1. Legumes share resources with nitrogen-fixing bacteria

    < Legumes partagent des ressources avec des bactéries fixatrices d'azote

    2. my name is
    
    < mon nom est

# Training

Training took around 1 hour on my Nividia Geoforce RTX-3060 6GB of memory.
Training details can be found in Training notebook.