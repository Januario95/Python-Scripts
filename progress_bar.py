import sys
import time

def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()

def updt(total, progress, prefix='Progress'):
    """
    Displays or updates a console progress bar.

    Original source: https://stackoverflow.com/a/15860757/1391441
    """
    barLength, status = 50, ""
    progress = float(progress) / float(total)
    if progress >= 1.:
        progress, status = 1, " Complete\r\n"
    block = int(round(barLength * progress))
    text = "\r{}: [{}] {:.0f}% {}".format(prefix, "#" * block + "-" * (barLength - block), round(progress * 100, 0),
        status)
    sys.stdout.write(text)
    sys.stdout.flush()
    time.sleep(0.2)


# runs = 300
# for run_num in range(runs):
#     updt(runs, run_num + 1)


texts = [
    'The bot successfully', 'inhibited the client from using new checks',
    'The bot successfully inhibited the client from using new checks',
    'Bot was did not inhibit the client, because was unable to locate commit path'
]
for text in texts:
    delay = 1/len(text)+0.01
    delay2 = delay + 0.3
    print(delay, delay2, text)


