import platform
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

def set_font():
    plt.rcParams['axes.unicode_minus'] = False
    path = 'c:/Windows/Fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)