class Flower:
    def __init__(self, name, color, freshness, stem_length, withering_time, price):
        self.name = name
        self.color = color
        self.freshness = freshness
        self.stem_length = stem_length
        self.withering_time = withering_time
        self.price = price

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'

    def get_remaining_withering_time(self):
        return self.withering_time - self.freshness


class Orchid(Flower):
    def __init__(self, freshness, stem_length, price, withering_time=7, name="Orchid", color='Purple'):
        super().__init__(name, color, freshness, stem_length, withering_time, price)


class Tulip(Flower):
    def __init__(self, color, freshness, stem_length, price, withering_time=5, name="Tulip"):
        super().__init__(name, color, freshness, stem_length, withering_time, price)


class Lily(Flower):
    def __init__(self, color, freshness, stem_length, price, withering_time=8, name="Lily"):
        super().__init__(name, color, freshness, stem_length, withering_time, price)


class FlowerBouquet:
    def __init__(self, *args):
        self.flower_list = []
        self.flower_list.extend(args)

    def get_price(self):
        prices = [flower.price for flower in self.flower_list]
        return sum(prices)

    def get_bouquet_withering_time(self):
        withering_time = [flower.get_remaining_withering_time() for flower in self.flower_list]
        return sum(withering_time) / len(withering_time)

    def sort_by_freshness(self, reverse=False):
        return sorted(self.flower_list, key=lambda x: x.freshness, reverse=reverse)

    def sort_by_color(self, reverse=False):
        return sorted(self.flower_list, key=lambda x: x.color, reverse=reverse)

    def sort_by_stem_length(self, reverse=False):
        return sorted(self.flower_list, key=lambda x: x.stem_length, reverse=reverse)

    def sort_by_stem_price(self, reverse=False):
        return sorted(self.flower_list, key=lambda x: x.price, reverse=reverse)

    def find_flower_by_price(self, value):
        res_list = [flower for flower in self.flower_list if flower.price == value]
        if not res_list:
            return "Nof found"
        return res_list

    def find_flower_by_color(self, value):
        res_list = [flower for flower in self.flower_list if flower.color == value]
        if not res_list:
            return "Nof found"
        return res_list


orchid = Orchid(1, 30, 10)
tulip = Tulip("Blue", 2, 25, 20)
lily = Lily("Pink", 3, 35, 30)

bouquet = FlowerBouquet(orchid, tulip, lily)
