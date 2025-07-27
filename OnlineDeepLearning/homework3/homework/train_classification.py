import torch
from torch.utils.data import DataLoader

import torch.nn as nn
import torch.optim as optim
from models import Classifier
from models import save_model
from datasets.classification_dataset import SuperTuxDataset

# Hyperparameters
batch_size = 64
learning_rate = 0.001
num_epochs = 10

# Data preparation (example using MNIST)
""" transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
]) """

# Load dataset

train_dataset = SuperTuxDataset(
    dataset_path='../classification_data/train',
    transform_pipeline='aug'
)
train_loader = DataLoader(
    train_dataset,
    batch_size=batch_size,
    shuffle=True)

# Model, loss, optimizer
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = Classifier().to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=learning_rate)

# Training loop
for epoch in range(num_epochs):
    model.train()
    running_loss = 0.0
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)

        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item() * images.size(0)

    epoch_loss = running_loss / len(train_loader.dataset)
    print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {epoch_loss:.4f}')

# Optionally save the trained model
save_model(model)