from botminer.util import picture
from botminer.util import result_getter

def show_packets_ip():
    result = result_getter.get_packet_ip_statistic(1)
    picture.drawBar(result,title='ip distribution', xlabel='ip range', ylabel='frequency')

def show_log_ip():
    result = result_getter.get_scan_log_ip_statistic(rank=2)
    picture.drawBar(result, title='scan log ip distribution', xlabel='ip range', ylabel='frequency')

def show_score():
    result = result_getter.get_bot_scores()
    picture.drawBar(result, title='score of all ip', xlabel='ip', ylabel='score')

def show_outline_score():
    result = result_getter.get_outline_scores()
    picture.drawBar(result, title='score of all ip', xlabel='id', ylabel='score')

def show_outline_score_scatter():
    result = result_getter.get_outline_scores()
    picture.drawScatter(result)