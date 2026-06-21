import time
import os

# Terminal size
width = 40
height = 10

# Ball position and direction
x, y = 1, 1
dx, dy = 1, 1

try:
    while True:
        # Clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Draw the ball
        for row in range(height):
            for col in range(width):
                if row == y and col == x:
                    print("O", end="")
                else:
                    print(" ", end="")
            print()
            
        # Update position
        x += dx
        y += dy
        
        # Bounce off walls
        if x <= 0 or x >= width - 1:
            dx = -dx
        if y <= 0 or y >= height - 1:
            dy = -dy
            
        # Wait a bit
        time.sleep(0.05)

except KeyboardInterrupt:
    print("\nBouncing ball animation ended.")
