import re

class docCrawler():
    """This object will go through a single document and perform the following
    operations:
        1. It will find any newly declared functions and add them to a list
        2. It will find where in the document a function is called, an object
            is created, or the method for an object is called. These will be
            stored in a dict.
    """
    def __init__(self, p):
        self.p = p
        self.function_dict = []
        self.func_lines = ''

    def check_for_funct(self, line):
        """Input:
            line: string - a single line of the document.

        Output:
            If a function declaration begins on the given line AND the function
            declaration ends on the same line, this method will return True.
            If a function declaration begins but does not end on the given line,
            the current line is appended to self.func_lines, and the method
            returns False.
            If no function is delcared on the given line, this method returns
            True.

        This method will check to see if a function has been declared in the
        given line. If it has been, it will add the name of the function and the
        arguments for that function to self.function_dict:
            key                 value
            ----------------------------------------
            name of function    arguments for the
                                function (as a list)

        It determines whether a function declaration begins on the current line
        by looking for 1 or mor tabs followed by 'def '. It will then check to
        see whether the function ends on the current line by looking for the
        string pattern '):'.
        """
        def_match = re.match('\t*def ', line)
        arg_match = re.search('\(', line)
        end_match = re.search('\):', line)
        if def_match: # Checks if a function definition begins on this line
            if end_match: # Checks if the function def also ends on this line
                a, name_start = def_match.span()
                name_end, arg_start = arg_match.span()
                arg_end, c = end_match.span()
                # We extract the function name and the arguments from the line
                func_name = line[name_start:name_end]
                temp = line[arg_start:arg_end].split(',')
                func_args = [i.strip() for i in temp] # turn args into neat list
                if func_name not in self.function_dict:
                    self.function_dict[func_name] = func_args
                else: # this probably won't happen, but just in case...
                    raise RuntimeError('Multiple functions with the same name \
                                        encountered by docCrawler within \
                                        single document.')
                self.func_lines = ''
                return True # I don't need these return True/False statements,
            else:           # but I'll leave them for now.
                self.func_lines += line
                return False
        return True

    def find_functions(self):
        """This method will open the file path given by self.p, which gives the
        location of a python document. It then goes through the file line by
        line and feeds each line to the check_for_funct() method. This will
        build a dictionary containing the name of each function defined within
        the file as keys, and the arguments for that function - in the form
        of a list - as values.
        """
        with open(self.p, 'r') as f:
            for line in f:
                line = line + self.func_lines
                if check_for_funct(line):
                    continue









class dirCrawler():
    """This object will go through an entire directory
    """
    pass
