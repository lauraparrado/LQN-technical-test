import json

from django_dynamic_fixture import G
from graphene_django.utils.testing import GraphQLTestCase
from graphql_relay import to_global_id

from app.models import Planet, Film, People
from swapi.schema import schema


class FirstTestCase(GraphQLTestCase):
    fixtures = ['app/fixtures/unittest.json']
    GRAPHQL_SCHEMA = schema

    def test_people_query(self):
        response = self.query(
            '''
                query{
                  allPlanets {
                    edges{
                      node{
                        id
                        name
                      }
                    }
                  }
                }
            ''',
        )
        self.assertResponseNoErrors(response)

        content = json.loads(response.content)
        self.assertEqual(len(content['data']['allPlanets']['edges']), 61)


class PeopleMutationTestCase(GraphQLTestCase):
    fixtures = ['app/fixtures/unittest.json']
    GRAPHQL_SCHEMA = schema

    def test_add_character(self):
        planet_test = G(Planet)
        film_test = G(Film)
        response = self.query(
            '''
            mutation ADD_CHARACTER($input: AddOrUpdateCharacterMutationInput!) {
              addOrUpdateCharacterMutation(input: $input) {
                character {
                  id
                  name
                  eyeColor
                  homeWorld {
                    name
                  }
                  films {
                    edges {
                      node {
                        title
                      }
                    }
                  }
                }
              }
            }
            ''',
            op_name="ADD_CHARACTER",
            input_data={
                "name": "seño adasaura",
                "homeWorld": to_global_id("PlanetType", planet_test.id),
                "films": [to_global_id("FilmType", film_test.id)],
                "eyeColor": "black"
            }
        )

        self.assertResponseNoErrors(response)
        self.assertEquals(response.status_code, 200)

    def test_update_character(self):
        people_test = G(People)

        response = self.query(
            '''
            mutation UPDATE_CHARACTER($input: AddOrUpdateCharacterMutationInput!) {
              addOrUpdateCharacterMutation(input: $input) {
                character {
                  id
                  name
                  eyeColor
                  homeWorld {
                    name
                  }
                  films {
                    edges {
                      node {
                        title
                      }
                    }
                  }
                }
              }
            }
            ''',
            op_name="UPDATE_CHARACTER",
            input_data={
                "id": to_global_id("PeopleType", people_test.id),
                "name": "test example",
            }
        )

        new_people_test = People.objects.get(id=people_test.id)
        self.assertResponseNoErrors(response)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(new_people_test.name, "test example")
