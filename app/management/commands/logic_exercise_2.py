from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = '''Your task in this exercise is as follows: Take the following selection of 70
    English Pokemon names (extracted from Wikipedia's list of Pokemon), and generate
    the/a sequence with the highest possible number of Pokemon names where the
    subsequent name starts with the final letter of the preceding name. No Pokemon
    name is to be repeated.
    '''

    longest_sequence = []

    def search_starts_letter(self, lastletter, pokemons):
        list_index = []
        for pokemon in pokemons:
            if pokemon.startswith(lastletter):
                list_index.append(pokemon)
        return list_index

    def search_sequence(self, pokemons, index_list, sequence=[]):
        for index in index_list:
            current_pokemon = index
            current_sequence = sequence.copy()
            current_sequence.append(current_pokemon)
            copy_pokemon = pokemons.copy()
            copy_pokemon.pop(copy_pokemon.index(current_pokemon))
            index = self.search_starts_letter(current_pokemon[-1], copy_pokemon)

            if index == [] and len(current_sequence) > len(self.longest_sequence):
                self.longest_sequence = current_sequence.copy()
            else:
                self.search_sequence(copy_pokemon, index, current_sequence)

    def handle(self, *args, **kwargs):
        pokemons = ["audino", "bagon", "baltoy", "banette", "bidoof", "braviary", "bronzor", "carracosta", "charmeleon",
                    "cresselia", "croagunk", "darmanitan", "deino", "emboar", "emolga", "exeggcute", "gabite",
                    "girafarig", "gulpin", "haxorus", "heatmor", "heatran", "ivysaur", "jellicent", "jumpluff",
                    "kangaskhan", "kricketune", "landorus", "ledyba", "loudred", "lumineon", "lunatone", "machamp",
                    "magnezone", "mamoswine", "nosepass", "petilil", "pidgeotto", "pikachu", "pinsir", "poliwrath",
                    "poochyena", "porygon2", "porygonz", "registeel", "relicanth", "remoraid", "rufflet", "sableye",
                    "scolipede", "scrafty", "seaking", "sealeo", "silcoon", "simisear", "snivy", "snorlax", "spoink",
                    "starly", "tirtouga", "trapinch", "treecko", "tyrogue", "vigoroth", "vulpix", "wailord",
                    "wartortle", "whismur", "wingull", "yamask"]

        for pokemon in pokemons:
            pokemons_copy = pokemons.copy()
            pokemons_copy.pop(pokemons_copy.index(pokemon))

            index_list = self.search_starts_letter(pokemon[-1], pokemons_copy)
            self.search_sequence(pokemons_copy, index_list, [pokemon])

        self.stdout.write("tamaño de la secuencia: {}".format(len(self.longest_sequence)))
        self.stdout.write("secuencia más larga: {}".format(self.longest_sequence))
