def _flatten(x):
    result = []
    for el in x:
        if hasattr(el, "__iter__") and not isinstance(el, basestring):
            result.extend(_flatten(el))
        else:
            result.append(el)
    return result
    
class Utils:
    @staticmethod
    def _deleteEmpty(str):
        return str != ""
        
    @staticmethod
    def _getInt(val):
        if val.replace('.','',1).isdigit():
            val = str(int(float(val)))
            
        return val
        
    # from http://stackoverflow.com/questions/406121/flattening-a-shallow-list-in-python
    _flatten = staticmethod(_flatten)
    
    @staticmethod
    def _isInfinity(value):
        return value == "Infinity" or value == "-Infinity"
