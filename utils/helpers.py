from typing import Callable, Dict

from browser.WrappedChrome import WrappedChrome


def parse_get_parameters(url: str) -> Dict[str, str]:
    parameters = url.split('?')[1]
    parameters = parameters.split('&')
    parameters = map(lambda parameter: parameter.split('='), parameters)
    parameters = list(parameters)
    parameters = {parameter[0]: parameter[1] for parameter in parameters}

    return parameters
