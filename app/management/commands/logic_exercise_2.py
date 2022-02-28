from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = '''Your task in this exercise is as follows: Take the following selection of 70
    English Pokemon names (extracted from Wikipedia's list of Pokemon), and generate
    the/a sequence with the highest possible number of Pokemon names where the
    subsequent name starts with the final letter of the preceding name. No Pokemon
    name is to be repeated.
    '''

    def search_starts_letter(self, lastletter, pokemons):
        for i, pokemon in enumerate(pokemons):
            if pokemon.startswith(lastletter):
               return i
        return False


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

        current_secuence = []
        longest_seceunce = []

        for pokemon in pokemons:
            current_pokemon = pokemon
            current_secuence.append(current_pokemon)

            pokemons_copy = pokemons.copy()
            pokemons_copy.pop(pokemons_copy.index(current_pokemon))

            index = self.search_starts_letter(current_pokemon[-1], pokemons_copy)

            while index is not False:
                current_pokemon = pokemons_copy[index]
                current_secuence.append(current_pokemon)
                pokemons_copy.pop(index)
                index = self.search_starts_letter(current_pokemon[-1], pokemons_copy)

            if len(current_secuence) > len(longest_seceunce):
                longest_seceunce = current_secuence

            current_secuence = []

        self.stdout.write("{}".format(longest_seceunce))


