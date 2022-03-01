from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = """ Desarrolla un algoritmo que imprima los números del 0 al 100. Adicionalmente debe
    imprimirse en la misma línea la palabra buzz en caso de que el número sea par. Sí el
    número es múltiplo de 5 debe imprimirse en la misma línea la palabra bazz.
    """

    def handle(self, *args, **kwargs):
        for i in range(101):
            word = ""
            if i % 2 == 0:
                word += " buzz"
            if i % 5 == 0:
                word += " bazz"

            self.stdout.write("{}{}".format(i, word))
