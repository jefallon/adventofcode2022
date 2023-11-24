from re import findall
from math import ceil


class Blueprint:
    def __init__(self, text):
        self.id = 0
        self.resources = ["ore", "clay", "obsidian", "geode"]
        self.max_geodes = 0
        self.max = dict()
        self.costs = dict()
        self.stack = list()
        self.text = text
        self.populate()
        self.states = 1
        self.best = str()
        return None

    def populate(self):
        self.parse_input()
        self.stack.append(
            State(
                self,
                {rsc: 0 for rsc in self.resources},
                {rsc: 0 for rsc in self.resources},
                32,
            )
        )
        self.stack[0].bots["ore"] = 1
        return None

    def parse_input(self):
        costs = list(map(int, findall("\d+", self.text)))
        self.id = costs[0]
        self.costs["ore"] = {"ore": costs[1]}
        self.costs["clay"] = {"ore": costs[2]}
        self.costs["obsidian"] = {"ore": costs[3], "clay": costs[4]}
        self.costs["geode"] = {"ore": costs[5], "obsidian": costs[6]}
        self.max = {
            "ore": max(self.costs[bot]["ore"] for bot in self.resources),
            "clay": self.costs["obsidian"]["clay"],
            "obsidian": self.costs["geode"]["obsidian"],
        }
        return None

    def play_round(self):
        s = self.stack.pop()
        if s.nominal_max < self.max_geodes:
            return None
        if s.minutes <= 0:
            #     s1 = State(
            #         self, dict(s.resources), dict(s.bots), s.minutes - 1, s.string + "."
            #     )
            #     s1.get_resources()
            #     self.stack.append(s1)
            # else:
            if s.resources["geode"] > self.max_geodes:
                self.best = s.string
                self.max_geodes = s.resources["geode"]
            return None

        for rsc in self.resources:
            s.can_make(rsc)

        return None

    def play(self):
        while self.stack:
            self.play_round()


class State:
    def __init__(self, blueprint, resources, bots, minutes, string=""):
        self.blueprint = blueprint
        self.resources = resources
        self.bots = bots
        self.minutes = minutes
        self.bound_geodes()
        self.string = string
        return None

    def make_turns(self, bot):
        for rsc in self.blueprint.costs[bot].keys():
            if self.bots[rsc] == 0:
                return 99
        turns = max(
            ceil((cost - self.resources[rsc]) / self.bots[rsc])
            for rsc, cost in self.blueprint.costs[bot].items()
        )
        turns = max(turns, 0)
        return turns

    def can_make(self, bot):
        if bot != "geode":
            X = self.bots[bot]
            T = self.minutes
            Z = self.blueprint.max[bot]
            Y = self.resources[bot]

            if (X * T) + Y >= T * Z:
                return None

        # for rsc, cost in self.resources.items():
        #     if self.blueprint.costs[bot].get(rsc, 0) > cost:
        #         return False
        # return True

        t = self.make_turns(bot)
        if t < self.minutes - 1:
            s1 = State(
                self.blueprint,
                dict(self.resources),
                dict(self.bots),
                self.minutes - t - 1,
                self.string + ("." * t) + bot[1],
            )
            for rsc, rate in self.bots.items():
                s1.resources[rsc] += rate * (t + 1)
            for rsc, cost in self.blueprint.costs[bot].items():
                s1.resources[rsc] -= cost
            s1.bots[bot] += 1
            s1.bound_geodes()
            if s1.nominal_max > s1.blueprint.max_geodes:
                self.blueprint.stack.append(s1)
                self.blueprint.states += 1
            return None
        else:
            runout = self.resources["geode"] + (self.bots["geode"] * self.minutes)
            if runout > self.blueprint.max_geodes:
                self.blueprint.max_geodes = runout
                self.blueprint.best = self.string + ("." * self.minutes)
            # self.blueprint.max_geodes = max(
            #     self.blueprint.max_geodes,
            #     self.resources["geode"] + self.bots["geode"] * self.minutes,
            # )
            return None

    # def get_resources(self):
    #     for rsc, bots in self.bots.items():
    #         self.resources[rsc] += bots
    #     return None

    # def make_bot(self, bot):
    #     for rsc, cost in self.blueprint.costs[bot].items():
    #         self.resources[rsc] -= cost
    #     self.bots[bot] += 1
    #     return None

    def bound_geodes(self):
        self.nominal_max = (
            self.resources["geode"]
            + (self.minutes * self.bots["geode"])
            + ((self.minutes * (self.minutes + 1)) // 2)
        )
        return None


with open("day19.input", "r") as f:
    quality = 0
    for row in f:
        b = Blueprint(row.strip())
        b.play()
        print(b.id * b.max_geodes, b.id, b.best, len(b.best), b.states)
        quality += b.id * b.max_geodes
print(quality)
