class Car:
    def __init__(self):
        self.make = None
        self.model = None
        self.year = None
        self.color = None
        self.engine = None

    def __str__(self):
        return f"{self.year} {self.make} {self.model}, {self.color}, Engine: {self.engine}"


class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_make(self, make):
        self.car.make = make

    def set_model(self, model):
        self.car.model = model

    def set_year(self, year):
        self.car.year = year

    def set_color(self, color):
        self.car.color = color

    def set_engine(self, engine):
        self.car.engine = engine

    def get_car(self):
        return self.car


class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct_sport_car(self):
        self.builder.set_make("Ford")
        self.builder.set_model("Mustang")
        self.builder.set_year(2024)
        self.builder.set_color("Red")
        self.builder.set_engine("V8")

    def construct_suv(self):
        self.builder.set_make("Toyota")
        self.builder.set_model("Rav4")
        self.builder.set_year(2024)
        self.builder.set_color("Blue")
        self.builder.set_engine("V6")


if __name__ == "__main__":
    car_builder = CarBuilder()
    director = Director(car_builder)

    director.construct_sport_car()
    sports_car = car_builder.get_car()
    print("Sport Car:")
    print(sports_car)

    director.construct_suv()
    suv = car_builder.get_car()
    print("\nSUV:")
    print(suv)
