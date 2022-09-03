# Can you change the self parameter inside a class to something else (say subhasis) .
# Try changing self to 'sif' or 'subhasis' and sel the effects.

class Sample:
    def __init__(slf, name):
        slf.name = name

obj = Sample("Subhasis")
print(obj.name)