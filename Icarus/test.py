import time

print("Downloading file...", end="", flush=True)
time.sleep(1)

# \r moves cursor to start, \033[K clears from cursor to end of line
print("\r\033[KDone!", flush=True)