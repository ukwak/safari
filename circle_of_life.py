from animal import Animal

def print_TODO(todo):
    print(f'<<<not implemented yet>>>')

class Circle_of_life:
    def __init__(self, world_size, num_zebras, num_lions):

    def display(self):

        print_TODO('display')

    def step_move(self):
        
        print_TODO('step_move()')

    def step_breed(self):
        print_TODO('step_breed()')

    def run(self, run_timesteps=100):
        self.display()

if __name__ == 'main':
    safari = Circle_of_life(5,5,2)
    safari.display()
    safari.step_move()
    safari.step_breed()
    safari.run()
