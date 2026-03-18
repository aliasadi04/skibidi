import torch
#which gpus are available
torch.cuda.device(1)    
print(torch.cuda.get_device_name())
print(torch.cuda.is_available())