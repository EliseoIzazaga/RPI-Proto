from SSD1331 import SSD1331
import time

SSD1331_PIN_CS  = 23
SSD1331_PIN_DC  = 24
SSD1331_PIN_RST = 25

def Color656(r, g, b):
    c = 0
    c = r >> 3
    c = c << 6
    c = c | (g >> 2)
    c = c << 5
    c = c | (b >> 3)
    return c

COLOR_BLACK  = Color656(  0,   0,   0)
COLOR_GREY   = Color656(192, 192, 192)
COLOR_WHITE  = Color656(255, 255, 255)
COLOR_RED    = Color656(255,   0,   0)
COLOR_PINK   = Color656(240, 100, 225)
COLOR_YELLOW = Color656(255, 255,   0)
COLOR_GOLDEN = Color656(255, 215,   0)
COLOR_BROWN  = Color656(128,  42,  42)
COLOR_BLUE   = Color656(  0,   0, 255)
COLOR_CYAN   = Color656(  0, 255, 255)
COLOR_GREEN  = Color656(  0, 255,   0)
COLOR_PURPLE = Color656(160,  32, 240)
MAX_WIDTH  = 0x60
MAX_HEIGHT = 0x40

FILL_RECT_DISABLE          = 0x00
FILL_RECT_ENABLE           = 0x01 

H_SCROLL_DISABLE           = 0x00
H_SCROLL_ENABLE            = 0x01

V_SCROLL_DISABLE           = 0x00
V_SCROLL_ENABLE            = 0x01

LOCK_MODE_DISABLE          = 0x12
LOCK_MODE_ENABLE           = 0x16

SET_COLUMN_ADDRESS         = 0x15
SET_ROW_ADDRESS            = 0x75

DRAW_LINE                  = 0x21
DRAW_RECT                  = 0x22
CLEAR_WINDOW               = 0x25
FILL_RECT                  = 0x26

CONTINUOUS_SCROLLING_SETUP = 0x27
DEACTIVE_SCROLLING         = 0x2E
ACTIVE_SCROLLING           = 0x2F

SET_CONTRAST_A             = 0x81
SET_CONTRAST_B             = 0x82
SET_CONTRAST_C             = 0x83

MASTER_CURRENT_CONTROL     = 0x87

SET_PRECHARGE_SPEED_A      = 0x8A
SET_PRECHARGE_SPEED_B      = 0x8B
SET_PRECHARGE_SPEED_C      = 0x8C

SET_REMAP                  = 0xA0
SET_DISPLAY_START_LINE     = 0xA1
SET_DISPLAY_OFFSET         = 0xA2
NORMAL_DISPLAY             = 0xA4
ENTIRE_DISPLAY_ON          = 0xA5
ENTIRE_DISPLAY_OFF         = 0xA6
INVERSE_DISPLAY            = 0xA7
SET_MULTIPLEX_RATIO        = 0xA8
DISPLAY_ON_DIM             = 0xAC
SET_MASTER_CONFIGURE       = 0xAD
DISPLAY_OFF                = 0xAE
DISPLAY_ON                 = 0xAF
POWER_SAVE_MODE            = 0xB0
PHASE_1_2_PERIOD           = 0xB1
CLOCK_DIVIDER              = 0xB3
SET_PRECHARGE_VOLTAGE      = 0xBB
SET_V_VOLTAGE              = 0xBE

LOCK_MODE                  = 0xFD

device = SSD1331(SSD1331_PIN_DC, SSD1331_PIN_RST, SSD1331_PIN_CS)

def startUpMessage():
    device.EnableDisplay(True)
    device.Clear()
    device.DrawString(0,0, "ONLINE...", COLOR_GOLDEN)
    time.sleep(10)
    device.Clear()

def printToOled(toPrint, color, displayTime):
    device.Clear()
    device.DrawString(0,0, toPrint, color)
    time.sleep(displayTime)
    device.Clear()




if __name__ == '__main__':
    try:
        startUpMessage()
        printToOled("Start up complete...")
        
    finally:
        device.EnableDisplay(False)
        device.Remove()
