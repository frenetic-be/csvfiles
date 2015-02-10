import csvfiles

def testit(test):
    '''
    Test function for the csvfiles modules. This allows to test the different 
    functions of the module.
    
    Args:
        testnumber (int): between 0 and 8
    '''
    if test < 0 or test > 8:
        raise ValueError('test number must be >= 0 and <= 8')
    if test == 0:
        print 'Simple example: '
        print "     d = csvfiles.getdata('TemperatureControl_20150208.txt')"
        print ''
    
        d = csvfiles.getdata('TemperatureControl_20150208.txt')
        print 'Dictionary keys: {0}'.format(d.keys())
        print 'Type of dictionary column: {0}'.format(type(d[0]))
        print 'Values of dictionary column 0: {0}'.format(d[0])

    if test == 1:
        print 'Let\s skip the first line (which contains the column header): '
        print "     d = csvfiles.getdata('TemperatureControl_20150208.txt', skiplines=1)"
        print ''
    
        d = csvfiles.getdata('TemperatureControl_20150208.txt', skiplines=1)
        print 'Dictionary keys: {0}'.format(d.keys())
        print 'Type of dictionary column: {0}'.format(type(d[0]))
        print 'Values of dictionary column 0: {0}'.format(d[0])

    if test == 2:
        print 'Let\s use retrieve the column headers and use that as dictionary keys: '
        print "     d = csvfiles.getdata('TemperatureControl_20150208.txt', field_header=True)"
        print ''
    
        d = csvfiles.getdata('TemperatureControl_20150208.txt', field_header=True)
        print 'Dictionary keys: {0}'.format(d.keys())
        print 'Type of dictionary column: {0}'.format(type(d['temperature']))
        print 'Values of dictionary column \'temperature\': {0}'.format(d['temperature'])

    if test == 3:
        print 'Ok. That\'s nice but the array we got is all string. I\'d like my data to be float: '
        print "     d = csvfiles.getdata('TemperatureControl_20150208.txt', field_header=True, types=float)"
        print ''
    
        d = csvfiles.getdata('TemperatureControl_20150208.txt', field_header=True, types=float)
        print 'Dictionary keys: {0}'.format(d.keys())
        print 'Type of dictionary column: {0}'.format(type(d['temperature']))
        print 'Values of dictionary column \'temperature\': {0}'.format(d['temperature'])
    
    if test == 4:
        print 'Great. But what if I have a column that is not convertible to float. It will fail. '
        print "     d = csvfiles.getdata('Weather_20150208.txt', field_header=True, types=float)"
        print ''
    
        d = csvfiles.getdata('Weather_20150208.txt', field_header=True, types=float)
        print 'Dictionary keys: {0}'.format(d.keys())
        print 'Type of dictionary column: {0}'.format(type(d['temperature']))
        print 'Values of dictionary column \'temperature\': {0}'.format(d['temperature'])

    if test == 5:
        print 'So, how to deal with that? We need to specify different types for different columns.'
        print "     d = csvfiles.getdata('Weather_20150208.txt', field_header=True, types=[str, float, float, str, float, float, float, float, float, float, float, str, int])"
        print ''
    
        d = csvfiles.getdata('Weather_20150208.txt', field_header=True, types=[str, float, float, str, float, float, float, float, float, float, float, str, int])
        print 'Dictionary keys: {0}'.format(d.keys())
        print 'Type of dictionary column: {0}'.format(type(d['temperature']))
        print 'Values of dictionary column \'temperature\': {0}'.format(d['temperature'])
        print 'Values of dictionary column \'time\': {0}'.format(d['time'])

    if test == 6:
        print 'That\'s it. You can also use the function csvfiles.getheader() to get the column headers only.'
        print "     h = csvfiles.getheader('TemperatureControl_20150208.txt')"
        print ''
    
        h = csvfiles.getheader('TemperatureControl_20150208.txt')
        print 'Column headers: {0}'.format(h)

    if test == 7:
        print 'And feed the headers to csvfiles.getdata().'
        print "     h = csvfiles.getheader('TemperatureControl_20150208.txt')"
        print "     d = csvfiles.getdata('TemperatureControl_20150208.txt', fields=h)"
        print ''
    
        h = csvfiles.getheader('TemperatureControl_20150208.txt')
        d = csvfiles.getdata('TemperatureControl_20150208.txt', fields=h)
        print 'Dictionary keys: {0}'.format(d.keys())
        print 'Type of dictionary column: {0}'.format(type(d['temperature']))
        print 'Values of dictionary column \'temperature\': {0}'.format(d['temperature'])

    if test == 8:
        print 'You can also make some simple plot'
        print "         csvfiles.plotdata('TemperatureControl_20150208.txt', None, ['temperature', 'lower threshhold'], field_header=True, labels=['Temp.', 'Threshold'], ylabel='Temperature (in C)', linestyles=[':','--'])"
        print ''
        csvfiles.plotdata('TemperatureControl_20150208.txt', None, ['temperature', 'lower threshold'], field_header=True, labels=['Temp.', 'Threshold'], ylabel='Temperature (in C)', linestyles=[':','--'])