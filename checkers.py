# vim: set fileencoding=utf-8 ts=4 sw=4 expandtab fdm=marker:
"""
Checker base class and various checkers for MCVerify.
"""

import logging

LOG = logging.getLogger('mcverify')

class Checker(object):
    """
    Checker baseclass. Contains the check method which needs to be
    implemented by the subclasses.
    """
    def __init__(self):
        # {{{
        self.name = self.__class__.__name__
        # }}}

    # pylint: disable=W0613
    def check(self, directory, files):
        """
        The check method does the actual checking. It takes a directory
        (full path) and a list of files in the bottom directory. This
        constraints how the music collection can be organized but can be
        changed here.

        :param directory: The full bottom directory of the files.
        :type directory: String
        :param files: A list of files in the directory
        :type files: A list of Strings
        :returns: True if check succeeded, otherwise False
        """
        # {{{
        LOG.debug("Running '%s' ..." % self.name)
        # }}}

    def status(self):
        """
        Get the status of this checker. This will be used for future
        versions where several checkers can run concurrently.

        :returns: Self.
        """
        # {{{
        return self
        # }}}

class CheckerGap(Checker):
    """
    Check for gaps in the files. This checker works can work in two ways,
    either by checking the actual number of the filename (in case there is
    a pattern specifing it in the documentation) or by checking the various
    ID tags for the files and see if there is any gaps.
    """
    def __init__(self):
        # {{{
        super(CheckerGap, self).__init__()
        # }}}

    def check(self, directory, files):
        # {{{
        super(CheckerGap, self).check(directory, files)

        result = True

        nexts = map(lambda x,y: (x,y), sorted(files), sorted(files[1:]))
        for n in nexts:
            if not n[1]:
                # end of list
                break

            a = int(n[0].split(".")[0])
            b = int(n[1].split(".")[0]) 
            if abs(a-b) != 1:
                LOG.error("Gap between '%s' and '%s'" % (n[0], n[1]))
                result = False

        return result
        # }}}

class CheckerName(Checker):
    """
    Check that the filenames matches the expression the configuration. See
    the documentation for examples.
    """
    def __init__(self):
        # {{{
        super(CheckerName, self).__init__()
        # }}}

    def check(self, directory, files):
        # {{{
        super(CheckerName, self).check(directory, files)

        result = True

        return result
        # }}}
    
class CheckerPath(Checker):
    """
    Check that the path of the files is contructed in an organized way. The
    actual "correct" path is defined in the configuration as a regular
    expression. See the documentation for examples.
    """
    def __init__(self):
        # {{{
        super(CheckerPath, self).__init__()
        # }}}

    def check(self, directory, files):
        # {{{
        super(CheckerPath, self).check(directory, files)

        result = True

        return result
        # }}}

class CheckerConsistency(Checker):
    """
    Check directory for consistency. This class will check that each ID field
    in every file is consistent in a logical manner. For example, same artist,
    same album, same year and so on. Special care has to be taken for
    various artists.
    """
    def __init__(self):
        # {{{
        super(CheckerConsistency, self).__init__()
        # }}}

    def check(self, directory, files):
        # {{{
        super(CheckerConsistency, self).check(directory, files)

        result = True

        return result
        # }}}

# Export an instance of every checker for others to use
CHECKERS = [
        CheckerGap(),
        CheckerName(),
        CheckerPath(),
        CheckerConsistency()
]

