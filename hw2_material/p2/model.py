import torch
import torch.nn as nn
import torchvision.models as models

class MyNet(nn.Module):
    def __init__(self):
        super(MyNet, self).__init__()
        
        ################################################################
        # TODO:                                                        #
        # Define your CNN model architecture. Note that the first      #
        # input channel is 3, and the output dimension is 10 (class).  #
        ################################################################
        
        self.conv1 = nn.Sequential(nn.Conv2d(3, 6, kernel_size=5, stride=1),
                                   nn.ReLU(),
                                   nn.MaxPool2d(kernel_size=2, stride=2))
        self.conv2 = nn.Sequential(nn.Conv2d(6, 16, kernel_size=5),
                                   nn.ReLU(),
                                   nn.MaxPool2d(kernel_size=2, stride=2))
        self.fc1 = nn.Sequential(nn.Linear(400, 128), nn.ReLU())
        self.fc2 = nn.Sequential(nn.Linear(128, 64), nn.ReLU())
        self.fc3 = nn.Linear(64, 10)

    def forward(self, x):

        ##########################################
        # TODO:                                  #
        # Define the forward path of your model. #
        ##########################################

        x = self.conv1(x)
        x = self.conv2(x)
        x = torch.flatten(x, start_dim=1, end_dim=-1)
        x = self.fc1(x)
        x = self.fc2(x)
        x = self.fc3(x)
        out = x
        return out
    
class ResNet18(nn.Module):
    def __init__(self):
        super(ResNet18, self).__init__()

        ############################################
        # NOTE:                                    #
        # Pretrain weights on ResNet18 is allowed. #
        ############################################

        # (batch_size, 3, 32, 32)
        self.resnet = models.resnet18(pretrained=True)
        # (batch_size, 512)
        self.resnet.fc = nn.Linear(self.resnet.fc.in_features, 10)
        # (batch_size, 10)

        #######################################################################
        # TODO (optinal):                                                     #
        # Some ideas to improve accuracy if you can't pass the strong         #
        # baseline:                                                           #
        #   1. reduce the kernel size, stride of the first convolution layer. # 
        #   2. remove the first maxpool layer (i.e. replace with Identity())  #
        # You can run model.py for resnet18's detail structure                #
        #######################################################################
        
        self.resnet.conv1 = nn.Conv2d(3, 64, kernel_size=3, stride=1, padding=1, bias=False)
        self.resnet.maxpool = Identity()

    def forward(self, x):
        return self.resnet(x)

class Identity(nn.Module):
    def __init__(self):
        super(Identity, self).__init__()
        
    def forward(self, x):
        return x
    
if __name__ == '__main__':
    model = ResNet18()
    print(model)