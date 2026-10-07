# pinn_pong.py

██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
██████████████████████████████████████████████▛░░▀██████████████████▀▀▀█▛▀░░▐████████████████████████████████████████████
████████████████▛▀▀▀██████████████████████████▌░░░██████████████████░░░▐██▌░░░▐████████▛▀▀▀██████████████████████████████
███████████████▙▖░░░██████████████████████████▙░░███████████████▛▀░░░▝▀▜░░░▐███████▙▖░░░█████████████████████████████
███▛▘░░░▀▜███████▙▄███▛▀▀▀██▀▜█████▀▀▀▜█▀▀████████████▀▀▀▀▜██▙▄░░░▗▄▌░░░▐█▛▀██████▙▄███▛▀▀▀██▀▜█████████▀▀▀▜████
███▌░░░░░░░░▀███▌░░░██▌░░░░░░░░▝▜██░░░░░░░░▝▜█████▛▘░░░▗▄███████░░░▐██▌░░░░░░░░░███▌░░░██▌░░░░░░░░▝███▛▘░░░░░░▝▜██
███▌░░░░▙▖░░░░██▌░░░█▌░░░░▄░░░░▐██░░░░▗░░░░▐██████▌░░░░████████████░░░▐██▌░░░░▗░░░███▌░░░██▌░░░░▄░░░░███░░░▗▄█░░░▐████
███▌░░░░████▌░░░█▌░░░█▌░░░███░░░▐██░░░▐██░░░▐██████▙▖░░░░▜█████████░░░▐██▌░░░▐██▌░░░██▌░░░██▌░░░██▌░░░██░░░▗▟██░░░▐████
███▌░░░░█▛▘░░░██▌░░░█▌░░░███░░░▐██░░░▐██░░░▐████████▙▄░░░░▐████████░░░▐██▌░░░▐██▌░░░██▌░░░██▌░░░██▌░░░██░░░▐███▀░░░▐████
███▌░░░░▘░░░░▄██▌░░░██▌░░░███░░░▐██░░░▐██░░░▐██████████▀░░░▗▟██████░░░▐██▌░░░▐██▌░░░██▌░░░██▌░░░██▌░░░██░░░░▝░░░░░▐████
███▌░░░░░░▗▄████▌░░░▀█▌░░░███░░░▐██░░░▐██░░░▐██████▛▀▀░░░░▗▟██████░░░▝▜▌░░░▐██▌░░░██▌░░░▀█▌░░░██▌░░░███▖░░░░░░░░▐████
███▌░░░░████████▙▄▄▄██▄▄▄▟███▄▄▄▟█▄▄▄▟█▄▄▄▟████████▙▖░░▄▄▟█████▄░░▄▟█▙▄▄▄██▙▄▄▄█▙▄▄▄█▙▄▄▄██▙▄▄▄████████░░░▐█████
███▌░░░░███████████████████████████████████████████████████████████████████████████████████████████████████████░░░░▐██████
███▌░░░░█████████████████████████████████████████████████████████████████████████████████████████████████████▛░░░░▐██████
███▌░░▄▄██████████████████████████████████████████████████████████████████████████████████████████████████▙▖░░░░░▟██████
███████████████████████████████████████████████████████████████████████████████████████████████████████████▙▄▄▄██████████
██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
made this ASCII thingie with my own program(plus some manual polishing), GO check it out on my github (pinnchyk)


A different (and maybe a bit odd) take on the classic Pong game, and my first attempt at creating a game in Python, using Pygame.

At the moment of last update of this README (06/10/2026), features include basically all those you'd expect from usual Pong, but more (with a bunch of inspiration from Deltarune; can't help it, it's a great, SUE ME). Controls are:

Menu controls:
    up - up arrow
    down - down arrow
    confirm - spacebar
    (as well as any of players' controls apply)
    
Player 1 (Red):
    up - W
    down - D 
    parry - E
Player 2 (Blue):
    up - P
    down - L
    parry - O
    
The inclusion of a parry mechanic might already catch you off-guard, but me being me, I had to spice the gameplay up a bit. If the ball (square, whatever) bounces off a player normally, it'll increase its speed a little; if you hit parry during a short window of time (0.3s or less) before the ball hits your character - the speed boost will be noticeably bigger. The direction in which the ball bounces off is determined not only by its initial direction, but also by which part of the player it hits (think of the player model as a parabolic object, and not a rectangular one that its represented as), while also speeding up the ball more on average the closer it hits to player's edge.

It's also hard to not mention the background, which is purely made using Pygame's draw functions; no assets. So therefore, the grid is fully customizable: color, lines distance, their angle, speed and intensity of oscillation, phase difference between the two grids, etc. 

The game does count the score, and shows it off in the end of the round. At the moment, you can only play one round of any of the three modes, but future plans include an infinite gameloop with progression in a form of a shop, where each player'll be able to buy/adjust their upgrades and sidegrades. The game will also include many different types of rounds with their own gimmicks, backgrounds and arena hazards. And, naturally, there'll be some settings options later on, like volume slider, low vfx mode, lyrics display toggle, etc.

Also, yes, there is quite a few hidden easter eggs here and there, go look out for them.

Well what else do you want me to say? Just go TRY THE GAME
