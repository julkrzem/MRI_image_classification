import torch
from torch.utils.data import TensorDataset, random_split, DataLoader


class AddTransform(torch.utils.data.Dataset):
    def __init__(self, dataset, transform=None):
        self.dataset = dataset
        self.transform = transform

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):
        image, label = self.dataset[idx]
        if self.transform:
            image = self.transform(image)
        return image, label
    


def preprocess(dataset, batch_size, transform=None):
    images = dataset['images']
    labels = dataset['labels']

    dataset_temp = TensorDataset(images, labels)

    if transform:
        dataset_temp = AddTransform(dataset_temp,transform)

    train_size = int(len(dataset_temp)*0.6)
    test_size = int(len(dataset_temp)*0.2)
    val_size = len(dataset_temp) -train_size - test_size

    train, test, val = random_split(dataset_temp, [train_size, test_size,val_size])

    batch_size = batch_size

    trainloader = DataLoader(train, batch_size=batch_size, shuffle=True)
    testloader = DataLoader(test, batch_size=batch_size, shuffle=True)
    valloader = DataLoader(val, batch_size=batch_size, shuffle=False)

    return trainloader,testloader,valloader

