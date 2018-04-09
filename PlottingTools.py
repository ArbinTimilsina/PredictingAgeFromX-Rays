def setTitle(axis, title, xAxis, yAxis):
    axis.set_title(title, fontsize=25)
    axis.set_xlabel(xAxis, fontsize=15)
    axis.set_ylabel(yAxis, fontsize=15)

def setTicks(axis):    
    for tick in axis.xaxis.get_ticklabels():
        tick.set_fontsize('large')
        tick.set_weight('bold')
    
    for tick in axis.yaxis.get_ticklabels():
        tick.set_fontsize('large')
        tick.set_weight('bold')
