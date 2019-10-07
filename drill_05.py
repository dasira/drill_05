from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global x, y
    global P1, P2

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x,y = event.x +25, KPU_HEIGHT - event.y - 26
        elif event.type == SDL_MOUSEBUTTONDOWN:
            P2= [event.x, KPU_HEIGHT - event.y]
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

def move_char(p1, p2):
    for i in range(0,100 + 1, 2):
        t = i / 100
        x = (1-t) * p1[0] + t*p2[0]
        y = (1-t) * p1[1] + t*p2[1]
        if P1[0] <= P2[0]:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        else:
            character.clip_draw(frame * 100, 0, 100, 100, x, y)

    pass


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')


running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
P1 = [640,512]
P2 = [640,512]
frame = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    move_char(P1,P2)

    hand_arrow.draw(x, y)
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()




