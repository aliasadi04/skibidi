import torch
#which gpus are available
torch.cuda.device(1)
print(torch.cuda.is_available())