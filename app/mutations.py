import graphene
from graphql_relay import from_global_id

from .models import Planet, People, Film
from .types import PlanetType, FilmType, PeopleType
from .utils import generic_model_mutation_process


class AddOrUpdatePlanetMutation(graphene.relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=False)
        name = graphene.String(required=True)
        rotation_period = graphene.String(required=False)
        orbital_period = graphene.String(required=False)
        diameter = graphene.String(required=False)
        climate = graphene.String(required=False)
        gravity = graphene.String(required=False)
        terrain = graphene.String(required=False)
        surface_water = graphene.String(required=False)
        population = graphene.String(required=False)

    planet = graphene.Field(PlanetType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        raw_id = input.get('id', None)

        data = {'model': Planet, 'data': input}
        if raw_id:
            data['id'] = from_global_id(raw_id)[1]

        planet = generic_model_mutation_process(**data)
        return AddOrUpdatePlanetMutation(planet=planet)


class AddOrUpdateCharacterMutation(graphene.relay.ClientIDMutation):
    character = graphene.Field(PeopleType)

    class Input:
        id = graphene.ID(required=False)
        name = graphene.String(required=True)
        height = graphene.String(required=False)
        mass = graphene.String(required=False)
        hair_color = graphene.Enum('hair_color', People.HAIR_COLOR_CHOICE)(required=False)
        skin_color = graphene.String(required=False)
        eye_color = graphene.Enum('eye_color', People.EYE_COLOR_CHOICE)(required=False)
        birth_year = graphene.String(required=False)
        gender = graphene.Enum('gender', People.GENDER)(required=False)
        home_world = graphene.ID(required=False)
        films = graphene.List(graphene.ID, required=False)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        home_world = input.get('home_world', None)
        films = input.pop('films', None)
        raw_id = input.get('id', None)

        if home_world:
            input['home_world'] = Planet.objects.get(id=from_global_id(home_world)[1])

        data = {'model': People, 'data': input}

        if raw_id:
            data['id'] = from_global_id(raw_id)[1]

        people = generic_model_mutation_process(**data)

        if films:
            for i, film in enumerate(films):
                films[i] = from_global_id(film)[1]

            people.films.set(Film.objects.filter(id__in=films))

        return AddOrUpdateCharacterMutation(character=people)

