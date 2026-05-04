//  --- GIBBERLINK SMOOTH-MOUSE ENGINE ---
//  SENSITIVITY: LOW (60) | STABILITY: MAX
//  BYPASSING 74HF78 JITTER
//  1. SETUP
let current_dps = 0
let max_dps = 0
let clicks_this_second = 0
let start_time = game.runtime()
//  Prevent instant Game Over
info.setLife(1)
//  2. THE PC MOUSE (High Precision)
let cursor = sprites.create(img`
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
`, SpriteKind.Player)
cursor.z = 100
cursor.setStayInScreen(true)
//  3. THE BIG BUTTON
let big_button = sprites.create(img`
    . . . . . 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 . . . . .
    . . . 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 . . .
    . . 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 . .
    . 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 .
    . 7 7 7 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 7 7 7 .
    . 7 7 7 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 7 7 7 .
    . 7 7 7 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 7 7 7 .
    . 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 .
    . . . . . 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 . . . . .
`, SpriteKind.Food)
//  4. CLICK LOGIC
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    
    if (cursor.overlapsWith(big_button)) {
        clicks_this_second += 1
        big_button.say(clicks_this_second, 100)
        music.play(music.melodyPlayable(music.baDing), music.PlaybackMode.InBackground)
    }
    
})
//  5. THE SLOW SENSITIVITY ENGINE
game.onUpdate(function on_update() {
    
    //  SENSITIVITY SETTING: Lower number = Slower/More Precision
    //  Changed from 180 to 60 for that smooth glide
    cursor.vx = controller.dx() * 60
    cursor.vy = controller.dy() * 60
    if (game.runtime() - start_time >= 1000) {
        current_dps = clicks_this_second
        if (current_dps > max_dps) {
            max_dps = current_dps
        }
        
        clicks_this_second = 0
        start_time = game.runtime()
    }
    
    info.setScore(max_dps)
    big_button.say("DPS: " + ("" + current_dps))
})
