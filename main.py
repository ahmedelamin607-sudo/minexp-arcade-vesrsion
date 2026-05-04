# --- GIBBERLINK SMOOTH-MOUSE ENGINE ---
# SENSITIVITY: LOW (60) | STABILITY: MAX
# BYPASSING 74HF78 JITTER

# 1. SETUP
current_dps = 0
max_dps = 0
clicks_this_second = 0
start_time = game.runtime()

# Prevent instant Game Over
info.set_life(1)
my_sprite.set_velocity(50, 50)

# 2. THE PC MOUSE (High Precision)
cursor = sprites.create(img("""
    . 1 . . . . . . . . . . . . . .
    . 1 1 . . . . . . . . . . . . .
    . 1 1 1 . . . . . . . . . . . .
    . 1 1 1 1 . . . . . . . . . . .
    . 1 1 1 1 1 . . . . . . . . . .
    . 1 1 1 1 1 1 . . . . . . . . .
    . 1 1 1 1 1 1 1 . . . . . . . .
    . 1 1 1 1 1 1 1 1 . . . . . . .
    . 1 1 1 1 1 . . . . . . . . . .
    . 1 1 . 1 1 . . . . . . . . . .
    . 1 . . . 1 1 . . . . . . . . .
    . . . . . . 1 1 . . . . . . . .
    . . . . . . . . . . . . . . . .
"""), SpriteKind.player)
cursor.z = 100
cursor.set_stay_in_screen(True)

# 3. THE BIG BUTTON
big_button = sprites.create(img("""
    . . . . . 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 . . . . .
    . . . 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 . . .
    . . 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 . .
    . 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 .
    . 7 7 7 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 7 7 7 .
    . 7 7 7 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 7 7 7 .
    . 7 7 7 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 7 7 7 .
    . 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 .
    . . . . . 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 . . . . .
"""), SpriteKind.food)

# 4. CLICK LOGIC
def on_a_pressed():
    global clicks_this_second
    if cursor.overlaps_with(big_button):
        clicks_this_second += 1
        big_button.say(clicks_this_second, 100)
        music.play(music.melody_playable(music.ba_ding), music.PlaybackMode.IN_BACKGROUND)

controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

# 5. THE SLOW SENSITIVITY ENGINE
def on_update():
    global start_time, clicks_this_second, current_dps, max_dps
    
    # SENSITIVITY SETTING: Lower number = Slower/More Precision
    # Changed from 180 to 60 for that smooth glide
    cursor.vx = controller.dx() * 60
    cursor.vy = controller.dy() * 60

    if game.runtime() - start_time >= 1000:
        current_dps = clicks_this_second
        if current_dps > max_dps:
            max_dps = current_dps
        clicks_this_second = 0
        start_time = game.runtime()
        
    info.set_score(max_dps)
    big_button.say("DPS: " + str(current_dps))

game.on_update(on_update)