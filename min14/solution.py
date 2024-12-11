import matplotlib.pyplot as plt
import random
import numpy as np
import time

N = 100
iterations = 100

grid = [[random.choice([0, 1]) for _ in range(N)] for _ in range(N)]

def updatepy(grid):
    newGrid = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            total = sum(grid[(i + di) % N][(j + dj) % N] 
                        for di in [-1, 0, 1] 
                        for dj in [-1, 0, 1] 
                        if (di != 0 or dj != 0))
            if grid[i][j] == 1:
                if (total < 2) or (total > 3):
                    newGrid[i][j] = 0
                else:
                    newGrid[i][j] = 1
            else:
                if total == 3:
                    newGrid[i][j] = 1
    return newGrid

final_python_grid = grid
start_time_py = time.time()
for i in range(iterations):
    final_python_grid = updatepy(final_python_grid)
end_time_py = time.time()

def updatenumpy(grid):
    newGrid = np.copy(grid)
    for i in range(N):
        for j in range(N):
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                          grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                          grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                          grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N]))
            if grid[i, j] == 1:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = 0
            else:
                if total == 3:
                    newGrid[i, j] = 1
    return newGrid

final_numpy_grid = np.array(grid)
start_time_np = time.time()
for i in range(iterations):
    final_numpy_grid = updatenumpy(final_numpy_grid)
end_time_np = time.time()

survivors_np = np.sum(final_numpy_grid)
survivors_py = sum(sum(row) for row in final_python_grid)

print(f"Numpy alive: {survivors_np}")
print(f"Python alive: {survivors_py}")
print(f"Numpy time: {end_time_np - start_time_np}")
print(f"Python time: {end_time_py - start_time_py}")

fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(final_python_grid, cmap='binary')
axes[0].set_title('Python')
axes[0].axis('off')

axes[1].imshow(final_numpy_grid, cmap='binary')
axes[1].set_title('Numpy')
axes[1].axis('off')

plt.tight_layout()
plt.show()