import textwrap
from enum import Enum
text = "This project was started in 2007 as a Google Summer of Code project by David Cournapeau. Later that year, Matthieu Brucher started work on this project as part of his thesis.\
In 2010 Fabian Pedregosa, Gael Varoquaux, Alexandre Gramfort and Vincent Michel of INRIA took leadership of the project and made the first public release, February the 1st 2010. Since then, several releases have appeared following a ~3 month cycle, and a thriving international community has been leading the development.\
"

for line in textwrap.wrap(text, 100):
    print(line)

# this can be used as identifier for set of constant data
class Color(Enum):
    RED = 1
    BLUE = 2
    WHITE = 0

print(Color.RED.value)