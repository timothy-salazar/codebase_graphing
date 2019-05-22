import re

def function_in_line(line):
    """Input:
        line: string - a single line of the document.

    Output:
        If a function declaration begins on the given line AND the function
        declaration ends on the same line, this function will return the name of
        the function as well as a list containing the arguments for that
        function.
        If a function declaration begins but does not end on the given line,
        this function will returns False.
        If no function is delcared on the given line, this function returns
        True.

    This function determines whether a function declaration begins on the
    given line by looking for 1 or mor tabs followed by 'def '. It will then
    check to see whether the function ends on the current line by looking for
    the string pattern '):'.
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
            return func_name, func_args
        else:
            self.func_lines += line
            return False
    return True
