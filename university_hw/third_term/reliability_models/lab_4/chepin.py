import re

class ChepinMetric:
    def __init__(self, files=None):
        self.input_vars = set()
        self.mod_vars = set()
        self.control_vars = set()
        self.unused_vars = set()
        self.count_vars = {}

        self.data = files
        self.path = './examples'

    def start(self):
        output = []

        for file in self.data:
            with open(self.path + '/' + file, 'r') as read_file:
                code = read_file.read()
                self.analyze_code(code)
                chepin_metric = self.count_metric()
                output.append(self.form_result(chepin_metric))
                self.clear_containers()

        return output

    def analyze_code(self, code):
        for line in code.split('\n'):
            if line:
                func_def = re.findall(r'def\s+(\w+)\((.?)\):', line)
                if func_def:
                    for func_name, args in func_def:
                        args_list = [arg.strip().split('=')[0] for arg in args.split(',')]
                        self.input_vars.update(args_list)

                input_match = re.search(r'input\((.*?)\)', line)
                if input_match:
                    var = re.match(r'^(.*?)=', line)
                    if var:
                        var_name = var.group(1).strip()
                        if var_name:
                            self.input_vars.add(var_name)
                        continue

                match = re.findall(r'(\w+)\s=', line)
                if match:
                    for var in match:
                        if var:
                            self.mod_vars.add(var)

                code_without_strings = re.sub(r'(\'.*?\'|\".*?\")', '', line)
                control_match = re.findall(r'\b(if|for|while|elif)\s+([^:]+)', code_without_strings)
                for _, expr in control_match:
                    control_vars_in_expr = re.findall(r'\b([a-zA-Z_]\w*)\b', expr)
                    self.control_vars.update([var for var in control_vars_in_expr if var not in {'and', 'or', 'in'}])

    def count_metric(self):
        P = len(self.input_vars)
        M = len(self.mod_vars)
        C = len(self.control_vars)
        T = len(self.unused_vars)

        return P + 2 * M + 3 * C + 0.5 * T

    def form_result(self, counted_metric):
        return {'P': len(self.input_vars), 'M': len(self.mod_vars), 'C': len(self.control_vars),
                'T': len(self.unused_vars), 'CHEPIN': counted_metric}

    def clear_containers(self):
        self.input_vars = set()
        self.mod_vars = set()
        self.control_vars = set()
        self.unused_vars = set()
        self.count_vars = {}

    def set_data(self, files):
        self.data = files
