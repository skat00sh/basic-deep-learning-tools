import torch
import torchvision
from utils import load_config_from_yml
from model import Net
import torch.optim as optim
import torch.nn.functional as F



path_to_config='/home/skatoosh/project/fraunhofer/basic-deep-learning-tools/config.yml'
CONFIG = load_config_from_yml(path_to_config)

# Loading train and test data
train_loader = torch.utils.data.DataLoader(
  torchvision.datasets.MNIST('./data/', train=True, download=True,
                             transform=torchvision.transforms.Compose([
                               torchvision.transforms.ToTensor(),
                               torchvision.transforms.Normalize(
                                 (0.1307,), (0.3081,))
                             ])),
  batch_size=CONFIG['batch_size'], shuffle=True)

test_loader = torch.utils.data.DataLoader(
  torchvision.datasets.MNIST('./data/', train=False, download=True,
                             transform=torchvision.transforms.Compose([
                               torchvision.transforms.ToTensor(),
                               torchvision.transforms.Normalize(
                                 (0.1307,), (0.3081,))
                             ])),
  batch_size=CONFIG['batch_size'], shuffle=True)

#Initialize the network and it's params
network = Net()
optimizer = optim.SGD(network.parameters(), lr=CONFIG['learning_rate'], momentum=CONFIG['momentum'])

learning_history = {
        "train_losses": [],
        "val_losses": [],
        "train_accuracy": [],
        "val_accuracy": [],
    }
def train():
  network.train()
  log_interval = CONFIG['log_interval']
  epoch = CONFIG['epochs']
  for batch_idx, (data, target) in enumerate(train_loader):
    optimizer.zero_grad()
    output = network(data)
    loss = F.nll_loss(output, target)
    loss.backward()
    optimizer.step()
    if batch_idx % log_interval == 0:
      print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
        epoch, batch_idx * len(data), len(train_loader.dataset),
        100. * batch_idx / len(train_loader), loss.item()))
      learning_history['train_losses'].append(loss.item())

  torch.save(network.state_dict(), './results/model.pth')
  torch.save(optimizer.state_dict(), './results/optimizer.pth')


if __name__ == '__main__':
    train()