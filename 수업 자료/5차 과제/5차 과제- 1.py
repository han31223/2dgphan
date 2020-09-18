from pico2d import *

def handle_events() :
    global running
    global dx
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            running = False
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_RIGHT:
                dx += 5
            elif e.key == SDLK_LEFT:
                dx -= 5
            elif e.key == SDLK_ESCAPE:
                running = False
        elif e.type == SDL_KEYUP:
                if e.key == SDLK_LEFT:
                    dx += 5
                elif e.key == SDLK_RIGHT:
                    dx -= 5
           
open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')

running = True
x = get_canvas_width() // 2
dx = 0
frame = 0
while running:
    clear_canvas()
    
    grass.draw(400,30)
    character.clip_draw(frame * 100 , 0 , 100, 100, x, 90)
    
    update_canvas()

    x += dx
    frame = (frame + 1 ) % 8

    handle_events()
    delay(0.05)
    

close_canvas()
