'''
.. module: csvfiles
.. moduleauthor: Julien Spronck
.. created: Feb 10, 2015

Simple module to read .csv files and transfer the content into a dictionary.
'''
__version__ = '1.0'

def str2date(datestr, date_format='%Y-%m-%d %H:%M:%S'):
    '''
    Converts a string to a datetime object.

    Args:
        datestr (str): the string.
        date_format (str, optional): The date format. Defaults to
            '%Y-%m-%d %H:%M:%S'.

    Returns:
        datetime object.
    Raises:
    '''
    from datetime import datetime

    datestr = datestr.split('.')[0]
    return datetime.strptime(datestr, date_format)

def str2float(astr):
    '''
    Converts a string to a float. The only difference with float() is that
    this returns 0 if the string is empty.

    Args:
        astr (str): the string.

    Returns:
        float.

    Raises:
    '''
    astr = astr.strip().replace(',','.')
    if astr == '':
        return 0.
    else:
        return float(astr)

def getdata(filename, fields=None, types=None, delimiter=',', skiplines=0,
            field_header=False):
    '''
    Reads the .csv file and transfer the content into a dictionary.

    Args:
        filename (str): file name.
        fields (list of str, optional): list of fields or key for the output
            dictionary. This must have the same number of elements than the
            number of columns in your csv file. Defaults to None. If None, the
            keys to the output dictionary will simply be numbers from 0 to the
            number of columns - 1.
        types (function or list of function, optional): function or list of
            functions to convert the data from a string to what you want. You
            can use the functions csvfiles.str2date and csvfiles.str2float.
            Defaults to None. If None, the data type will be str.
        delimiter (str, optional): Delimiter. Defaults to ','.
        skiplines (int, optional): Skip the first n lines. Defaults to 0.
        field_header (bool, optional): If True, it uses the first line of the
            file to determine what the fields are. Defaults to False.

    Returns:
        dictionary with content of the .csv file

    Raises:
        ValueError, TypeError
    '''
    # pylint: disable=E0611
    from numpy import append, array
    # pylint: enable=E1103


    dic = {}
    start = True

    if field_header:
        fields = getheader(filename, delimiter=delimiter)
        skiplines += 1
    linecounter = 0
    with open(filename, mode='r') as fil:

        for line in fil:
            row = line.split(delimiter)
            linecounter += 1
            if linecounter <= skiplines:
                continue

            for j, item in enumerate(row):
                if hasattr(types, '__call__'):
                    theel = types(item)
                elif isinstance(types, list) and len(types) == len(row):
                    theel = types[j](item)
                elif isinstance(types, list) and len(types) != len(row):
                    raise ValueError('types must be a function or a list of '+
                                     'functions with the same '+
                                     'length as the number of columns in the'+
                                     ' csv file.')
                elif types == None:
                    theel = item
                else:
                    raise TypeError('Unsupported type for types. Supported '+
                                    'types are functions, list of functions '+
                                    'or None')
                if start:
                    if fields == None:
                        dic[j] = array(theel)
                    elif fields != None and len(fields) == len(row):
                        dic[fields[j]] = array(theel)
                    else:
                        raise ValueError('fields must be a list '+
                                         'of strings with the same length '+
                                         'as the number of columns in the '+
                                         'csv file.')
                else:
                    if fields != None and len(fields) == len(row):
                        dic[fields[j]] = append(dic[fields[j]], theel)
                    elif fields != None:
                        ## ignore falty rows
                        continue
                    else:
                        dic[j] = append(dic[j], theel)
            start = False
    return dic

def getheader(filename, delimiter=','):
    '''
    Reads the first line of the .csv file, split into an array of column
    headers.

    Args:
        filename (str): file name.
        delimiter (str, optional): Delimiter. Defaults to ','.

    Returns:
        list of column headers of the .csv file

    Raises:
    '''
    with open(filename, mode='r') as fil:
        header = fil.readline()
    header = header.strip('\n\r# ')
    fields = header.split(delimiter)
    fields = [field.strip('\'" ') for field in fields]
    return fields

def plotdata(filename, xcol, ycols, field_header=False, delimiter=',',
             xlabel='', ylabel='', title='', linestyles=None,
             colors=None, markers=None, labels=None):
    '''
    Creates a simple plot of the data in the .csv file.

    Args:
        filename (str): file name.
        xcol (str or int): name of column containing x data. If field_header is
            True, xcol is a str with the name returned by csvfiles.getheader().
            Else, it is an int representing the column number.
        ycols (str or int or list of str or list of int): name of column
            containing x data. If field_header is True, ycols is a str or a
            list of str with the names returned by csvfiles.getheader().
            Else, it is an int or a list of int representing the column numbers
            that you want to plot.
        field_header (bool, optional): If True, it uses the first line of the
            file to determine what the fields are. Defaults to False.
        delimiter (str, optional): Delimiter. Defaults to ','.
        xlabel (str, optional): plot label for x-axis. Defaults to ''.
        ylabel (str, optional): plot label for y-axis. Defaults to ''.
        title (str, optional): plot title. Defaults to ''.
        linestyles (list of str, optional): plot line styles (see matplotlib
            line styles). If provided, this must be a list that has the same
            length as the number of columns to plot (ycols). Defaults to None.
        colors (list of str, optional): . plot colors (see matplotlib
            colors). If provided, this must be a list that has the same
            length as the number of columns to plot (ycols). Defaults to None.
        markers (list of str, optional): plot markers (see matplotlib
            markers). If provided, this must be a list that has the same
            length as the number of columns to plot (ycols). Defaults to None.
        labels (list of str, optional): line labels (see matplotlib
            line labels). If provided, this must be a list that has the same
            length as the number of columns to plot (ycols). Defaults to None.
            If not None, this argument creates a legend with the provided
            labels.
    Returns:

    Raises:
    '''
    # pylint: disable=E0611
    from numpy import array, arange
    from matplotlib import pyplot as plt
    # pylint: enable=E1103

    def col2data(dicti, column):
        '''
        Converts string to float.
        '''
        if not column in dicti:
            raise KeyError('{0}. Possible values are {1}'.format(column,
                                                                 dicti.keys()))
        return array([str2float(data) for data in dicti[column]])

    # Retrieve data from .csv file
    dic = getdata(filename, field_header=field_header, delimiter=delimiter)

    ydata = {}
    if not isinstance(ycols, list):
        ydata[0] = col2data(dic, ycols)
    else:
        for j, ycol in enumerate(ycols):
            ydata[j] = col2data(dic, ycol)

    if xcol == None:
        xdata = arange(len(ydata[0]))
    else:
        xdata = col2data(dic, xcol)

    for j, data in ydata.iteritems():
        line, = plt.plot(xdata, data)
        if colors != None and len(colors) == len(ydata):
            line.set_color(colors[j])
        if linestyles != None and len(linestyles) == len(ydata):
            line.set_linestyle(linestyles[j])
        if markers != None and len(markers) == len(ydata):
            line.set_marker(markers[j])
        if labels != None and len(labels) == len(ydata):
            line.set_label(labels[j])

    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)
    if title:
        plt.title(title)
    if labels != None:
        plt.legend()

    plt.show()
