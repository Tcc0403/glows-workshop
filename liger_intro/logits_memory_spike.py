import os

import torch
import torch.nn as nn
import torch.profiler


# Dummy model
class LMHead(nn.Module):
    def __init__(self, input_size, vocab_size):
        super(LMHead, self).__init__()
        self.fc = nn.Linear(input_size, vocab_size)

    def forward(self, x):
        return self.fc(x)

# Hyperparameters
hidden_size = 4096
vocab_size = 128000
BT = 4096 # batch_size = 1, seq_length = 4096

# Create model, loss function
model = LMHead(hidden_size, vocab_size).cuda()
criterion = nn.CrossEntropyLoss()

# Random inputs and labels
inputs = torch.randn(BT, hidden_size).requires_grad_().cuda()
targets = torch.randint(0, vocab_size, (BT,)).cuda()

# Output directory for the trace
trace_dir = "./trace_log"
os.makedirs(trace_dir, exist_ok=True)



# Profile and export to Chrome trace format
with torch.profiler.profile(
    activities=[torch.profiler.ProfilerActivity.CPU, torch.profiler.ProfilerActivity.CUDA],
    record_shapes=True,
    with_stack=True,
    on_trace_ready=torch.profiler.tensorboard_trace_handler(trace_dir),
    with_flops=True,
    profile_memory=True,
    schedule = torch.profiler.schedule(
        wait=0,
        warmup=0,
        active=5,
        skip_first=1,
    )
) as prof:

    for step in range(6):  
        output = model(inputs)
        loss = criterion(output, targets)
        loss.backward()
        prof.step() 

print(f"Trace exported to: {trace_dir}")
