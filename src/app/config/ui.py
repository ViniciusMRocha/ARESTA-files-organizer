# main colors
from typing import Counter


app_bg_color = '#ffffff'
primary_color = '#6dddff'
# font
font_color_white = '#FFFFFF'
font_color_black = '#000000'
# accents
blue_accent = '#1d659c'
gray_accent = '#666666'
light_blue_accent = '#416b88'
yellow_accent = '#f8e85b'
dark_red_accent = '#8b0000'


# ======== DARK MODE =============
# main colors
app_bg_color_dark = '#363636'

chosen_lang = 'PT'
language = ['EN', 'PT']

new_name = 'New Name'
if chosen_lang == language[0]:
    # Labels
    file_path = 'File Path'
    new_name = 'New Name'
    counter = 'Counter'
    order = 'Order'
    map_btn = 'Get Map'
    output_btn = 'Output'
    run_btn = 'Run'
    restart_btn = 'Restart'

    # UI Options
    order_options = ['Ascending', 'Descending']

elif chosen_lang == language[1]:
    # UI Options
    order_options = ['Ascending', 'Descending']


# global app_bg_color
# global primary_color
# global font_color_white
# global font_color_black
# global blue_accent
# global gray_accent
# global light_blue_accent
# global yellow_accent
