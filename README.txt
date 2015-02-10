NAME
    __init__

DESCRIPTION
    .. module: csvfiles
    .. moduleauthor: Julien Spronck
    .. created: Feb 10, 2015
    
    Simple module to read .csv files and transfer the content into a dictionary.


VERSION
    1.0


FUNCTIONS

    getdata(filename, fields=None, types=None, delimiter=', skiplines=0, field_header=False)
     |  Reads the .csv file and transfer the content into a dictionary.
     |  
     |  Args:
     |      filename (str): file name.
     |      fields (list of str, optional): list of fields or key for the output
     |          dictionary. This must have the same number of elements than the
     |          number of columns in your csv file. Defaults to None. If None, the
     |          keys to the output dictionary will simply be numbers from 0 to the
     |          number of columns - 1.
     |      types (function or list of function, optional): function or list of
     |          functions to convert the data from a string to what you want. You
     |          can use the functions csvfiles.str2date and csvfiles.str2float.
     |          Defaults to None. If None, the data type will be str.
     |      delimiter (str, optional): Delimiter. Defaults to ','.
     |      skiplines (int, optional): Skip the first n lines. Defaults to 0.
     |      field_header (bool, optional): If True, it uses the first line of the
     |          file to determine what the fields are. Defaults to False.
     |  
     |  Returns:
     |      dictionary with content of the .csv file
     |  
     |  Raises:
     |      ValueError, TypeError

    getheader(filename, delimiter=')
     |  Reads the first line of the .csv file, split into an array of column
     |  headers.
     |  
     |  Args:
     |      filename (str): file name.
     |      delimiter (str, optional): Delimiter. Defaults to ','.
     |  
     |  Returns:
     |      list of column headers of the .csv file
     |  
     |  Raises:

    plotdata(filename, xcol, ycols, field_header=False, delimiter=', xlabel='', ylabel='', title='', linestyles=None, colors=None, markers=None, labels=None)
     |  Creates a simple plot of the data in the .csv file.
     |  
     |  Args:
     |      filename (str): file name.
     |      xcol (str or int): name of column containing x data. If field_header is
     |          True, xcol is a str with the name returned by csvfiles.getheader().
     |          Else, it is an int representing the column number.
     |      ycols (str or int or list of str or list of int): name of column
     |          containing x data. If field_header is True, ycols is a str or a
     |          list of str with the names returned by csvfiles.getheader().
     |          Else, it is an int or a list of int representing the column numbers
     |          that you want to plot.
     |      field_header (bool, optional): If True, it uses the first line of the
     |          file to determine what the fields are. Defaults to False.
     |      delimiter (str, optional): Delimiter. Defaults to ','.
     |      xlabel (str, optional): plot label for x-axis. Defaults to ''.
     |      ylabel (str, optional): plot label for y-axis. Defaults to ''.
     |      title (str, optional): plot title. Defaults to ''.
     |      linestyles (list of str, optional): plot line styles (see matplotlib
     |          line styles). If provided, this must be a list that has the same
     |          length as the number of columns to plot (ycols). Defaults to None.
     |      colors (list of str, optional): . plot colors (see matplotlib
     |          colors). If provided, this must be a list that has the same
     |          length as the number of columns to plot (ycols). Defaults to None.
     |      markers (list of str, optional): plot markers (see matplotlib
     |          markers). If provided, this must be a list that has the same
     |          length as the number of columns to plot (ycols). Defaults to None.
     |      labels (list of str, optional): line labels (see matplotlib
     |          line labels). If provided, this must be a list that has the same
     |          length as the number of columns to plot (ycols). Defaults to None.
     |          If not None, this argument creates a legend with the provided
     |          labels.
     |  Returns:
     |  
     |  Raises:

    str2date(datestr, date_format='%Y-%m-%d %H:%M:%S')
     |  Converts a string to a datetime object.
     |  
     |  Args:
     |      datestr (str): the string.
     |      date_format (str, optional): The date format. Defaults to
     |          '%Y-%m-%d %H:%M:%S'.
     |  
     |  Returns:
     |      datetime object.
     |  Raises:

    str2float(astr)
     |  Converts a string to a float. The only difference with float() is that
     |  this returns 0 if the string is empty.
     |  
     |  Args:
     |      astr (str): the string.
     |  
     |  Returns:
     |      float.
     |  
     |  Raises:


