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


if __name__ == '__main__':
    device = SSD1331(SSD1331_PIN_DC, SSD1331_PIN_RST, SSD1331_PIN_CS)
    try:
        device.EnableDisplay(True)
        device.Clear()
        
        device.DrawString(0,0, "Hello World", COLOR_GREEN)
        time.sleep(10)
        device.Clear()
        device.DrawString(0,0, "Part2", COLOR_BLUE)
        time.sleep(10)
    finally:
        device.EnableDisplay(False)
        device.Remove()