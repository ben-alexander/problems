https://www.reddit.com/r/dailyprogrammer/comments/6qutez/20170801_challenge_325_easy_color_maze/

```python
>>> import colour_maze
>>> 
>>> maze = """B O R O Y\nO R B G R\nB O G O Y\nY G B Y G\nR O R B R"""
>>> sequence = 'OG'
>>> colour_maze.print_path(colour_maze.parse_maze(maze), colour_maze.run(maze, sequence))
\ \ \ O \
\ \ \ G \
\ O G O \
\ G \ \ \
\ O \ \ \
>>> maze = """R R B R R R B P Y G P B B B G P B P P R
... B G Y P R P Y Y O R Y P P Y Y R R R P P
... B P G R O P Y G R Y Y G P O R Y P B O O
... R B B O R P Y O O Y R P B R G R B G P G
... R P Y G G G P Y P Y O G B O R Y P B Y O
... O R B G B Y B P G R P Y R O G Y G Y R P
... B G O O O G B B R O Y Y Y Y P B Y Y G G
... P P G B O P Y G B R O G B G R O Y R B R
... Y Y P P R B Y B P O O G P Y R P P Y R Y
... P O O B B B G O Y G O P B G Y R R Y R B
... P P Y R B O O R O R Y B G B G O O P B Y
... B B R G Y G P Y G P R R P Y G O O Y R R
... O G R Y B P Y O P B R Y B G P G O O B P
... R Y G P G G O R Y O O G R G P P Y P B G
... P Y P R O O R O Y R P O R Y P Y B B Y R
... O Y P G R P R G P O B B R B O B Y Y B P
... B Y Y P O Y O Y O R B R G G Y G R G Y G
... Y B Y Y G B R R O B O P P O B O R R R P
... P O O O P Y G G Y P O G P O B G P R P B
... R B B R R R R B B B Y O B G P G G O O Y"""
>>> sequence = 'ROYPO'
>>> colour_maze.print_path(colour_maze.parse_maze(maze), colour_maze.run(maze, sequence))
\ \ \ \ \ \ \ \ Y \ \ \ \ \ \ \ \ \ \ \
\ \ \ \ \ \ \ \ O \ \ \ \ \ \ \ \ \ \ \
\ \ \ \ \ \ \ \ R \ \ \ \ \ \ \ \ \ \ \
\ \ \ \ \ \ \ \ O \ R \ \ \ \ \ \ \ \ \
\ \ \ \ \ \ \ \ P Y O \ \ \ \ \ \ \ \ \
\ \ \ \ \ \ \ \ \ \ P \ \ \ \ \ \ \ \ \
\ \ \ \ \ \ \ \ \ \ Y \ \ \ \ \ \ \ \ \
\ \ \ \ \ \ \ \ \ R O \ \ \ \ \ \ \ \ \
\ \ \ \ \ \ \ \ P O \ \ \ \ \ \ \ \ \ \
\ \ \ \ \ \ \ \ Y \ \ \ \ \ \ \ \ \ \ \
\ \ \ \ \ \ O R O \ \ \ \ \ \ \ \ \ \ \
\ \ \ \ \ \ P \ \ \ \ \ \ \ \ \ \ \ \ \
\ \ \ \ \ \ Y O P \ \ \ \ \ \ \ \ \ \ \
\ \ \ \ \ \ O R Y O \ \ \ \ \ \ \ \ \ \
\ \ \ \ O O R O Y R \ \ \ \ \ \ \ \ \ \
\ \ \ \ R \ \ \ P O \ \ \ \ \ \ \ \ \ \
\ \ \ P O \ \ \ O R \ \ \ \ \ \ \ \ \ \
\ \ \ Y \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \
\ \ \ O P Y \ \ \ \ \ \ \ \ \ \ \ \ \ \
\ \ \ R \ R R \ \ \ \ \ \ \ \ \ \ \ \ \
>>> 
```