import tkinter
import random
class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")
        self.canvas = tkinter.Canvas(self.master, width=400, height=400)
        self.canvas.pack()
        self.snake = [(20, 20), (20, 30), (20, 40)]
        self.direction = "Down"
        self.food = None
        self.create_food()
        self.master.bind("<KeyPress>", self.change_direction)
        self.update()

    def create_food(self):
        while True:
            x = random.randint(0, 39) * 10
            y = random.randint(0, 39) * 10
            if (x, y) not in self.snake:
                self.food = (x, y)
                break

    def change_direction(self, event):
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            self.direction = event.keysym

    def update(self):
        head_x, head_y = self.snake[0]
        if self.direction == "Up":
            head_y -= 10
        elif self.direction == "Down":
            head_y += 10
        elif self.direction == "Left":
            head_x -= 10
        elif self.direction == "Right":
            head_x += 10

        new_head = (head_x, head_y)

        if new_head in self.snake or not (0 <= head_x < 400 and 0 <= head_y < 400):
            self.game_over()
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.create_food()
        else:
            self.snake.pop()

        self.draw()
        self.master.after(100, self.update)

    def draw(self):
        self.canvas.delete("all")
        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(x, y, x + 10, y + 10, fill="green")
        food_x, food_y = self.food
        self.canvas.create_rectangle(food_x, food_y, food_x + 10, food_y + 10, fill="red")

    def game_over(self):
        self.canvas.delete("all")
        self.canvas.create_text(200, 200, text="Game Over", font=("Arial", 24), fill="red)")