# WallpaperChanger.py

import ctypes

class WallpaperChanger:
    @staticmethod
    def change_wallpaper(image_path):
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)
