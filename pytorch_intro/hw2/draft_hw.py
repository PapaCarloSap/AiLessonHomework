# %% [markdown]
# # Feed-forward сети
# 
# Итак, давайте потренируемся тренировать нейронные сети прямого распространения (так как делали на паре)
# При этом попробуем создать свою функцию активации на одном из слоев

# %%
# Сделаем необходимые импорты
import torch

# %%
# Загрузим датасет CIFAR-100, сразу же создадим dataloader для него
# Если вам не хватает вычислительных ресурсов, то можно вернуться к CIFAR-10
import torchvision
import torchvision.transforms as transforms

transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
BATCH_SIZE = 4
NUM_CLASSES = 100

train_set = torchvision.datasets.CIFAR100(root='./temp_data', train=True, download=True, transform=transform)
train_loader = torch.utils.data.DataLoader(train_set, batch_size=BATCH_SIZE, shuffle=True, num_workers=0)

test_set = torchvision.datasets.CIFAR100(root='./temp_data', train=False, download=True, transform=transform)
test_loader = torch.utils.data.DataLoader(test_set, batch_size = BATCH_SIZE, shuffle=False, num_workers=0)

# %%
def get_img_vector_size()->int:
    dataiter = iter(train_loader)
    images, labels = dataiter.next()
    size = images[0].size()
    return size[0] * size[1] * size[2]   


# %%
# Создайте собственную архитектуру! Можете использовать все, что угодно, но в ограничении на использование линейные слои (пока без сверток)
# Давайте добавим ограниченный Leaky_relu, то есть output = max(0.1x, 0.5x)
# Ваша задача добавить его в архитектуру сети как функцию активации

import torch.nn as nn
import torch.nn.functional as F

class CustomLeakyRelu(nn.Module):
    def __init__(self, border:float, alpha:float) -> None:
        super().__init__()
        self.border = border
        self.alpha = alpha
        
    def forward(self, input):
        x = F.leaky_relu(input)
        return torch.where(x>self.border, x*self.alpha, x)
        
class Net(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        img_vector_size = get_img_vector_size()
        self.fc1 = nn.Linear(img_vector_size,512)
        self.fc2 = nn.Linear(512,128)
        self.fc3 = nn.Linear(128,NUM_CLASSES)
        self.cust_relu = CustomLeakyRelu(0.1, 0.5)
        
    def forward(self, x):
        x = x.view(x.shape[0], -1)
        
        x = self.cust_relu(self.fc1(x))
        #x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x
    
    def predict(self, x):
        x = x.view(x.shape[0], -1)
        
        x = self.cust_relu(self.fc1(x))
        #x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.softmax(self.fc3(x))
        return x
        

        
net = Net()

#%%

loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(net.parameters(), lr=0.001)

# %%
# Запустить обучение (по аналогии с тем, что делали на паре)
from tqdm import tqdm_notebook, tqdm

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
net.to(device)
#for epoch in tqdm.notebook.tqdm(range(10)):  
for epoch in tqdm(range(10)):  
    running_loss = 0.0 
    net.train()
    for i, batch in enumerate(train_loader, 0):
        #inputs, target = batch[0], batch[1]
        inputs, target = batch[0].to(device), batch[1].to(device)

        # обнуляем градиент
        optimizer.zero_grad()

        outputs = net(inputs)
        loss = loss_fn(outputs, target)
        loss.backward()
        optimizer.step()

        # выводим статистику о процессе обучения
        running_loss += loss.item()
        if i % 300 == 0:    # печатаем каждые 300 mini-batches
            print('[%d, %5d] loss: %.3f' %
                  (epoch + 1, i + 1, running_loss / 2000))
            running_loss = 0.0

print('Training is finished!')



# %%
xx= torch.FloatTensor([1.0, -1.0])
activation = nn.LeakyReLU(0.5)
activation(xx)


# %%
xx= torch.FloatTensor([1.0, -1.0])
activation = CustomLeakyRelu(0.1, 0.5)
tt = activation(xx)
print(tt)

# %%
