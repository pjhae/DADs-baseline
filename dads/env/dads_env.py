from abc import ABC, abstractmethod


class DadsEnvironment(ABC):
    def __init__(self):
        self._state = None

    @abstractmethod
    def get_state(self):
        pass

    @abstractmethod
    def set_state(self):
        pass

    @abstractmethod
    def get_obs(self):
        pass

    @abstractmethod
    def step(self):
        pass

    @property
    @abstractmethod
    def done(self):
        pass

    @abstractmethod
    def reset(self):
        pass

    def __enter__(self):
        self._state = self.get_state()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.set_state(self._state)