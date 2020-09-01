"""`List` provider example."""

import dataclasses
from typing import List

from dependency_injector import providers


@dataclasses.dataclass
class Module:
    name: str


@dataclasses.dataclass
class Dispatcher:
    modules: List[Module]


dispatcher_factory = providers.Factory(
    Dispatcher,
    modules=providers.List(
        providers.Factory(Module, name='m1'),
        providers.Factory(Module, name='m2'),
    ),
)


if __name__ == '__main__':
    dispatcher = dispatcher_factory()

    assert isinstance(dispatcher.modules, list)
    assert dispatcher.modules[0].name == 'm1'
    assert dispatcher.modules[1].name == 'm2'

    # Call "dispatcher = dispatcher_factory()" is an equivalent for:
    # dispatcher = Dispatcher(
    #     modules=[
    #         Module(name='m1'),
    #         Module(name='m2'),
    #     ],
    # )
