import torch
#which gpus are available
torch.cuda.device(1)    
torch.cuda.get_device_name
print(torch.cuda.is_available())
print("********")
print(torch.cuda.utilization(0))
print(torch.cuda.utilization(1))