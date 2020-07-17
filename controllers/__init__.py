#se não fizer essa iniciação dos módulos, dá problema no @module.route
from .sessao import module as sessao
from .calculadora import module as calculadora
from .historico import module as historico