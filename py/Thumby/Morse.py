import thumby
import time

# ==========================================
# Morse Table
# ==========================================

MORSE = {
    # Letters
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",

    # Numbers
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
}

# ==========================================
# Configuration
# ==========================================

HOLD_MS = 300

AUTO_COMMIT_MS = 1000

DOT_FREQ = 700
DASH_FREQ = 700

DOT_BEEP_MS = 50
DASH_BEEP_MS = 150

# ==========================================
# State
# ==========================================

text_buffer = ""
current_morse = ""
preview = ""

b_down = False
b_start = 0

last_morse_input = 0

# ==========================================
# Helpers
# ==========================================

def update_preview():
    global preview

    if current_morse == "":
        preview = ""
    else:
        preview = MORSE.get(current_morse, "")

def visible_text():
    # Show the most recent text that fits
    return text_buffer[-12:]

def play_dot():
    try:
        thumby.audio.play(DOT_FREQ, DOT_BEEP_MS)
    except:
        pass

def play_dash():
    try:
        thumby.audio.play(DASH_FREQ, DASH_BEEP_MS)
    except:
        pass

# ==========================================
# Main Loop
# ==========================================

while True:

    # --------------------------------------
    # Morse Input (B)
    # --------------------------------------

    if thumby.buttonB.pressed():

        if not b_down:
            b_down = True
            b_start = time.ticks_ms()

    elif b_down:

        duration = time.ticks_diff(
            time.ticks_ms(),
            b_start
        )

        if duration < HOLD_MS:
            current_morse += "."
            play_dot()
        else:
            current_morse += "-"
            play_dash()

        last_morse_input = time.ticks_ms()

        update_preview()
        b_down = False

    # --------------------------------------
    # Newline (A)
    # --------------------------------------

    if thumby.buttonA.justPressed():
        if preview:
            text_buffer += preview

        current_morse = ""
        update_preview()

    # --------------------------------------
    # Space (Right)
    # --------------------------------------

    if thumby.buttonR.justPressed():
        text_buffer += " "

    # --------------------------------------
    # Backspace (Left)
    # --------------------------------------

    if thumby.buttonL.justPressed():

        if len(text_buffer) > 0:
            text_buffer = text_buffer[:-1]

    # --------------------------------------
    # Clear Current Morse (Up)
    # --------------------------------------

    if thumby.buttonU.justPressed():

        current_morse = ""
        update_preview()

    # --------------------------------------
    # Auto Commit
    # --------------------------------------

    if current_morse != "":

        elapsed = time.ticks_diff(
            time.ticks_ms(),
            last_morse_input
        )

        if elapsed > AUTO_COMMIT_MS:

            if preview:
                text_buffer += preview

            current_morse = ""
            update_preview()

    # ======================================
    # Display
    # ======================================

    thumby.display.fill(0)

    # Recent text
    thumby.display.drawText(
        visible_text(),
        0,
        0,
        1
    )

    # Current Morse sequence
    thumby.display.drawText(
        current_morse[-8:],
        0,
        14,
        1
    )

    # Preview character
    thumby.display.drawText(
        preview,
        0,
        28,
        1
    )

    # Morse key indicator
    if b_down:
        thumby.display.drawText(
            "*",
            66,
            28,
            1
        )

    # Auto-commit progress bar
    if current_morse != "":

        elapsed = time.ticks_diff(
            time.ticks_ms(),
            last_morse_input
        )

        remaining = max(
            0,
            AUTO_COMMIT_MS - elapsed
        )

        width = int(
            20 * remaining / AUTO_COMMIT_MS
        )

        thumby.display.drawFilledRectangle(
            50,
            32,
            width,
            3,
            1
        )

    thumby.display.update()
