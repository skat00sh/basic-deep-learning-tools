# basic-deep-learning-tools
The repo was created as a part of a student round discussino at Fraunhofer AISEC


## Steps
- Create a `conda` environment using
```bash
    conda create -n basic_torch python=3.10
 ```
- In order to run this repo,you can directly create the clone of the same environment using the following command(From directory root):
```bash
    conda env create --file basic_torch.yml 
```
- If you install more dependencies or change version of already existing libraries, make sure to update the enrionment file using:
```bash
  conda env export --name basic_torch > basic_torch.yml
```


## Tips to use on server
 
 - Run the training using the `screen` command so that in case your connection times out and you're disconnected, your training won't halt
 - Some commonly used screen commands
 ```bash
    # Name your screen in case you are running multiple python scripts
    screen -S my_screen_name
    
    # To disconnect from the screen without killing the process press **Ctrl + a, d**
    
    # To reconnect with the screen
    screen -r my_screen_name
    
    # To list all the running screen
    screen -ls
 ```

- Setup Pycharm or VsCode with remote Python interpreter to check if your local changes work with the libraries installed in the server `conda` env
- In case you don't use PyCharm or VSCode, then using `pudb` is a good option for debugging directly from the terminal in case your code breaks on the server
- There are many ways to organise a deep learning repo but the basic structure I prefer is for a barebones repo is:
``` bash
 REPO_ROOT
├── basic_torch.yml
├── config.yml
├── data
│ └── MNIST
├── model.py
├── README.md
├── train.py
└── utils.py
```
- Conda autocomplete bashscript [link](https://gist.github.com/skat00sh/e2bc4ed82313e658add18396245adeae)
