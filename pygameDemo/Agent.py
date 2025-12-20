import abc

class Agent(abc.ABC):
    @abc.abstractmethod
    def reset(self,grid,direction):
        raise NotImplementedError

    @abc.abstractmethod
    def step(self,grid):
        raise NotImplementedError

    