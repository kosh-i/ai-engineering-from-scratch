import torch, time

# CPU test
x_cpu = torch.rand(5000, 5000)
start = time.time()
y_cpu = torch.mm(x_cpu, x_cpu)
print("CPU time:", time.time() - start)

# GPU test
x_gpu = torch.rand(5000, 5000, device="cuda")
start = time.time()
y_gpu = torch.mm(x_gpu, x_gpu)
torch.cuda.synchronize()  # wait for GPU to finish
print("GPU time:", time.time() - start)

print("GPU result device:", y_gpu.device)
