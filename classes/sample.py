""" Sample class definition.
"""


class SampleGeneral:
    """ Sample class definition.
    """

    def __init__(self, rw_list: list,
                       ro_list: list):
        # A constructor
        self._rw_list = rw_list # read-write allowed
        self._ro_list = ro_list # read only

    @property
    def rw_list(self):
        """ Access read-write list.
        """
        return self._rw_list


#-------------------------------------------------------------------------------
#
# Instance of that class can be filled with random data:
#
# sObj = SampleStruct()
# sObj.some_list = [1, 2, 3]
# sObj.person = 'John Doe'
# sObj.experience = 8.2
#
#-------------------------------------------------------------------------------
class SampleStruct:
    pass



#-------------------------------------------------------------------------------
#
# Iterator behavior:
# - Container class with __iter__ that returns Iterator object with __next__
# or
# - Unified class with both __iter__ (returns self) and __next__
#
#-------------------------------------------------------------------------------
class SampleIterator:
    """
    """

    def __init__(self, data):
        self.data = data
        self.index = -1

    def __iter__(self):
        """ Or define
        """
        return self

    def __next__(self):
        if self.index == len(self.data) - 1:
            raise StopIteration
        self.index += 1
        return self.data[self.index]




