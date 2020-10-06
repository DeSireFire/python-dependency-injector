"""Main module."""

import sys

from dependency_injector.wiring import Provide

from .services import UserService, AuthService, PhotoService
from .containers import Container


def main(
        email: str,
        password: str,
        photo: str,
        user_service: UserService = Provide[Container.user_service],
        auth_service: AuthService = Provide[Container.auth_service],
        photo_service: PhotoService = Provide[Container.photo_service],
):
    user = user_service.get_user(email)
    auth_service.authenticate(user, password)
    photo_service.upload_photo(user, photo)


if __name__ == '__main__':
    container = Container()
    container.configure_logging()
    container.config.from_ini('config.ini')
    container.wire(modules=[sys.modules[__name__]])

    main(*sys.argv[1:])
