from typing import AsyncIterator

from dishka import Provider, Scope, provide, AnyOf, from_context
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, AsyncEngine, create_async_engine

from dah.application.common.ports.uow import UoW
from dah.bootstrap.config import DBConfig


class Config(Provider):
    scope = Scope.APP

    db_config = from_context(DBConfig)


class DBProvider(Provider):
    scope = Scope.REQUEST

    @provide(scope=Scope.APP)
    async def get_engine(self, config: DBConfig) -> AsyncIterator[AsyncEngine]:
        engine = create_async_engine(
            config.uri,
            echo=config.echo,
            pool_size=15,
            max_overflow=15,
        )
        yield engine
        await engine.dispose()

    @provide(scope=Scope.APP)
    async def get_sessionmaker(
            self, engine: AsyncEngine
    ) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(
            bind=engine,
            autocommit=False,
            autoflush=False,
            expire_on_commit=False,
        )

    @provide(scope=Scope.REQUEST)
    async def get_session(
            self,
            async_factory: async_sessionmaker[AsyncSession],
    ) -> AsyncIterator[AnyOf[UoW, AsyncSession]]:
        async with async_factory() as session:
            yield session


def setup_providers() -> tuple[Provider, ...]:
    return (
        Config(),
        DBProvider(),
    )
