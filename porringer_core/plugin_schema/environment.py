"""Plugin utilities for package environments"""

from abc import abstractmethod
from typing import Protocol

from porringer_core.schema import Package, PackageName


class EnvironmentPlugin(Protocol):
    """Plugin definition for package environments"""

    @abstractmethod
    def packages(self) -> list[Package]:
        """Gathers installed packages in the given environment

        Returns:
            A list of packages
        """
        raise NotImplementedError

    @abstractmethod
    def search(self, name: PackageName) -> Package | None:
        """Searches the environment's sources for a package

        Args:
            name: The package name to search for

        Returns:
            The package, or None if it doesn't exist
        """
        raise NotImplementedError

    @abstractmethod
    def install(self, name: PackageName) -> Package | None:
        """Installs the given package identified by its name

        Args:
            name: The package name to install

        Returns:
            The package, or None if it doesn't exist
        """
        raise NotImplementedError

    @abstractmethod
    def uninstall(self, names: list[PackageName]) -> list[Package | None]:
        """Uninstalls the given list of packages

        Args:
            names: The packages to uninstall

        Returns:
            A list of packages that were uninstalled. Each item could be None if there was a failure
        """
        raise NotImplementedError

    @abstractmethod
    def upgrade(self, names: list[PackageName]) -> list[Package | None]:
        """Upgrades the given list of packages

        Args:
            names: The packages to upgrade

        Returns:
            A list of packages that were upgraded. Each item could be None if there was a failure
        """
        raise NotImplementedError
