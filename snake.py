#snake game
#author: Enayah Mir
#importing all the imports
import random
import curses
#creating scrolling stuff
s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
#creating the window
w = curses.newwin(sh, sw, 0, 0)
#create a keypad window
w.keypad(1)
w.timeout(100)
#numerical values to size where snake is
snk_x = sw/4
snk_y = sh/2
# create mr.snake
snake = [
	[snk_y, snk_x],
	[snk_y, snk_x-1],
	[snk_y, snk_x-2]
]
#create food size
food = [sh/2, sw/2]
#create food, looks like letter pi
w.addch(food[0], food[1], curses.ACS_PI)
#right key function
key = curses.KEY_RIGHT

while True:
	next_key = w.getch()
	key = key if next_key == -1 else next_key
	#looking to see if dead
	if snake[0] [0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1]:
		curses.endwin()
		quit()
	#creating new head object
	new_head = [snake[0][0], snake[0][1]]
	#checking if arrow keys are pressed
	if key == curses.KEY_DOWN:
		new_head[0] += 1
	if key == curses.KEY_UP:
		new_head[0] -= 1
	if key == curses.KEY_LEFT:
		new_head[0] -= 1
	if key == curses.KEY_RIGHT:
		new_head[0] += 1
	snake.insert(0, new_head)
	#check if snake has eaten the food
	if snake[0] ==food:
		food= None
		while food is None:
			nf = [
				random.randint(1, sh-1),
				random.randint(1, sw-1)
				]
			food = nf if nf not in snake else None
			#add another piece of pie
			w.addch(food[0], food[1], curses.ACS_PI)
		else:
			tail = snake.pop()
			w.addch(int(tail[0]), int(tail[1]), ' ')
		w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)
