from pico2d import *
import helper as h

def handle_events() :
    global running , dx ,dy , x , y, delta, pos, target, speed , done
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            running = False
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                running = False
        elif e.type == SDL_MOUSEBUTTONDOWN:
            target[0], target[1] =  e.x  , get_canvas_height() - e.y - 1  
            delta = h.delta(pos,target,speed)
            speed = speed + 1

            


open_canvas()
grass = load_image('../res/grass.png')
character = load_image('../res/run_animation.png')

running = True
speed = 1
target = [0,0]
delta = [0,0]
pos = 150 , 80
done = [0,0]
x,y = get_canvas_width() // 2 , 80
dx ,dy = 0,0
frame = 0

while running:
    clear_canvas()
    
    grass.draw(400,30)
    character.clip_draw(frame * 100 , 0 , 100, 100, pos[0], pos[1])
    
    update_canvas()

    frame = (frame + 1 ) % 8

    handle_events()
    pos, done = h.move_toward(pos,delta,target)
    if (done == True) :
        speed = 1
        delta = [0,0]
        target = [0,0]
    print(pos,target,done)
    delay(0.05)
    

close_canvas()
