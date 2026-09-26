# pinn_pong.py

███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
██████████████████████████████████████████████▛░░▀██████████████████▀▀▀▜██▛▀░░▐████████████████████████████████████████
████████████████▛▀▀▀██████████████████████████▌░░░██████████████████░░░▐██▌░░░▐████████▛▀▀▀████████████████████████████
███████████████▙▖░░░██████████████████████████▙░░█████████████████▛▀░░░▝▀▜▌░░░▐███████▙▖░░░████████████████████████████
███▛▘░░░▀▜███████▙▄███▛▀▀▀██▀▜█████▀▀▀▜█▀▀████████████▀▀▀▀▜███████▙▄░░░▗▄▟▌░░░▐█▛▀██████▙▄███▛▀▀▀██▀▜█████████▀▀▀▜█████
███▌░░░░░░░░▀███▌░░░██▌░░░░░░░░▝▜██░░░░░░░░▝▜███████▛▘░░░▗▄▟████████░░░▐██▌░░░░░░░░░███▌░░░██▌░░░░░░░░▝███▛▘░░░░░░▝▜███
███▌░░░░▙▖░░░░██▌░░░██▌░░░░▄░░░░▐██░░░░▗░░░░▐██████▌░░░░████████████░░░▐██▌░░░░▗▖░░░░██▌░░░██▌░░░░▄░░░░███░░░▗▄█░░░▐███
███▌░░░░██▌░░░██▌░░░██▌░░░███░░░▐██░░░▐██░░░▐██████▙▖░░░░▜██████████░░░▐██▌░░░▐██▌░░░██▌░░░██▌░░░██▌░░░██░░░▗▟██░░░▐███
███▌░░░░█▛▘░░░██▌░░░██▌░░░███░░░▐██░░░▐██░░░▐████████▙▄░░░░▐████████░░░▐██▌░░░▐██▌░░░██▌░░░██▌░░░██▌░░░██░░░▐██▀░░░▐███
███▌░░░░▘░░░░▄██▌░░░██▌░░░███░░░▐██░░░▐██░░░▐██████████▀░░░▗▟███████░░░▐██▌░░░▐██▌░░░██▌░░░██▌░░░██▌░░░██░░░░▝░░░░░▐███
███▌░░░░░░▗▄████▌░░░▀█▌░░░███░░░▐██░░░▐██░░░▐██████▛▀▀░░░░▗▟████████░░░▝▜█▌░░░▐██▌░░░██▌░░░▀█▌░░░██▌░░░███▖░░░░░░░░▐███
███▌░░░░████████▙▄▄▄██▄▄▄▟███▄▄▄▟█▄▄▄▟███▄▄▄▟██████▙▖░░▄▄▟██████████▄░░▄▟█▙▄▄▄███▙▄▄▄██▙▄▄▄█▙▄▄▄███▙▄▄▄█████████░░░▐███
███▌░░░░███████████████████████████████████████████████████████████████████████████████████████████████████████░░░░▐███
███▌░░░░█████████████████████████████████████████████████████████████████████████████████████████████████████▛░░░░▐████
███▌░░▄▄██████████████████████████████████████████████████████████████████████████████████████████████████▙▖░░░░░▟█████
███████████████████████████████████████████████████████████████████████████████████████████████████████████▙▄▄▄████████
███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
made this ASCII thingie with my own program, GO check it out on my github (pinnchyk)


A different (and maybe a bit odd) take on the classic Pong game, and my first attempt at creating a game in Python, using Pygame.

At the moment of upload of the first version (26/09/2026, pretty late at night), features include basically all those you'd expect from usual Pong, but more. Controls are:
Player 1 (Red):
    up - W
    down - D 
    parry - E
Player 2 (Blue):
    up - P
    down - L
    parry - O

The inclusion of a parry mechanic might already catch you off-guard, but me being me, I had to spice the gameplay up a bit. If the ball (square, whatever) bounces off a player normally, it'll increase its speed a little; if you hit parry during a short window of time (0.3s or less) before the ball hits your character - the speed boost will be noticeably bigger. The direction in which the ball bounces off is determined not only by its initial direction, but also by which part of the player it hits (think of the player model as a parabolic object, and not a rectangular one that its represented as).
It's also hard to not mention the background, which is purely made using Pygame's draw functions; no assets. So therefore, the grid is fully customizable: color, lines distance, their angle, speed and intensity of oscillation, phase difference between the two grids, etc. 

The game does also technically count the score, but only displays it in the console when it changes. As for the future features, some ideas I got are some basic ones, like SFX, additional VFX, background music, but also some more far-fetched ones, like a shop where players would be able to purchase individual boosts for their characters, or maybe even additional abilities. The shop would occur after rounds, which would come one by one, and I am considering making different types of rounds, with their specific gimmicks, accompanied by a different arena (background) and music.

Well what else do you want me to say? Just go TRY THE GAME
