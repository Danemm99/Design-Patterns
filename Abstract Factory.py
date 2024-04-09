from abc import ABC, abstractmethod


class Chair(ABC):
    @abstractmethod
    def has_legs(self):
        pass

    @abstractmethod
    def color(self):
        pass


class Sofa(ABC):
    @abstractmethod
    def has_legs(self):
        pass

    @abstractmethod
    def color(self):
        pass


class VictorinChair(Chair):
    def has_legs(self):
        print('This Victorian Chair has legs.')

    def color(self):
        print('Black.')


class ModernChair(Chair):
    def has_legs(self):
        print('This Modern Chair has legs.')

    def color(self):
        print('Red.')


class VictorinSofa(Sofa):
    def has_legs(self):
        print('This Victorian Sofa has legs.')

    def color(self):
        print('Brown.')


class ModernSofa(Sofa):
    def has_legs(self):
        print('This Modern Sofa has legs.')

    def color(self):
        print('Green.')


class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_sofa(self):
        pass


class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return VictorinChair()

    def create_sofa(self):
        return VictorinSofa()


class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return ModernChair()

    def create_sofa(self):
        return ModernSofa()


if __name__ == "__main__":
    victorian_furniture_factory = VictorianFurnitureFactory()
    modern_furniture_factory = ModernFurnitureFactory()

    victorian_chair = victorian_furniture_factory.create_chair()
    modern_sofa = modern_furniture_factory.create_sofa()

    victorian_chair.has_legs()
    modern_sofa.color()
