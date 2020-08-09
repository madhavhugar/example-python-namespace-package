from kernel import process
from hardware import ram
from user import network

def whoami():
    return f'\n{process.whoami()}\n{ram.whoami()}\n{network.whoami()}\n'
