import generator
import gui


maze = generator.build_maze()
game = gui.Game(height=600,
                width=800,
                maze=maze)


game.mainloop()